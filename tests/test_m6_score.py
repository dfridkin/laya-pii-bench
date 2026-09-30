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
from bench.label import read_docs
from tests.fixture_expected import fixture_units
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
    assert sc.d008_gap(_headline(1.0, 0.995)) == pytest.approx(0.005)
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
    assert not any(c.startswith("D-008 review") for c in s.caveats)  # arm mock, not A
    text_md = rep.render([s])
    assert "(doc-level, underpowered)" in text_md and "point - exact lo" in text_md
    assert "### Holdout (descriptive only, D-005)" not in text_md.split("### Test (headline)")[0]


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


def test_latency_outliers_counted_and_caveated() -> None:
    assert sc.outliers([100.0] * 99 + [600.0]) == 1 and sc.outliers([]) == 0
    assert sc.outliers([100.0] * 99 + [400.0]) == 0
    lat = sc.latency_stats([100.0] * 99 + [600.0])
    sp = sc.SpeedMetrics(hardware="h", batch1=lat, batched=None, per_doc_ms=None,
                         warmup_excluded=0, batch1_outliers=1)  # fmt: skip
    cal = sc.CalibParams.model_validate_json(
        next((Path(__file__).parent.parent / "calib" / "mini").glob("mock*.json")).read_text()
    )
    assert any("batch-1 calls took over 5x" in c for c in sc.caveats({}, cal, sp=sp))
    assert not any("took over" in c for c in sc.caveats({}, cal, sp=sp.model_copy(
        update={"batch1_outliers": 0})))  # fmt: skip


def test_exact_upper_bound_and_target() -> None:
    assert sc.exact_recall_hi(10, 10) == 1.0 and sc.exact_recall_hi(0, 0) is None
    hi = sc.exact_recall_hi(79, 85)
    assert hi is not None and 0.97 < hi < 0.98  # the M6 review's B3/qs_v2 figure
    h = _headline(0.929, 0.85).model_copy(update={"recall_target": 0.995, "recall_exact_hi": hi})
    assert "**missed**" in rep._target(h)  # pyright: ignore[reportPrivateUsage]


def test_d008_flag_only_on_arm_a_test(run: dict[str, Path]) -> None:
    assert _score(run)[0] == 0
    s = Scores.model_validate_json(run["out"].read_text())
    h = _headline(1.0, 0.97)
    a = s.model_copy(update={"context": s.context.model_copy(update={"arm": "A"})})
    assert "D-008 review" in rep._d008(a, "test", h)  # pyright: ignore[reportPrivateUsage]
    assert "D-008 review" not in rep._d008(a, "holdout", h)  # pyright: ignore[reportPrivateUsage]
    assert "D-008 review" not in rep._d008(s, "test", h)  # pyright: ignore[reportPrivateUsage]


def test_outliers_are_judged_within_length_buckets() -> None:
    ms = [100.0] * 50 + [900.0] * 10  # long units are slow, not outliers
    toks = [300] * 50 + [6000] * 10
    assert sc.outliers(ms, toks) == 0 and sc.outliers(ms) == 10
    assert sc.outliers([*ms, 5000.0], [*toks, 6000]) == 1


def test_drift_ratio() -> None:
    d = Decision.model_validate_json(
        Path(__file__).parent.parent.joinpath("fixtures/mini/decisions_mock.jsonl")
        .read_text().splitlines()[0]
    )  # fmt: skip
    rows = [d.model_copy(update={"state_tokens": 256, "latency_ms": 100.0 + i}) for i in range(80)]
    r = sc.drift(rows)
    assert r is not None and 1.0 < r < 1.8
    assert sc.drift(rows[:40]) is None


def test_findings_name_degenerate_and_weak_runs(run: dict[str, Path]) -> None:
    assert _score(run)[0] == 0
    s = Scores.model_validate_json(run["out"].read_text())
    h = s.splits["test"].headline.model_copy(update={
        "forward_rate": Interval(point=0.004, lo=0.0, hi=0.01, n_resamples=10),
        "auroc_pii": 0.4})  # fmt: skip
    sp = s.splits["test"].model_copy(update={"headline": h})
    weak = s.model_copy(update={"splits": {**s.splits, "test": sp}})
    md = rep.render([weak])
    assert "nearly degenerate" in md and "barely rank PII" in md


def test_gallery_highlights_only_counted_spans() -> None:
    from bench.config import load_policy
    from bench.domain import PiiCategory, Route

    policy = load_policy(Path(__file__).parent.parent / "config" / "policy.yaml")
    docs = read_docs(DOCS)
    doc = next(d for d in docs if any(s.category is PiiCategory.CODED_ID for s in d.spans))
    unit = next(u for u in fixture_units() if u.doc_id == doc.id)
    d = Decision.model_validate_json(
        Path(__file__).parent.parent.joinpath("fixtures/mini/decisions_mock.jsonl")
        .read_text().splitlines()[0]
    )  # fmt: skip
    row = sc.Row(unit, doc, d, {}, {}, Route.FORWARD, [])
    coded = [s for s in doc.spans if s.category is PiiCategory.CODED_ID
             and unit.start <= s.start and s.end <= unit.end]  # fmt: skip
    assert coded
    md = sc.highlight(row, policy.effective_pii_categories)
    esc = [sc._md_escape(doc.text[s.start : s.end]) for s in coded]  # pyright: ignore[reportPrivateUsage]
    assert all(f"**{v}**" not in md for v in esc)
    assert any(f"**{v}**" in sc.highlight(row) for v in esc)
