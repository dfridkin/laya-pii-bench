"""End-to-end calibrate -> score -> report on the fixture mock decisions (M2 gates 2 and 3)."""

import json
import re
from pathlib import Path

import pytest
from typer.testing import CliRunner

from bench.cli import app
from bench.domain import Scores
from bench.label import write_units
from bench.report import SECTIONS, render
from tests.fixture_expected import fixture_units
from tests.gitutil import commit_file

ROOT = Path(__file__).resolve().parent.parent
MINI = ROOT / "fixtures" / "mini"
RUN = CliRunner()


def metrics_md_sections() -> list[str]:
    text = (ROOT / "docs" / "specs" / "metrics.md").read_text()
    return re.findall(r"^\d+\. \*\*(.+?):?\*\*", text, flags=re.M)


@pytest.fixture(scope="module")
def pipeline(tmp_path_factory: pytest.TempPathFactory) -> dict[str, Path]:
    d = tmp_path_factory.mktemp("m2")
    paths = {
        "units": d / "units.jsonl",
        "calib": d / "calib" / "mock__qs_v1.json",
        "scores": d / "scores" / "mock__qs_v1.json",
        "report": d / "report.md",
    }
    write_units(fixture_units(), paths["units"])
    common = ["--decisions", str(MINI / "decisions_mock.jsonl"), "--units", str(paths["units"])]
    r = RUN.invoke(app, ["calibrate", *common, "--out", str(paths["calib"]), "--debug-fit-all",
                         "--allow-no-meta"])  # fmt: skip
    assert r.exit_code == 0, r.output
    commit_file(paths["calib"])  # D-019: score reads only committed calib
    r = RUN.invoke(
        app,
        ["score", *common, "--calib", str(paths["calib"]), "--out", str(paths["scores"]),
         "--docs", str(MINI / "docs.jsonl"), "--hw", str(d / "no-hw.json"), "--allow-debug-calib",
         "--allow-no-meta"],
    )  # fmt: skip
    assert r.exit_code == 0, r.output
    r = RUN.invoke(app, ["report", "--scores", str(paths["scores"]), "--out", str(paths["report"])])
    assert r.exit_code == 0, r.output
    return paths


def test_sections_match_metrics_spec() -> None:
    assert metrics_md_sections() == list(SECTIONS)


def test_report_has_every_section(pipeline: dict[str, Path]) -> None:
    text = pipeline["report"].read_text()
    for i, name in enumerate(metrics_md_sections(), start=1):
        assert f"\n## {i}. {name}\n" in text, name
    assert "DEBUG REPORT" in text
    assert "fixture: 0 false forward(s)" in text  # in-sample t_low misses nothing


def test_gallery_renders_false_forwards() -> None:
    from bench import score as sc
    from bench.label import read_docs
    from tests.test_metrics_golden import IDENTITY, POLICY

    docs = read_docs(MINI / "docs.jsonl")
    scores = sc.score(sc.read_decisions(MINI / "decisions_mock.jsonl"), fixture_units(), docs,
                      IDENTITY, POLICY, {"fixture": {d.id for d in docs}}, None,
                      {"docs": "d", "units": "u", "decisions": "x"})  # fmt: skip
    text = render([scores])
    assert "fixture: 1 false forward(s)" in text
    assert "**fx06:chunk:512:1** route forward" in text
    assert "**2207 Quarry Hill Lane, Apartment 5B, Linden Valley, OR**" in text


def test_debug_fit_on_mock_has_perfect_in_sample_recall(pipeline: dict[str, Path]) -> None:
    s = Scores.model_validate_json(pipeline["scores"].read_text())
    h = s.splits["fixture"].headline
    assert s.context.calib_fit_on == "fixture_debug"
    assert h.recall is not None and h.recall.point == 1.0  # t_low = min positive p (0 misses of 8)
    assert h.false_forwards == 0


