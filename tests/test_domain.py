from typing import Any, get_args

import pytest
from pydantic import ValidationError

from bench.domain import (
    EXPORTED,
    Answer,
    CalibParams,
    CategoryAnswer,
    ChoiceQuestion,
    Decision,
    DocKindAnswer,
    Document,
    GoldAnswers,
    Negative,
    PiiCategory,
    QuestionSet,
    RoleAnswer,
    Route,
    RoutedDecision,
    Span,
    Unit,
)


def span(**kw: Any) -> Span:
    base: dict[str, Any] = {
        "start": 0,
        "end": 4,
        "category": "phi_direct",
        "role": "patient",
        "value_kind": "person_name",
        "surface": "first_last",
    }
    return Span.model_validate(base | kw)


def gold(**kw: Any) -> GoldAnswers:
    base: dict[str, Any] = {
        "pii_present": "A",
        "subject_role": "patient",
        "category": "direct",
        "doc_kind": "narrative",
        "categories_multi": {c.value: c is PiiCategory.PHI_DIRECT for c in PiiCategory},
    }
    return GoldAnswers.model_validate(base | kw)


def doc_dict(**kw: Any) -> dict[str, Any]:
    base: dict[str, Any] = {
        "id": "d1",
        "doc_type": "csr_patient_narrative",
        "lang": "en",
        "text": "Anna was seen.",
        "spans": [span().model_dump()],
        "negatives": [],
        "tags": [],
        "length_bucket": "short",
        "pii_depth": None,
        "world_refs": {"study": "FTX-1", "site": "S1", "subjects": ["1001-0001"]},
        "gen_meta": {"source": "fixture"},
    }
    return base | kw


def test_document_roundtrip() -> None:
    d = Document.model_validate(doc_dict())
    assert Document.model_validate_json(d.model_dump_json()) == d


def test_unknown_key_rejected() -> None:
    with pytest.raises(ValidationError):
        Document.model_validate(doc_dict(extra_field=1))


def test_models_frozen() -> None:
    s = span()
    with pytest.raises(ValidationError):
        s.start = 2  # type: ignore[misc]


@pytest.mark.parametrize(("start", "end"), [(3, 3), (5, 2)])
def test_empty_or_inverted_interval_rejected(start: int, end: int) -> None:
    with pytest.raises(ValidationError):
        span(start=start, end=end)
    with pytest.raises(ValidationError):
        Negative(start=start, end=end, kind="nct_id")


def test_negative_offsets_rejected() -> None:
    with pytest.raises(ValidationError):
        span(start=-1)


def test_bad_enums_rejected() -> None:
    with pytest.raises(ValidationError):
        span(category="phi")
    with pytest.raises(ValidationError):
        span(role="doctor")
    with pytest.raises(ValidationError):
        Document.model_validate(doc_dict(lang="fr"))


def test_gold_requires_every_category() -> None:
    with pytest.raises(ValidationError, match="categories_multi"):
        gold(categories_multi={"phi_direct": True})
    with pytest.raises(ValidationError):
        gold(pii_present="yes")


def test_unit_and_decision_types() -> None:
    u = Unit(
        id="d1:chunk:512:0",
        doc_id="d1",
        kind="chunk",
        start=0,
        end=10,
        tokens=4,
        tokenizer="english",
        truncated=False,
        split_span=False,
        gold=gold(),
    )
    ans = Answer(question="pii_present", choice="A", probs={"A": 0.9, "B": 0.1}, confidence=0.5)
    dec = Decision(
        unit_id=u.id,
        arm="A",
        qs="qs_v1",
        checkpoint="english",
        checkpoint_rev="abc",
        max_len=512,
        answers=[ans],
        latency_ms=60.0,
        t_offset_ms=0.0,
        batch_size=1,
    )
    assert dec.warmup is False
    routed = RoutedDecision(
        decision=dec, route=Route.FORWARD, triggers=[], calibrated_probs={"pii_present": ans.probs}
    )
    assert routed.route == "forward"
    with pytest.raises(ValidationError):
        Decision.model_validate(dec.model_dump() | {"batch_size": 0})


def test_calib_params_fit_on_calib_only() -> None:
    kw: dict[str, Any] = {
        "arm": "A",
        "qs": "qs_v1",
        "temperatures": {"pii_present:2": 1.3},
        "t_low": 0.1,
        "t_high": 0.9,
        "recall_target": 0.995,
        "precision_target": 0.98,
        "decisions_sha256": "d",
        "units_sha256": "u",
        "calib_doc_ids": ["d1"],
        "content_hash": "x",
    }
    CalibParams.model_validate(kw | {"fit_on": "calib"})
    with pytest.raises(ValidationError):
        CalibParams.model_validate(kw | {"fit_on": "test"})


def test_question_option_limits() -> None:
    with pytest.raises(ValidationError):
        ChoiceQuestion(type="choice", instructions="?", criteria={"A": "only one"})
    with pytest.raises(ValidationError):
        ChoiceQuestion(type="choice", instructions="?", criteria={str(i): "x" for i in range(11)})
    qs = QuestionSet.model_validate(
        {"id": "q", "questions": {"n": {"type": "noul", "instructions": "?"}}}
    )
    assert qs.questions["n"].type == "noul"


def test_gold_literals_match_answer_aliases() -> None:
    assert set(get_args(RoleAnswer)) == {"patient", "staff", "both", "none"}
    assert "none" in get_args(CategoryAnswer)
    assert len(get_args(DocKindAnswer)) == 4


def test_exported_models_have_schema() -> None:
    for model in EXPORTED:
        assert model.model_json_schema()["title"] == model.__name__
