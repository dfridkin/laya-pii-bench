"""Edge cases and mutation-killers from the M0-M3 audit (reports/audits/M0-M3-audit-*.md)."""

from pathlib import Path
from typing import Any

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from bench import calibrate as cal
from bench import score as sc
from bench.config import load_policy
from bench.domain import (
    Answer,
    CalibParams,
    Decision,
    Document,
    GoldAnswers,
    PiiCategory,
    Route,
    Unit,
)

ROOT = Path(__file__).resolve().parent.parent
POLICY = load_policy(ROOT / "config" / "policy.yaml")
HASHES = {"decisions": "d" * 64, "units": "u" * 64}
CALIB = CalibParams(
    arm="t", qs="q", temperatures={"pii_present:2": 1.0}, t_low=0.5, t_high=0.9,
    recall_target=0.995, precision_target=0.98, fit_on="calib", decisions_sha256="d",
    units_sha256="u", calib_doc_ids=[], content_hash="x",
)  # fmt: skip


def gold(pii: str) -> GoldAnswers:
    return GoldAnswers(
        pii_present=pii,  # type: ignore[arg-type]
        subject_role="patient" if pii == "A" else "none",
        category="direct" if pii == "A" else "none",
        doc_kind="narrative",
        categories_multi={c: pii == "A" and c is PiiCategory.PHI_DIRECT for c in PiiCategory},
    )


def rows(spec: list[tuple[str, float, str]]) -> list[sc.Row]:
    """spec: (doc_id, p(pii=A), gold pii) per unit."""
    docs: dict[str, Document] = {}
    units: dict[str, Unit] = {}
    decisions: list[Decision] = []
    for i, (doc_id, p, g) in enumerate(spec):
        docs.setdefault(doc_id, Document.model_validate({
            "id": doc_id, "doc_type": "csr_patient_narrative", "lang": "en", "text": "x" * 10,
            "spans": [], "negatives": [], "tags": [], "length_bucket": "short", "pii_depth": None,
            "world_refs": {"study": "s", "site": "1", "subjects": []}, "gen_meta": {},
        }))  # fmt: skip
        uid = f"{doc_id}:chunk:512:{i}"
        units[uid] = Unit(
            id=uid, doc_id=doc_id, kind="chunk", start=0, end=10, tokens=3, tokenizer="t",
            truncated=False, split_span=False, gold=gold(g),
        )  # fmt: skip
        ans = Answer(question="pii_present", choice="A" if p > 0.5 else "B",
                     probs={"A": p, "B": 1 - p}, confidence=0.5)  # fmt: skip
        decisions.append(Decision(unit_id=uid, arm="t", qs="q", checkpoint="c", checkpoint_rev="r",
                                  max_len=512, answers=[ans], latency_ms=1.0, t_offset_ms=0.0,
                                  batch_size=1))  # fmt: skip
    return sc.build_rows(decisions, units, docs, CALIB, POLICY)


# --- bootstrap ----------------------------------------------------------------------------------


def test_bootstrap_resamples_documents_not_units() -> None:
    # doc a: two positives, both caught; doc b: one positive, missed. Document resamples of size 2
    # give (a,a) = 4/4, (a,b) = 2/3, (b,b) = 0/2. Resampling units would also produce 1/3.
    rs = rows([("a", 0.9, "A"), ("a", 0.8, "A"), ("b", 0.1, "A")])
    values = sc.bootstrap_values(rs, lambda x: sc._recall(x, 0.5), 2000, 7)  # pyright: ignore[reportPrivateUsage]
    assert all(v in (0.0, 1.0) or abs(v - 2 / 3) < 1e-12 for v in values)
    assert 0.0 in values and 1.0 in values


def test_bootstrap_is_deterministic_and_drops_undefined() -> None:
    # doc n has no positives: resamples of only n have undefined recall and are dropped
    rs = rows([("p", 0.9, "A"), ("p", 0.2, "A"), ("n", 0.1, "B")])
    a = sc.bootstrap(rs, lambda x: sc._recall(x, 0.5), 2000, 7)  # pyright: ignore[reportPrivateUsage]
    b = sc.bootstrap(rs, lambda x: sc._recall(x, 0.5), 2000, 7)  # pyright: ignore[reportPrivateUsage]
    assert a == b and a is not None
    assert 1000 < a.n_resamples < 2000  # ~25% of resamples are (n, n)


def test_one_document_has_no_ci() -> None:
    rs = rows([("a", 0.9, "A"), ("a", 0.2, "A"), ("a", 0.8, "A")])
    ci = sc.bootstrap(rs, lambda x: sc._recall(x, 0.5), 2000, 7)  # pyright: ignore[reportPrivateUsage]
    assert ci is not None and ci.point == pytest.approx(2 / 3)
    assert ci.lo is None and ci.hi is None and ci.n_resamples == 0


# --- exact bound, route recall ------------------------------------------------------------------