def test_tampered_calib_exits_nonzero(pipeline: dict[str, Path], tmp_path: Path) -> None:
    calib = json.loads(pipeline["calib"].read_text())
    calib["t_low"] = 0.01
    bad = tmp_path / "mock__qs_v1.json"
    bad.write_text(json.dumps(calib))
    r = RUN.invoke(
        app,
        ["score", "--decisions", str(MINI / "decisions_mock.jsonl"), "--units",
         str(pipeline["units"]), "--calib", str(bad), "--out", str(tmp_path / "s.json"),
         "--docs", str(MINI / "docs.jsonl"), "--allow-debug-calib", "--allow-no-meta"],
    )  # fmt: skip
    assert r.exit_code != 0
    assert "hash mismatch" in r.output
    assert not (tmp_path / "s.json").exists()


def test_debug_calib_needs_explicit_flag(pipeline: dict[str, Path], tmp_path: Path) -> None:
    r = RUN.invoke(
        app,
        ["score", "--decisions", str(MINI / "decisions_mock.jsonl"), "--units",
         str(pipeline["units"]), "--calib", str(pipeline["calib"]), "--out",
         str(tmp_path / "s.json"), "--docs", str(MINI / "docs.jsonl")],
    )  # fmt: skip
    assert r.exit_code != 0 and "allow-debug-calib" in r.output


def test_calibrate_refuses_without_calib_split(pipeline: dict[str, Path], tmp_path: Path) -> None:
    r = RUN.invoke(
        app,
        ["calibrate", "--decisions", str(MINI / "decisions_mock.jsonl"), "--units",
         str(pipeline["units"]), "--out", str(tmp_path / "c.json")],
    )  # fmt: skip
    assert r.exit_code != 0 and not (tmp_path / "c.json").exists()


def test_report_hud_note_and_empty(pipeline: dict[str, Path], tmp_path: Path) -> None:
    r = RUN.invoke(
        app,
        ["report", "--scores-dir", str(pipeline["scores"].parent), "--out",
         str(tmp_path / "r.md"), "--hud", str(tmp_path / "replay.json")],
    )  # fmt: skip
    assert r.exit_code == 0 and "M7" in r.output
    assert not (tmp_path / "replay.json").exists()
    with pytest.raises(ValueError):
        render([])


def test_report_without_scores_is_a_clean_error(tmp_path: Path) -> None:
    r = RUN.invoke(app, ["report", "--scores-dir", str(tmp_path), "--out", str(tmp_path / "r.md")])
    assert r.exit_code == 2 and "no scores" in r.output
    assert not isinstance(r.exception, ValueError)  # was an uncaught "no scores to report"


def test_multilabel_and_every_reliability_table_render() -> None:
    from bench import score as sc
    from bench.domain import Answer, Decision
    from bench.label import read_docs
    from tests.test_metrics_golden import IDENTITY, POLICY

    qs = ["pii_present", "has_phi_direct", "has_phi_quasi", "has_coded_id", "has_staff_pii"]
    decisions = [
        Decision(unit_id=u.id, arm="mock", qs="qs_v2", checkpoint="english", checkpoint_rev="M",
                 max_len=512, latency_ms=1.0, t_offset_ms=0.0, batch_size=1,
                 answers=[Answer(question=q, choice="A", probs={"A": 0.7, "B": 0.3}, confidence=0.1)
                          for q in qs])
        for u in fixture_units()
    ]  # fmt: skip
    calib = IDENTITY.model_copy(update={"qs": "qs_v2", "temperatures": {f"{q}:2": 1.0 for q in qs}})
    docs = read_docs(MINI / "docs.jsonl")
    text = render([sc.score(decisions, fixture_units(), docs, calib, POLICY,
                            {"fixture": {d.id for d in docs}}, None,
                            {"docs": "d", "units": "u", "decisions": "x"})])  # fmt: skip
    assert "Multi-label categories: micro-F1" in text
    for q in qs:
        assert f"Reliability data, `{q}`" in text
