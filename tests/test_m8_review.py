"""M8 results-review fixes: lexical baselines, per-point t_high on the curve, C findings."""

import json
from pathlib import Path
from types import SimpleNamespace
from typing import Any

from bench import baseline as bl
from bench import report as rep
from bench import score as sc
from bench.cli import _run_caveats  # pyright: ignore[reportPrivateUsage]
from bench.config import load_policy
from bench.domain import CalibParams, Decision, Headline, Interval, RunMeta
from tests.test_freeze import HW

POLICY = load_policy(Path("config/policy.yaml"))


def _row(p: float, positive: bool) -> Any:
    return SimpleNamespace(p_pii=p, positive=positive, cal={"pii_present": {"A": p, "B": 1 - p}})


def test_curve_raises_t_high_to_each_points_t_low() -> None:
    rows = [_row(0.99, True), _row(0.95, True), _row(0.97, False), _row(0.1, False)]
    calib = CalibParams.model_construct(t_high=0.9, t_low_curve={"0.9": 0.98, "0.995": 0.9})
    by = {c.target: c for c in sc.curve(rows, calib, POLICY)}
    # strict point: 0.95 and 0.97 fall below t_low and are forwarded, not redacted by t_high 0.9
    assert by[0.9].false_forwards == 1 and by[0.9].forward_rate == 0.75
    assert by[0.995].false_forwards == 0 and by[0.995].forward_rate == 0.25
    none = CalibParams.model_construct(t_high=None, t_low_curve={"0.9": 0.98})
    assert sc.curve(rows, none, POLICY)[0].forward_rate == 0.75


def _data_dir(tmp: Path) -> Path:
    tmp.mkdir()
    units = [
        ("u1", "Patient Jane Roe, MRN 4471", "A"),
        ("u2", "Dosing schedule table", "B"),
        ("u3", "Contact John Doe at 555-0101", "A"),
        ("u4", "Storage at 2-8 C", "B"),
    ]
    (tmp / "texts.jsonl").write_text(
        "".join(json.dumps({"unit_id": u, "text": t}) + "\n" for u, t, _ in units)
    )
    (tmp / "records.jsonl").write_text(
        "".join(
            json.dumps({"unit_id": u, "question": q, "label": lab}) + "\n"
            for u, _, lab in units
            for q in ("pii_present", "subject_role")
        )
    )
    (tmp / "manifest.json").write_text("{}")
    return tmp


def test_baseline_trains_on_pii_present_and_writes_a_run(tmp_path: Path) -> None:
    data = _data_dir(tmp_path / "data")
    x, y, _ = bl.training_set(data)
    assert len(x) == 4 and y == [1, 0, 1, 0]
    texts = {"t1": "Patient Mary Major, MRN 9", "t2": "Storage table"}
    probs: list[list[float]] = []
    for out in (tmp_path / "r1", tmp_path / "r2"):
        meta = bl.run("word", data, texts, out, HW, {"units": "u"})
        rows = [
            Decision.model_validate_json(r)
            for r in (out / "decisions.jsonl").read_text().splitlines()
        ]
        assert [r.unit_id for r in rows] == ["t1", "t2"]
        assert all(len(r.answers) == 1 and r.answers[0].question == "pii_present" for r in rows)
        probs.append([r.answers[0].probs["A"] for r in rows])
        assert RunMeta.model_validate_json((out / "meta.json").read_text()) == meta
        assert meta.checkpoint == "baseline-word" and "finetune_manifest" in meta.config_hashes
    assert probs[0] == probs[1]  # deterministic
    assert probs[0][0] > probs[0][1]


def _h(**kw: Any) -> Headline:
    base: dict[str, Any] = dict(
        t_low=0.97, t_high=0.97, n_units=1000, n_docs=100, n_positive=419,
        recall=Interval(point=0.995, lo=None, hi=None, n_resamples=0), recall_exact_lo=0.98,
        route_recall=1 - 1 / 419,
        forward_rate=Interval(point=0.926, lo=None, hi=None, n_resamples=0),
        false_forwards=1, precision=None, recall_target=0.995, auroc_pii=0.99987,
    )  # fmt: skip
    return Headline(**{**base, **kw})


def test_c_finding_states_route_recall_bounds_and_no_review_band() -> None:
    a = _h(auroc_pii=0.786, forward_rate=Interval(point=0.005, lo=None, hi=None, n_resamples=0))
    text = rep._c_finding("qs_v1", a, _h())  # pyright: ignore[reportPrivateUsage]
    assert "0.9999" in text and "1 of 419 PII units forwarded" in text
    assert "not rejected, not demonstrated" in text and "no review band" in text
    assert "no review band" not in rep._c_finding("qs_v1", a, _h(t_high=0.99))  # pyright: ignore[reportPrivateUsage]
    lo, hi = rep._route_bounds(_h())  # pyright: ignore[reportPrivateUsage]
    assert lo is not None and hi is not None and lo < 418 / 419 < hi
    assert rep._verdict(0.99, 0.999, 0.995) == "not rejected, not demonstrated"  # pyright: ignore[reportPrivateUsage]
    assert rep._verdict(0.9, 0.99, 0.995) == "missed"  # pyright: ignore[reportPrivateUsage]


def test_in_distribution_caveat_cites_the_best_baseline() -> None:
    by = {("C", "qs_v1"): _h(), ("LW", "qs_v1"): _h(auroc_pii=0.993),
          ("LC", "qs_v1"): _h(auroc_pii=0.9936)}  # fmt: skip
    text = rep._in_distribution(by)[0]  # pyright: ignore[reportPrivateUsage]
    assert "in-distribution" in text and "0.9936" in text and "arm LC" in text
    assert "not measured" in rep._in_distribution({("C", "qs_v1"): _h()})[0]  # pyright: ignore[reportPrivateUsage]
    assert rep._in_distribution({("A", "qs_v1"): _h()}) == []  # pyright: ignore[reportPrivateUsage]


def test_run_caveats_name_baselines_and_kaggle_hardware() -> None:
    hw = HW.model_copy(update={"device_name": "Tesla T4"})
    base = SimpleNamespace(checkpoint="baseline-word", device="cpu", hw=hw)
    assert "Lexical baseline" in _run_caveats(base)[0]
    cuda = SimpleNamespace(checkpoint="english", device="cuda", hw=hw)
    assert "Tesla T4" in _run_caveats(cuda)[0]
    assert _run_caveats(SimpleNamespace(checkpoint="english", device="mps", hw=hw)) == []