@pytest.mark.parametrize("n", [1, 8, 100, 900])
def test_exact_lower_bound_zero_misses_closed_form(n: int) -> None:
    # Clopper-Pearson with n/n: lower = (alpha/2)^(1/n)
    assert sc.exact_recall_lo(n, n) == pytest.approx(0.025 ** (1 / n), rel=1e-9)


def test_exact_lower_bound_edges() -> None:
    assert sc.exact_recall_lo(0, 5) == 0.0
    assert sc.exact_recall_lo(0, 0) is None
    assert sc.exact_recall_lo(99, 100) < sc.exact_recall_lo(100, 100)  # type: ignore[operator]


def test_headline_route_recall_and_exact_lo() -> None:
    rs = rows([("a", 0.9, "A"), ("b", 0.2, "A"), ("c", 0.1, "B"), ("d", 0.95, "A")])
    h = sc.headline(rs, CALIB, POLICY)
    assert h.recall is not None and h.recall.point == pytest.approx(2 / 3)
    # b (p .2) is forwarded? role question absent -> threshold only -> FORWARD: 1 false forward
    assert h.false_forwards == 1 and h.route_recall == pytest.approx(2 / 3)
    assert h.recall_exact_lo == pytest.approx(sc.exact_recall_lo(2, 3))


# --- routing ties, reliability edge, macro-F1 labels --------------------------------------------


def test_route_at_exactly_t_high_redacts() -> None:
    assert sc.route_unit(0.9, None, 0.5, 0.9, True) == (Route.REDACT, ["p_at_or_above_t_high"])
    assert sc.route_unit(0.5, None, 0.5, 0.9, True)[0] is Route.ESCALATE  # p == t_low
    assert sc.route_unit(1.0, None, 0.5, None, True)[0] is Route.ESCALATE  # no t_high


def test_confidence_one_lands_in_last_bin() -> None:
    bins = sc.reliability([1.0, 1.0, 0.5], [True, True, False])
    assert bins[-1].n == 2 and bins[-2].n == 0 and bins[7].n == 1


def test_macro_f1_counts_prediction_only_labels() -> None:
    # gold never says b; predicting b is an error that macro-F1 must see
    assert sc.per_class_f1(["a", "a"], ["a", "b"]) == {"a": pytest.approx(2 / 3), "b": 0.0}
    assert sc.macro_f1(["a", "a"], ["a", "b"]) == pytest.approx(1 / 3)


# --- temperature bounds and fallback ------------------------------------------------------------


def test_all_correct_drives_t_to_lower_bound_and_falls_back() -> None:
    rows_ = [[0.9, 0.1], [0.8, 0.2], [0.7, 0.3]]
    # the NLL keeps falling as T -> 0; the fit stops at the 0.05 lower bound (pinned literal)
    assert cal.fit_temperature(rows_, [0, 0, 0]) == pytest.approx(0.05, rel=1e-3)
    assert cal.fit_or_fallback(rows_, [0, 0, 0]) == (1.0, "calib accuracy 1.0")
    assert cal.fit_or_fallback(rows_, [1, 1, 1]) == (1.0, "calib accuracy 0.0")


def test_uninformative_confident_rows_hit_upper_bound_and_fall_back() -> None:
    # p = .9 but right exactly half the time: the NLL optimum is T -> infinity (p -> .5)
    t, reason = cal.fit_or_fallback([[0.9, 0.1]] * 4, [0, 1, 0, 1])
    assert t == 1.0 and reason is not None and reason.startswith("fit hit bound")


def test_fallbacks_recorded_in_calib_params() -> None:
    from tests.fixture_expected import fixture_units

    mock = (ROOT / "fixtures/mini/decisions_mock.jsonl").read_text().splitlines()
    decisions = [Decision.model_validate_json(x) for x in mock]
    params = cal.fit(
        decisions, {u.id: u for u in fixture_units()}, POLICY, "fixture_debug", input_hashes=HASHES
    )
    assert params.temperature_fallbacks == {"doc_kind:4": "calib accuracy 1.0"}
    assert params.temperatures["doc_kind:4"] == 1.0


# --- properties -----------------------------------------------------------------------------------

labels = st.lists(st.sampled_from("abc"), min_size=1, max_size=30)


@settings(max_examples=300)
@given(st.data())
def test_metric_ranges(data: Any) -> None:
    g = data.draw(labels)
    p = data.draw(st.lists(st.sampled_from("abc"), min_size=len(g), max_size=len(g)))
    assert 0.0 <= sc.accuracy(g, p) <= 1.0
    assert 0.0 <= sc.macro_f1(g, p) <= 1.0
    conf = data.draw(st.lists(st.floats(0, 1), min_size=len(g), max_size=len(g)))
    correct = [a == b for a, b in zip(g, p, strict=True)]
    assert 0.0 <= sc.ece(conf, correct) <= 1.0
    auc = sc.auroc(conf, correct)
    if auc is not None:
        assert 0.0 <= auc <= 1.0
        flipped = sc.auroc(conf, [not c for c in correct])
        assert flipped is not None and auc + flipped == pytest.approx(1.0)
