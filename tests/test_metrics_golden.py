"""Golden metrics on the mock decisions (fixtures/mini/decisions_mock.jsonl), computed by hand.

Mock p(pii=A) per unit, gold pii_present, predicted subject_role (gold role):
  fx01 .97 A both(both)   fx02 .12 B none(none)     fx03 .62 A staff(staff)
  fx04 .29 A patient(pat) fx05 .83 A staff(both)    fx06#0 .72 A both(both)
  fx06#1 .21 A staff(pat) fx07 .38 B none(none)     fx08 .91 A patient(pat)
  fx09 .56 B none(none)   fx10 .87 A patient(both)
Identity calibration (T = 1), t_low = 0.25, t_high = 0.85, so every number below follows from
this table with pencil and paper. Tolerance 1e-9 (M2 gate).
"""

from pathlib import Path

import pytest

from bench import score as sc
from bench.config import load_policy
from bench.domain import CalibParams, Route, Scores
from bench.label import read_docs
from tests.fixture_expected import fixture_units

ROOT = Path(__file__).resolve().parent.parent
MINI = ROOT / "fixtures" / "mini"
POLICY = load_policy(ROOT / "config" / "policy.yaml")
TOL = 1e-9

IDENTITY = CalibParams(
    arm="mock",
    qs="qs_v1",
    temperatures={
        "pii_present:2": 1.0,
        "subject_role:4": 1.0,
        "category:5": 1.0,
        "doc_kind:4": 1.0,
    },
    t_low=0.25,
    t_high=0.85,
    recall_target=0.995,
    precision_target=0.98,
    fit_on="fixture_debug",
    content_hash="not-checked-here",
)


@pytest.fixture(scope="module")
def scores() -> Scores:
    docs = read_docs(MINI / "docs.jsonl")
    decisions = sc.read_decisions(MINI / "decisions_mock.jsonl")
    return sc.score(
        decisions,
        fixture_units(),
        docs,
        IDENTITY,
        POLICY,
        {"fixture": {d.id for d in docs}},
        None,
        {"docs": "d", "units": "u", "decisions": "x"},
    )


def close(a: float | None, b: float) -> bool:
    return a is not None and abs(a - b) < TOL


def test_pii_present_question(scores: Scores) -> None:
    m = scores.splits["fixture"].per_question["pii_present"]
    # predicted A iff p > .5: correct except fx04, fx06#1 (missed A) and fx09 (false A)
    assert close(m.accuracy, 8 / 11)
    assert m.confusion.labels == ["A", "B"]
    assert m.confusion.counts == [[6, 2], [1, 2]]
    f1_a = 2 * 6 / (2 * 6 + 1 + 2)  # tp 6, fp 1, fn 2 = 12/15
    f1_b = 2 * 2 / (2 * 2 + 2 + 1)  # tp 2, fp 2, fn 1 = 4/7
    assert close(m.per_class_f1["A"], f1_a) and close(m.per_class_f1["B"], f1_b)
    assert close(m.macro_f1, (f1_a + f1_b) / 2)
    assert m.majority_class == "A" and close(m.majority_baseline_accuracy, 8 / 11)


def test_other_questions(scores: Scores) -> None:
    pq = scores.splits["fixture"].per_question
    assert close(pq["subject_role"].accuracy, 8 / 11)  # fx05, fx06#1, fx10 wrong
    assert close(pq["category"].accuracy, 8 / 11)  # fx05, fx06#1, fx09 wrong
    assert close(pq["doc_kind"].accuracy, 1.0)
    assert pq["doc_kind"].majority_class == "form_table"  # 4 of 11 (fx03, 04, 08, 09)
    assert close(pq["doc_kind"].majority_baseline_accuracy, 4 / 11)
    assert scores.splits["fixture"].multilabel is None  # qs_v1 has no has_* questions


def test_ece_brier_auroc(scores: Scores) -> None:
    c = scores.splits["fixture"].calibration["pii_present"]
    # confidence = max prob; bins of width 1/15 (edges avoided by the mock values):
    #   bin 14: .97(ok)            gap .03
    #   bin 13: .88 .91 .87 (ok)   acc 1, mean .8867  3 * gap = 3 - 2.66 = .34
    #   bin 12: .83(ok)            gap .17
    #   bin 11: .79(wrong)         gap .79
    #   bin 10: .71(wrong) .72(ok) acc .5, mean .715  2 * gap = .43
    #   bin  9: .62 .62 (ok)       2 * gap = .76
    #   bin  8: .56(wrong)         gap .56
    expected_ece = (0.03 + 0.34 + 0.17 + 0.79 + 0.43 + 0.76 + 0.56) / 11
    assert close(c.ece_raw, expected_ece)
    assert close(c.ece_raw, 3.08 / 11)
    # binary Brier = 2 * (1 - p_gold)^2 per unit
    miss = [0.03, 0.12, 0.38, 0.71, 0.17, 0.28, 0.79, 0.38, 0.09, 0.56, 0.13]
    assert close(c.brier_raw, sum(2 * m**2 for m in miss) / 11)
    # correct confidences .97 .88 .62 .83 .72 .62 .91 .87 vs wrong .71 .79 .56:
    # 6 + 5 + 8 = 19 winning pairs of 24
    assert close(c.auroc_raw, 19 / 24)
    # identity temperature: calibrated == raw
    assert close(c.ece_calibrated, c.ece_raw) and close(c.brier_calibrated, c.brier_raw)
    assert sum(b.n for b in c.reliability_raw) == 11 and len(c.reliability_raw) == 15


