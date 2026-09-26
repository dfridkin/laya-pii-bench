"""The hand-labeled fixture (M1): rebuilds exactly, validates, covers every required case."""

from pathlib import Path

import pytest

from bench.config import load_policy
from bench.domain import Document, PiiCategory, SubjectRole
from bench.fixture import build, dumps
from bench.models import pinned
from bench.validate import validate_file

ROOT = Path(__file__).resolve().parent.parent
MINI = ROOT / "fixtures" / "mini"


@pytest.fixture(scope="module")
def docs() -> dict[str, Document]:
    return {d.id: d for d in build(MINI / "src")}


def cats(d: Document) -> set[PiiCategory]:
    return {s.category for s in d.spans}


def test_committed_jsonl_matches_sources() -> None:
    assert dumps(build(MINI / "src")) == (MINI / "docs.jsonl").read_text(encoding="utf-8"), (
        "fixtures/mini/docs.jsonl is stale: run `uv run bench build-fixture`"
    )


def test_all_valid() -> None:
    report = validate_file(MINI / "docs.jsonl", load_policy(ROOT / "config" / "policy.yaml"))
    assert report.ok and report.n_valid == 10


def test_ten_distinct_cases(docs: dict[str, Document]) -> None:
    assert len(docs) == 10
    assert len({d.gen_meta["case"] for d in docs.values()}) == 10


def test_dense_phi_narrative(docs: dict[str, Document]) -> None:
    d = docs["fx01"]
    assert d.doc_type == "csr_patient_narrative"
    assert set(PiiCategory) == cats(d)
    kinds = {s.value_kind for s in d.spans}
    assert {"person_name", "dob", "mrn", "address", "phone", "zip", "initials"} <= kinds


def test_clean_protocol(docs: dict[str, Document]) -> None:
    d = docs["fx02"]
    assert d.doc_type == "protocol_section" and not d.spans and not d.negatives


def test_staff_only_delegation_log(docs: dict[str, Document]) -> None:
    d = docs["fx03"]
    assert d.doc_type == "delegation_log" and "table" in d.tags
    assert cats(d) == {PiiCategory.STAFF_PII}
    assert {s.role for s in d.spans} == {SubjectRole.STAFF}


def test_crf_subject_ids_only(docs: dict[str, Document]) -> None:
    d = docs["fx04"]
    assert d.doc_type == "crf_page" and "table" in d.tags
    assert {s.value_kind for s in d.spans} == {"subject_id"}
    assert cats(d) == {PiiCategory.CODED_ID}


def test_email_thread_with_signature(docs: dict[str, Document]) -> None:
    d = docs["fx05"]
    assert d.doc_type == "site_correspondence" and "email_quoting" in d.tags
    assert "Best regards" in d.text and "\n> " in d.text
    assert cats(d) == {PiiCategory.STAFF_PII, PiiCategory.CODED_ID}


def test_hard_negative_only(docs: dict[str, Document]) -> None:
    d = docs["fx07"]
    assert not d.spans and "hard_negative" in d.tags
    kinds = {n.kind for n in d.negatives}
    assert {"protocol_no", "nct_id", "lot_no", "eponym"} <= kinds
    assert "Kaplan-Meier" in [d.text[n.start : n.end] for n in d.negatives]


def test_ocr_noisy_mrn(docs: dict[str, Document]) -> None:
    d = docs["fx08"]
    assert "ocr_noise" in d.tags
    mrn = [s for s in d.spans if s.value_kind == "mrn"]
    assert len(mrn) == 1 and mrn[0].surface == "ocr_noisy"
    assert mrn[0].category == PiiCategory.PHI_DIRECT


def test_pre_redacted(docs: dict[str, Document]) -> None:
    d = docs["fx09"]
    assert not d.spans and {"hard_negative", "pre_redacted"} <= set(d.tags)
    redacted = [d.text[n.start : n.end] for n in d.negatives if n.kind == "pre_redacted"]
    assert "[REDACTED]" in redacted


def test_german(docs: dict[str, Document]) -> None:
    d = docs["fx10"]
    assert d.lang == "de" and PiiCategory.PHI_DIRECT in cats(d)


def test_fictional_contact_details(docs: dict[str, Document]) -> None:
    # Invariant 10: reserved example domains and 555 numbers only.
    for d in docs.values():
        for s in d.spans:
            value = d.text[s.start : s.end]
            if s.value_kind == "email":
                assert value.endswith((".example.org", ".example.com")), value
            if s.value_kind == "phone":
                assert "555" in value, value


@pytest.mark.model
def test_fx06_span_straddles_token_256(docs: dict[str, Document]) -> None:
    """Arm A chunks are 256 tokens; the segmenter may back off up to 8 tokens to whitespace."""
    from tokenizers import Tokenizer

    tok = Tokenizer.from_file(
        str(pinned("english", ROOT / "models.lock.json").snapshot / "tokenizer" / "tokenizer.json")
    )
    d = docs["fx06"]
    offsets = tok.encode(d.text, add_special_tokens=False).offsets
    crossing = [
        s
        for s in d.spans
        if (idx := [i for i, (a, b) in enumerate(offsets) if a < s.end and b > s.start])
        and idx[0] < 256 - 8
        and idx[-1] >= 256
    ]
    assert crossing, "no span covers tokens 248..256"
