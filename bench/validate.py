"""Document validation: offset integrity, overlap, enums, policy consistency (`make fixture`).

Pydantic enforces enums and field shapes; the checks here cover what a single model can't see:
offsets against the text, intervals against each other, and spans against the label policy.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from dataclasses import dataclass, field
from pathlib import Path

from pydantic import ValidationError

from bench.config import Policy
from bench.domain import Document, LengthBucket, Negative, PiiCategory, Span, SubjectRole

KNOWN_TAGS = frozenset(
    {
        "hard_negative",
        "pre_redacted",
        "table",
        "ocr_noise",
        "line_wrap",
        "headers_footers",
        "email_quoting",
    }
)

PATIENT_CATEGORIES = frozenset(
    {PiiCategory.PHI_DIRECT, PiiCategory.PHI_QUASI, PiiCategory.CODED_ID}
)
STAFF_ROLES = frozenset({SubjectRole.STAFF, SubjectRole.SPONSOR})


@dataclass
class DocResult:
    line: int
    doc_id: str | None
    errors: list[str] = field(default_factory=lambda: [])

    @property
    def ok(self) -> bool:
        return not self.errors


@dataclass
class Report:
    results: list[DocResult]

    @property
    def n_valid(self) -> int:
        return sum(r.ok for r in self.results)

    @property
    def ok(self) -> bool:
        return bool(self.results) and self.n_valid == len(self.results)


def _splits_word(text: str, pos: int) -> bool:
    """True if `pos` falls between two alphanumeric characters (an edge cutting a token)."""
    return 0 < pos < len(text) and text[pos - 1].isalnum() and text[pos].isalnum()


def _check_offsets(text: str, name: str, items: Sequence[Span | Negative]) -> Iterable[str]:
    for i, it in enumerate(items):
        if it.end > len(text):
            yield f"{name}[{i}] end {it.end} beyond text length {len(text)}"
            continue
        value = text[it.start : it.end]
        if value != value.strip():
            yield f"{name}[{i}] {value!r} has leading/trailing whitespace"
        if _splits_word(text, it.start) or _splits_word(text, it.end):
            yield f"{name}[{i}] {value!r} starts or ends inside a word"
    starts = [it.start for it in items]
    if starts != sorted(starts):
        yield f"{name} not sorted by start"


def _overlaps(a: Span | Negative, b: Span | Negative) -> bool:
    return a.start < b.end and b.start < a.end


def _check_overlap(doc: Document) -> Iterable[str]:
    for group, items in (("spans", doc.spans), ("negatives", doc.negatives)):
        for i in range(1, len(items)):
            if _overlaps(items[i - 1], items[i]):
                yield f"{group}[{i - 1}] and {group}[{i}] overlap"
    for i, s in enumerate(doc.spans):
        for j, n in enumerate(doc.negatives):
            if _overlaps(s, n):
                yield f"spans[{i}] overlaps negatives[{j}]"


def _check_policy(doc: Document, policy: Policy) -> Iterable[str]:
    if doc.doc_type not in policy.doc_kind_map:
        yield f"doc_type {doc.doc_type} missing from policy.doc_kind_map"
    for i, s in enumerate(doc.spans):
        if s.category in PATIENT_CATEGORIES and s.role is not SubjectRole.PATIENT:
            yield f"spans[{i}] category {s.category} requires role patient, got {s.role}"
        if s.category is PiiCategory.STAFF_PII and s.role not in STAFF_ROLES:
            yield f"spans[{i}] category staff_pii requires role staff or sponsor, got {s.role}"


def _check_tags(doc: Document) -> Iterable[str]:
    unknown = sorted(set(doc.tags) - KNOWN_TAGS)
    if unknown:
        yield f"unknown tags {unknown}"
    if len(set(doc.tags)) != len(doc.tags):
        yield "duplicate tags"
    if bool(doc.negatives) != ("hard_negative" in doc.tags):
        yield "tag hard_negative must be present iff the doc has negatives"
    if doc.pii_depth is not None and doc.length_bucket not in (LengthBucket.LONG, LengthBucket.XL):
        yield "pii_depth is only set on long or xl docs"


def check_document(doc: Document, policy: Policy) -> list[str]:
    errors = [
        *_check_offsets(doc.text, "spans", doc.spans),
        *_check_offsets(doc.text, "negatives", doc.negatives),
    ]
    if not errors:  # overlap checks assume in-bounds, sorted intervals
        errors += _check_overlap(doc)
    errors += _check_policy(doc, policy)
    errors += _check_tags(doc)
    return errors


def validate_lines(lines: Iterable[str], policy: Policy) -> Report:
    results: list[DocResult] = []
    seen: dict[str, int] = {}
    for lineno, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            doc = Document.model_validate_json(line)
        except ValidationError as e:
            errs = [f"{'.'.join(map(str, x['loc']))}: {x['msg']}" for x in e.errors()]
            results.append(DocResult(lineno, None, errs))
            continue
        res = DocResult(lineno, doc.id, check_document(doc, policy))
        if doc.id in seen:
            res.errors.append(f"duplicate id (first on line {seen[doc.id]})")
        seen.setdefault(doc.id, lineno)
        results.append(res)
    return Report(results)


def validate_file(path: Path, policy: Policy) -> Report:
    with path.open(encoding="utf-8") as f:
        return validate_lines(f, policy)
