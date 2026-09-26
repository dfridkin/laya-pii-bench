"""Calib provenance (audit A1): score refuses gold or calib that doesn't belong to the run."""

from pathlib import Path

import pytest
from typer.testing import CliRunner

from bench import score as sc
from bench.cli import app
from bench.domain import CalibParams, HwInfo, RunMeta
from bench.label import write_units
from tests.fixture_expected import fixture_units

ROOT = Path(__file__).resolve().parent.parent
MINI = ROOT / "fixtures" / "mini"
RUN = CliRunner()


def calib(**kw: object) -> CalibParams:
    base: dict[str, object] = {
        "arm": "a", "qs": "q", "temperatures": {}, "t_low": 0.5, "t_high": None,
        "recall_target": 0.995, "precision_target": 0.98, "fit_on": "calib",
        "decisions_sha256": "d", "units_sha256": "u", "calib_doc_ids": ["c1", "c2"],
        "content_hash": "x",
    }  # fmt: skip
    return CalibParams.model_validate(base | kw)


def test_disjoint_calib_passes_and_overlap_fails() -> None:
    sc.verify_provenance(calib(), "u", "docs", None, {"t1", "t2"})
    with pytest.raises(sc.ScoreError, match="used to fit calib"):
        sc.verify_provenance(calib(), "u", "docs", None, {"t1", "c2"})
    # the labeled fixture fit is in-sample by design
    sc.verify_provenance(calib(fit_on="fixture_debug"), "u", "docs", None, {"c1"})


def test_units_must_match_calib_and_run() -> None:
    with pytest.raises(sc.ScoreError, match="calib was fit on different units"):
        sc.verify_provenance(calib(), "OTHER", "docs", None, set())
    with pytest.raises(sc.ScoreError, match="units file differs"):
        sc.verify_provenance(calib(), "u", "docs", {"units": "RUN", "docs": "docs"}, set())
    with pytest.raises(sc.ScoreError, match="docs file differs"):
        sc.verify_provenance(calib(), "u", "docs", {"units": "u", "docs": "RUN"}, set())


def test_flipped_gold_is_refused_end_to_end(tmp_path: Path) -> None:
    """The audit's reproduction: relabeled units must not score against an existing calib."""
    units = tmp_path / "units.jsonl"
    write_units(fixture_units(), units)
    c = tmp_path / "c.json"
    common = ["--decisions", str(MINI / "decisions_mock.jsonl"), "--units", str(units)]
    assert (
        RUN.invoke(app, ["calibrate", *common, "--out", str(c), "--debug-fit-all"]).exit_code == 0
    )
    flipped = tmp_path / "flipped.jsonl"
    write_units(
        [u.model_copy(update={"gold": u.gold.model_copy(update={
            "pii_present": "B" if u.gold.pii_present == "A" else "A"})}) for u in fixture_units()],
        flipped,
    )  # fmt: skip
    r = RUN.invoke(app, ["score", "--decisions", str(MINI / "decisions_mock.jsonl"),
                         "--units", str(flipped), "--calib", str(c), "--out",
                         str(tmp_path / "s.json"), "--docs", str(MINI / "docs.jsonl"),
                         "--allow-debug-calib"])  # fmt: skip
    assert r.exit_code == 2 and "calib was fit on different units" in r.output
    assert not (tmp_path / "s.json").exists()


def test_calibrate_refuses_units_other_than_the_runs(tmp_path: Path) -> None:
    run_dir = tmp_path / "run"
    run_dir.mkdir()
    (run_dir / "decisions.jsonl").write_text((MINI / "decisions_mock.jsonl").read_text())
    hw = HwInfo(os="o", arch="a", cpu="c", ram_gb=8, python="p", torch="t", laya="l",
                device="mps", device_name="n", checkpoints={}, created_at="x")  # fmt: skip
    meta = RunMeta(arm="mock", qs="qs_v1", dataset="mini", hw=hw, device="mps",
                   checkpoint="english", checkpoint_rev="r", config_hashes={"units": "0" * 64},
                   batch_size=1, warmup_calls=2, sessions=1, started_at="x",
                   finished_at="y")  # fmt: skip
    (run_dir / "meta.json").write_text(meta.model_dump_json())
    units = tmp_path / "units.jsonl"
    write_units(fixture_units(), units)
    r = RUN.invoke(app, ["calibrate", "--decisions", str(run_dir / "decisions.jsonl"),
                         "--units", str(units), "--out", str(tmp_path / "c.json"),
                         "--debug-fit-all"])  # fmt: skip
    assert r.exit_code == 2 and "differs from the units this run was produced from" in r.output