def test_headline_recall_forward_rate(scores: Scores) -> None:
    h = scores.splits["fixture"].headline
    assert (h.n_units, h.n_docs, h.n_positive) == (11, 10, 8)
    assert h.recall is not None and close(h.recall.point, 7 / 8)  # only fx06#1 (.21) < .25
    assert close(h.forward_rate.point, 2 / 11)  # fx02 .12 and fx06#1 .21
    assert h.false_forwards == 1
    assert close(h.precision, 7 / 9)  # p >= .25: 7 positives + fx07, fx09
    assert h.recall.lo is not None and h.recall.hi is not None
    assert h.recall.lo <= h.recall.point <= h.recall.hi


def test_routing(scores: Scores) -> None:
    r = scores.splits["fixture"].routing
    assert r.counts == {Route.FORWARD: 2, Route.REDACT: 5, Route.ESCALATE: 4}
    assert r.by_gold_pii["A"] == {Route.FORWARD: 1, Route.REDACT: 5, Route.ESCALATE: 2}
    assert r.by_gold_pii["B"] == {Route.FORWARD: 1, Route.REDACT: 0, Route.ESCALATE: 2}
    assert r.triggers == {
        "p_at_or_above_t_high": 3,  # fx01, fx08, fx10
        "p_below_t_low": 2,
        "p_in_escalate_band": 4,  # fx03, fx05, fx07, fx09
        "role_both": 2,  # fx01, fx06#0
        "role_patient": 3,  # fx04, fx08, fx10
    }


def test_failure_gallery(scores: Scores) -> None:
    s = scores.splits["fixture"]
    assert [f.unit_id for f in s.failures] == ["fx06:chunk:512:1"]
    f = s.failures[0]
    assert f.missed_value_kinds == ["address"]
    assert "**2207 Quarry Hill Lane, Apartment 5B, Linden Valley, OR**" in f.text_markdown
    assert s.false_forward_value_kinds == {"address": 1}


def test_slices(scores: Scores) -> None:
    rows = {(r.dimension, r.value): r for r in scores.splits["fixture"].slices}
    mvr = rows[("doc_type", "monitoring_visit_report")]
    assert (mvr.n_units, mvr.n_docs, mvr.false_forwards) == (2, 1, 1)
    assert close(mvr.recall, 1 / 2) and close(mvr.forward_rate, 1 / 2)
    assert rows[("split_span", "yes")].n_units == 1
    assert rows[("lang", "de")].n_units == 1
    assert rows[("hard_negative", "yes")].recall is None  # fx07, fx09 have no positives
    assert all(r.small_sample for r in rows.values())


def test_speed(scores: Scores) -> None:
    sp = scores.speed
    lat = [61.0, 58.5, 60.2, 57.9, 59.4, 70.3, 64.8, 58.1, 60.7, 59.9, 62.6]
    assert sp.warmup_excluded == 2 and sp.batched is None
    assert sp.batch1 is not None and sp.batch1.n == 11
    assert close(sp.batch1.p50_ms, 60.2)  # median of the 11
    assert close(sp.batch1.units_per_sec, 11 / (sum(lat) / 1000))
    assert sp.per_doc_ms is not None and sp.per_doc_ms.n == 10  # fx06 = 70.3 + 64.8
    assert close(sp.per_doc_ms.mean_ms, sum(lat) / 10)
    assert sp.hardware.startswith("unknown hardware")


def test_primitives_directly() -> None:
    assert sc.recall_at([0.1, 0.5], [True, True], 0.25) == 0.5
    assert sc.recall_at([0.1], [False], 0.25) is None
    assert sc.auroc([0.5, 0.5], [True, False]) == 0.5
    assert sc.auroc([0.5], [True]) is None
    assert sc.majority(["b", "a", "a", "b"]) == ("a", 0.5)  # ties: alphabetical
    assert sc.latency_stats([]) is None
    assert sc.ece([1.0], [True]) == 0.0  # conf 1.0 lands in the last bin
    assert sc.route_unit(0.1, "patient", 0.25, 0.85, True) == (Route.REDACT, ["role_patient"])
    assert sc.route_unit(0.1, "patient", 0.25, 0.85, False)[0] is Route.FORWARD
    assert sc.route_unit(0.1, None, 0.25, 0.85, True)[0] is Route.FORWARD
