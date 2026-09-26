"""Domain model: the contract every stage reads and writes (docs/specs/domain.md).

JSON Schema is exported from these types (`bench schema`); the HUD's TS types are generated from
that schema. Change a type here first, then everything downstream.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class _Model(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class DocType(StrEnum):
    PROTOCOL = "protocol_section"
    ICF = "icf_signature_page"
    CRF = "crf_page"
    SAE = "sae_cioms"
    NARRATIVE = "csr_patient_narrative"
    MONITORING = "monitoring_visit_report"
    DEVIATION = "deviation_log"
    LAB = "lab_report"
    CONMED = "conmed_log"
    DELEGATION = "delegation_log"
    IRB = "irb_letter"
    SITE_EMAIL = "site_correspondence"


class PiiCategory(StrEnum):
    PHI_DIRECT = "phi_direct"  # name, MRN, SSN-like, phone, email, street address, full DOB
    PHI_QUASI = "phi_quasi"  # event/visit dates, age > 89, ZIP, initials, rare dx + site
    CODED_ID = "coded_id"  # subject no., randomization no. (policy-dependent, D-001)
    STAFF_PII = "staff_pii"  # investigator / coordinator / CRA name + contact


class SubjectRole(StrEnum):
    PATIENT = "patient"
    STAFF = "staff"
    SPONSOR = "sponsor"


class LengthBucket(StrEnum):
    SHORT = "short"  # < 1k tokens
    MEDIUM = "medium"  # 1-4k
    LONG = "long"  # 4-8k
    XL = "xl"  # > 8k


class PiiDepth(StrEnum):
    EARLY = "early"
    MIDDLE = "middle"
    LATE = "late"


Lang = Literal["en", "de", "es", "pl"]
PiiAnswer = Literal["A", "B"]  # A = yes, B = no (neutral keys, D-006)
RoleAnswer = Literal["patient", "staff", "both", "none"]
CategoryAnswer = Literal["direct", "quasi", "coded", "staff", "none"]
DocKindAnswer = Literal["narrative", "form_table", "correspondence", "protocol_text"]
UnitKind = Literal["chunk", "section", "doc"]
Split = Literal["train", "calib", "test", "holdout"]


class _Interval(_Model):
    start: int = Field(ge=0)
    end: int = Field(ge=0)  # char offsets into Document.text, end exclusive

    @model_validator(mode="after")
    def _nonempty(self) -> _Interval:
        if self.end <= self.start:
            raise ValueError(f"empty or inverted interval [{self.start}, {self.end})")
        return self


class Span(_Interval):
    category: PiiCategory
    role: SubjectRole
    value_kind: str  # "person_name", "mrn", "dob", "subject_id", ...
    surface: str  # variant generator used, e.g. "last_first_upper"


class Negative(_Interval):
    kind: str  # "protocol_no", "nct_id", "lot_no", "eponym", ...


class WorldRefs(_Model):
    study: str
    site: str
    subjects: list[str]


class Document(_Model):
    id: str
    doc_type: DocType
    lang: Lang
    text: str
    spans: list[Span]
    negatives: list[Negative]
    tags: list[str]  # hard_negative, table, ocr_noise, line_wrap, ...
    length_bucket: LengthBucket
    pii_depth: PiiDepth | None
    world_refs: WorldRefs
    gen_meta: dict[str, str | int | list[str]]


class GoldAnswers(_Model):
    pii_present: PiiAnswer
    subject_role: RoleAnswer
    category: CategoryAnswer  # precedence-flattened
    doc_kind: DocKindAnswer
    categories_multi: dict[PiiCategory, bool]  # for qs_v2

    @model_validator(mode="after")
    def _all_categories(self) -> GoldAnswers:
        if set(self.categories_multi) != set(PiiCategory):
            raise ValueError("categories_multi must have exactly one entry per PiiCategory")
        return self


class Unit(_Model):
    id: str  # f"{doc_id}:{kind}:{max_len}:{idx}"
    doc_id: str
    kind: UnitKind
    start: int = Field(ge=0)
    end: int = Field(ge=0)
    tokens: int = Field(ge=0)
    tokenizer: str
    truncated: bool
    split_span: bool  # a gold span crosses a unit boundary
    gold: GoldAnswers


class ChoiceQuestion(_Model):
    type: Literal["choice"]
    instructions: str
    criteria: dict[str, str] = Field(min_length=2, max_length=10)  # <= 10 options (runtime spec)


class ScoreQuestion(_Model):
    type: Literal["score"]
    instructions: str
    criteria: list[str] = Field(min_length=2, max_length=10)


class NoulQuestion(_Model):
    type: Literal["noul"]  # never on the English checkpoint (invariant 5); enforced by the runner
    instructions: str


Question = Annotated[ChoiceQuestion | ScoreQuestion | NoulQuestion, Field(discriminator="type")]


class QuestionSet(_Model):
    id: str
    questions: dict[str, Question] = Field(min_length=1)


class Answer(_Model):
    question: str
    choice: str
    probs: dict[str, float]
    confidence: float


class Route(StrEnum):
    FORWARD = "forward"
    REDACT = "redact"
    ESCALATE = "escalate"


class Decision(_Model):
    """One per unit per run; also the HUD trace event."""

    unit_id: str
    arm: str
    qs: str
    checkpoint: str
    checkpoint_rev: str
    max_len: int
    answers: list[Answer]  # RAW probabilities (invariant 4)
    latency_ms: float
    t_offset_ms: float
    batch_size: int = Field(ge=1)
    warmup: bool = False


class RoutedDecision(_Model):
    """Produced by the score stage only (routing never happens in the runner)."""

    decision: Decision
    route: Route
    triggers: list[str]
    calibrated_probs: dict[str, dict[str, float]]


Device = Literal["cuda", "mps", "cpu"]


class HwInfo(_Model):
    """Hardware fingerprint (`hw.json`), attached to every run (invariant 9)."""

    os: str
    arch: str
    cpu: str
    ram_gb: float
    python: str
    torch: str
    laya: str
    device: Device
    device_name: str
    checkpoints: dict[str, str]
    created_at: str


class RunMeta(_Model):
    arm: str
    qs: str
    hw: HwInfo
    checkpoint_rev: str
    config_hashes: dict[str, str]
    warmup_calls: int = Field(ge=0)
    started_at: str
    finished_at: str | None


class CalibParams(_Model):
    arm: str
    qs: str
    temperatures: dict[str, float]  # key f"{question}:{n_options}"
    t_low: float
    t_high: float
    recall_target: float
    precision_target: float
    fit_on: Literal["calib"]
    content_hash: str


# Exported to schema/ and to the HUD. Scores joins this list in M2 (docs/specs/domain.md).
EXPORTED: tuple[type[BaseModel], ...] = (
    Document,
    Unit,
    QuestionSet,
    Decision,
    RoutedDecision,
    RunMeta,
    CalibParams,
    HwInfo,
)
