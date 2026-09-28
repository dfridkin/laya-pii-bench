"""M6 score/report additions: routed JSONL (C7), batched speed input (C6), autocast state (C8),
D-008 review flag and doc-level label, qs_v1 vs qs_v2 comparison."""

import json
from pathlib import Path

import pytest
import yaml
from typer.testing import CliRunner

from bench import report as rep
from bench import score as sc
from bench.cli import app
from bench.domain import Decision, Headline, Interval, RoutedDecision, RunMeta, Scores
from tests.gitutil import commit_file
from tests.test_freeze import DOCS, _calibrate, _run

RUN = CliRunner()


@pytest.fixture
def run(tmp_path: Path) -> dict[str, Path]:
    p = _run(tmp_path)
    assert _calibrate(p).startswith("0:")
    commit_file(p["calib"])
    return p


def _score(p: dict[str, Path], *extra: str) -> tuple[int, str]:
    args = ["score", "--decisions", str(p["dec"]), "--units", str(p["units"]), "--calib",
            str(p["calib"]), "--out", str(p["out"]), "--docs", str(DOCS), "--splits",
            str(p["splits"]), *extra]  # fmt: skip
    r = RUN.invoke(app, args)
    return r.exit_code, r.output


def _batched(p: dict[str, Path], units_hash: str | None = None) -> Path:
    d = p["dec"].parent.parent / "run__batch4"
    d.mkdir()
    rows = [Decision.model_validate_json(x) for x in p["dec"].read_text().splitlines()]
    out = [r.model_copy(update={"mode": "batched", "batch_size": 1 if r.warmup else 4,
                                "latency_ms": r.latency_ms / 3,
                                "autocast": True}) for r in rows]  # fmt: skip
    (d / "decisions.jsonl").write_text("".join(r.model_dump_json() + "\n" for r in out))
    meta = RunMeta.model_validate_json((p["dec"].parent / "meta.json").read_text())
    hashes = dict(meta.config_hashes)
    if units_hash:
        hashes["units"] = units_hash
    meta = meta.model_copy(update={"batch_size": 4, "config_hashes": hashes})
    (d / "meta.json").write_text(meta.model_dump_json())
    return d / "decisions.jsonl"


def test_routed_jsonl_matches_scored_routing(run: dict[str, Path]) -> None:
    code, out = _score(run)
    assert code == 0, out
    routed_path = run["out"].with_suffix(".routed.jsonl")
    routes = [RoutedDecision.model_validate_json(x) for x in routed_path.read_text().splitlines()]
    s = Scores.model_validate_json(run["out"].read_text())
    assert {r.split for r in routes} == set(s.splits) == {"test"}
    counts = s.splits["test"].routing.counts
    assert len(routes) == s.splits["test"].headline.n_units == sum(counts.values())
    for route, n in counts.items():
        assert sum(r.route == route for r in routes) == n
    assert all(not r.decision.warmup for r in routes)


def test_batched_run_feeds_speed_only(run: dict[str, Path]) -> None:
    assert _score(run)[0] == 0
    plain = Scores.model_validate_json(run["out"].read_text())
    code, out = _score(run, "--batched-decisions", str(_batched(run)))
    assert code == 0, out
    s = Scores.model_validate_json(run["out"].read_text())
    assert s.speed.batched is not None and s.speed.batched.n == s.speed.batch1.n  # type: ignore[union-attr]
    assert s.speed.batched_autocast == "on" and s.context.batched_decisions_sha256
    assert s.splits == plain.splits  # batched answers never enter a metric


def test_batched_run_of_other_units_is_refused(run: dict[str, Path]) -> None:
    code, out = _score(run, "--batched-decisions", str(_batched(run, units_hash="x" * 64)))
    assert code == 2 and "batched run units differ" in out


def test_autocast_state() -> None:
    d = Decision.model_validate_json(
        Path(__file__).parent.parent.joinpath("fixtures/mini/decisions_mock.jsonl")
        .read_text().splitlines()[0]
    )  # fmt: skip
    assert sc.autocast_state([d]) == "unknown"
    on, off = d.model_copy(update={"autocast": True}), d.model_copy(update={"autocast": False})
    assert sc.autocast_state([on, on]) == "on" and sc.autocast_state([off]) == "off"
    assert sc.autocast_state([on, off]) == "mixed"


def _headline(point: float, lo: float | None, n_pos: int = 50) -> Headline:
    return Headline(t_low=0.1, t_high=None, n_units=100, n_docs=20, n_positive=n_pos,
                    recall=Interval(point=point, lo=None, hi=None, n_resamples=0),
                    recall_exact_lo=lo, route_recall=point,
                    forward_rate=Interval(point=0.5, lo=None, hi=None, n_resamples=0),
                    false_forwards=0, precision=None)  # fmt: skip


def test_d008_gap_flags_above_one_point() -> None:
    assert sc.d008_gap(_headline(1.0, 0.95)) == pytest.approx(0.05)
    assert rep._gap(_headline(1.0, 0.995)).startswith("0.0050")  # pyright: ignore[reportPrivateUsage]
    assert "**review**" in rep._gap(_headline(1.0, 0.95))  # pyright: ignore[reportPrivateUsage]
    assert sc.d008_gap(_headline(1.0, None)) is None


def test_scores_caveat_d008_and_doc_level(run: dict[str, Path], tmp_path: Path) -> None:
    arms = tmp_path / "arms.yaml"
    cfg = yaml.safe_load((Path(__file__).parent.parent / "config" / "arms.yaml").read_text())
    cfg["arms"]["mock"] = {**cfg["arms"]["A"], "doc_level": True}
    arms.write_text(yaml.safe_dump(cfg))
    code, out = _score(run, "--arms", str(arms))
    assert code == 0, out
    s = Scores.model_validate_json(run["out"].read_text())
    assert s.context.doc_level and any(c.startswith("Doc-level arm") for c in s.caveats)
    h = s.splits["test"].headline
    gap = sc.d008_gap(h)
    assert (gap is not None and gap > sc.D008_GAP) == any(
        c.startswith("D-008 review") for c in s.caveats
    )
    text_md = rep.render([s])
    assert "(doc-level, underpowered)" in text_md and "point - exact lo" in text_md


def test_report_compares_question_sets(run: dict[str, Path]) -> None:
    assert _score(run)[0] == 0
    s = Scores.model_validate_json(run["out"].read_text())
    other = s.model_copy(update={"context": s.context.model_copy(update={"qs": "qs_v2"})})
    md = rep.render([s, other])
    assert "### qs_v1 vs qs_v2" in md
    table = md.split("### qs_v1 vs qs_v2", 1)[1]
    assert "| mock | test | qs_v1 |" in table and "| mock | test | qs_v2 |" in table
    assert "### qs_v1 vs qs_v2" not in rep.render([s])
    assert json.loads(s.model_dump_json())["speed"]["batch1_autocast"] == "unknown"
