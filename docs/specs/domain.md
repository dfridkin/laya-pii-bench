# Spec: domain model (`bench/domain.py`)

Pydantic v2, `model_config = ConfigDict(extra="forbid", frozen=True)` on every model.
This file is the contract. JSON Schema is exported from it; the HUD's TS types are generated from
the schema. Change types here first.

```python
from enum import StrEnum
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field

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
    PHI_DIRECT = "phi_direct"    # name, MRN, SSN-like, phone, email, street address, full DOB
    PHI_QUASI = "phi_quasi"      # event/visit dates, age > 89, ZIP, initials, rare dx + site
    CODED_ID = "coded_id"        # subject no., randomization no. (policy-dependent, D-001)
    STAFF_PII = "staff_pii"      # investigator / coordinator / CRA name + contact

class SubjectRole(StrEnum):
    PATIENT = "patient"; STAFF = "staff"; SPONSOR = "sponsor"

class LengthBucket(StrEnum):
    SHORT = "short"; MEDIUM = "medium"; LONG = "long"; XL = "xl"   # <1k, 1-4k, 4-8k, >8k tokens

class PiiDepth(StrEnum):
    EARLY = "early"; MIDDLE = "middle"; LATE = "late"

class Span(BaseModel):
    start: int; end: int                       # char offsets into Document.text, end exclusive
    category: PiiCategory; role: SubjectRole
    value_kind: str                            # "person_name", "mrn", "dob", "subject_id", ...
    surface: str                               # variant generator used, e.g. "last_first_upper"

class Negative(BaseModel):
    start: int; end: int
    kind: str                                  # "protocol_no", "nct_id", "lot_no", "eponym", ...

class WorldRefs(BaseModel):
    study: str; site: str; subjects: list[str]

class Document(BaseModel):
    id: str; doc_type: DocType; lang: Literal["en", "de", "es", "pl"]
    text: str
    spans: list[Span]; negatives: list[Negative]
    tags: list[str]                            # hard_negative, table, ocr_noise, line_wrap, ...
    length_bucket: LengthBucket; pii_depth: PiiDepth | None
    world_refs: WorldRefs
    gen_meta: dict[str, str | int | list[str]]

UnitKind = Literal["chunk", "section", "doc"]

class Unit(BaseModel):
    id: str                                    # f"{doc_id}:{kind}:{max_len}:{idx}"
    doc_id: str; kind: UnitKind; start: int; end: int
    tokens: int; tokenizer: str; truncated: bool
    split_span: bool                           # a gold span crosses a unit boundary
    gold: "GoldAnswers"

class GoldAnswers(BaseModel):
    pii_present: Literal["A", "B"]             # A = yes, B = no (neutral keys, D-006)
    subject_role: Literal["patient", "staff", "both", "none"]
    category: Literal["direct", "quasi", "coded", "staff", "none"]   # precedence-flattened
    doc_kind: Literal["narrative", "form_table", "correspondence", "protocol_text"]
    categories_multi: dict[PiiCategory, bool]  # for qs_v2

class Answer(BaseModel):
    question: str; choice: str
    probs: dict[str, float]; confidence: float
    answer_confidence: float | None = None     # laya max-p confidence, stored for D-014

class Route(StrEnum):
    FORWARD = "forward"; REDACT = "redact"; ESCALATE = "escalate"

class Decision(BaseModel):                     # one per unit per run; also the HUD trace event
    unit_id: str; arm: str; qs: str
    checkpoint: str; checkpoint_rev: str; max_len: int
    answers: list[Answer]                      # RAW probabilities (invariant 4)
    latency_ms: float; t_offset_ms: float; batch_size: int
    warmup: bool = False
    state_tokens: int | None = None            # as the checkpoint tokenizer sees the state
    truncated_questions: list[str] = []        # questions whose input cut the state (inv. 7)

class RoutedDecision(BaseModel):               # produced by score stage only
    decision: Decision; route: Route; triggers: list[str]
    calibrated_probs: dict[str, dict[str, float]]

class RunMeta(BaseModel):
    arm: str; qs: str; dataset: str; hw: HwInfo
    device: Device                             # actual device after laya fallback
    checkpoint: str; checkpoint_rev: str
    config_hashes: dict[str, str]; batch_size: int; warmup_calls: int; sessions: int
    started_at: str; finished_at: str | None

class CalibParams(BaseModel):
    arm: str; qs: str
    temperatures: dict[str, float]             # key f"{question}:{n_options}"
    t_low: float; t_high: float; recall_target: float; precision_target: float
    fit_on: Literal["calib", "fixture_debug"]   # fixture_debug: D-013 (OPEN)
    content_hash: str
```

`Scores` mirrors the sections in `docs/specs/metrics.md`; define it when building M2.
