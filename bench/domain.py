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
Device = Literal["cuda", "mps", "cpu"]


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
    value: str | None = None  # text[start:end] at generation; validate checks it (D-016)


class Negative(_Interval):
    kind: str  # "protocol_no", "nct_id", "lot_no", "eponym", ...
    value: str | None = None  # text[start:end] at generation


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
    # generator bookkeeping; `sections` holds section start offsets (ints) for section units (M5)
    gen_meta: dict[str, str | int | list[str] | list[int]]


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
    confidence: float  # laya `confidence` (choice: 1 - normalized entropy)
    answer_confidence: float | None = None  # laya `answer_confidence` (max p); D-014


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
    batch_size: int = Field(ge=1)  # states in this call (a batched run's tail may be smaller)
    mode: Literal["batch1", "batched"] = "batch1"  # run mode; speed stats split on this
    device: Device | None = None  # device laya reported after this call
    # laya's autocast switch after this call (MPS fp16 at >= 5 question rows); laya turns it off
    # for good after one failed autocast forward, which changes speed mid-run (audit C8)
    autocast: bool | None = None
    # laya returned NaN probabilities on the first call and this is the single retry (M6: seen on
    # long B4 calls under memory pressure; the same unit is clean in isolation)
    retried: bool = False
    warmup: bool = False
    # State tokens as the checkpoint tokenizes them, and the questions whose input cut the state
    # short (laya's per-question room: max_len - prompt head - specials). Invariant 7.
    state_tokens: int | None = None
    truncated_questions: list[str] = Field(default_factory=lambda: [])


class RoutedDecision(_Model):
    """Produced by the score stage only (routing never happens in the runner)."""

    decision: Decision
    route: Route
    triggers: list[str]
    calibrated_probs: dict[str, dict[str, float]]
    split: str | None = None  # the scored split the unit's document belongs to


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
    dataset: str  # "main" for data/docs.jsonl, else the docs file's directory name
    hw: HwInfo
    device: Device  # device the checkpoint actually ran on (after any laya fallback)
    checkpoint: str
    checkpoint_rev: str
    config_hashes: dict[str, str]  # arm config, question set, docs, units
    batch_size: int = Field(ge=1)
    warmup_calls: int = Field(ge=0)  # per session
    sessions: int = Field(ge=1)  # 1 + number of resumes that made calls
    started_at: str
    finished_at: str | None
    release_every: int | None = None  # calls between allocator releases (outside the timer)


class CalibParams(_Model):
    arm: str
    qs: str
    temperatures: dict[str, float]  # key f"{question}:{n_options}"
    # keys whose fit was degenerate (calib accuracy 0 or 1, or the optimum hit a bound) and fell
    # back to T = 1, with the reason; reported, never silent
    temperature_fallbacks: dict[str, str] = Field(default_factory=lambda: {})
    t_low: float
    t_high: float | None  # None: no observed threshold reaches precision_target; no p-based redact
    recall_target: float
    precision_target: float
    # "fixture_debug": fit on the fixture itself (no calib split exists); score refuses it unless
    # explicitly allowed, and the report labels it. Real runs are always "calib" (invariant 3).
    fit_on: Literal["calib", "fixture_debug"]
    # provenance (covered by content_hash): what the params were fit on. `score` checks that the
    # units match, and that calib docs are disjoint from scored docs unless fit_on=fixture_debug.
    decisions_sha256: str
    units_sha256: str
    calib_doc_ids: list[str]
    content_hash: str


# --- splits and label manifest (M5) -------------------------------------------------------------


class Splits(_Model):
    """`data/splits.json`: every document's split (D-005 amended, D-016, D-018)."""

    seed: int
    docs_sha256: str
    config_sha256: str
    doc_split: dict[str, Split]  # doc id -> split
    groups: dict[str, Split]  # group key -> split: "study/site", "sponsor:<doc id>", "holdout"
    counts: dict[Split, int]  # documents per split


class ArmLabelStats(_Model):
    arm: str
    kind: UnitKind
    tokenizer: str  # checkpoint@revision that counted tokens
    units_sha256: str
    n_units: int
    by_split: dict[Split, int]
    truncated: dict[Split, int]
    split_span: dict[Split, int]
    # question set -> question -> split -> gold class -> units
    classes: dict[str, dict[str, dict[Split, dict[str, int]]]]


class LabelManifest(_Model):
    """`data/label_manifest.json` (M5 gates 2-4)."""

    docs_sha256: str
    policy_sha256: str
    splits_sha256: str
    arms: dict[str, ArmLabelStats]
    # "<arm>/<qs>/<question>/<split>: <class>" for every class missing in train/calib/test
    missing: list[str]
    holdout_missing: list[str]  # same for holdout (reported, not a gate failure; D-005)


# --- generator manifest -----------------------------------------------------------------------


class ValidatorResult(_Model):
    name: str  # "V1".."V6"
    passed: bool
    failures: int
    detail: list[str]  # first failures, for the log


class GenManifest(_Model):
    seed: int
    n_docs: int
    sha256: str  # of data/docs.jsonl
    gen_spec_sha256: str
    counts: dict[str, dict[str, int]]  # dimension -> value -> docs (doc_type, lang, bucket, ...)
    rates: dict[str, float]  # tag -> realized share of docs
    validators: list[ValidatorResult]
    created_at: str


# --- scores (docs/specs/metrics.md; one section per report section) ---------------------------


class Interval(_Model):
    point: float
    lo: float | None  # 95% document-level bootstrap CI; None if not estimable
    hi: float | None
    n_resamples: int  # resamples where the statistic was defined


class Headline(_Model):
    t_low: float
    t_high: float | None
    n_units: int
    n_docs: int
    n_positive: int
    recall: Interval | None  # pii_present recall at t_low; None without positives
    # exact (Clopper-Pearson) 95% lower bound on unit-level recall at t_low; ignores within-document
    # clustering (optimistic), but unlike the bootstrap it is informative when there are no misses
    recall_exact_lo: float | None
    route_recall: float | None  # 1 - false_forwards / n_positive (routing incl. role override)
    forward_rate: Interval
    false_forwards: int
    precision: float | None  # of p(pii) >= t_low; None if nothing is above t_low
    # M6 review: what the operating point is worth, not only what it catches
    recall_target: float | None = None  # the calib-fit target (D-007)
    recall_exact_hi: float | None = None  # exact 95% upper bound: < target -> target missed
    specificity: float | None = None  # forwarded negatives / negatives
    auroc_pii: float | None = None  # discrimination: calibrated p(pii) vs gold pii_present
    # AUROC of each positive type (direct > staff > quasi-only) against all negatives
    auroc_by_kind: dict[str, float | None] = Field(default_factory=lambda: {})
    truncated_forwarded: int = 0  # forwarded units whose tail the model never saw


class ConfusionMatrix(_Model):
    labels: list[str]
    counts: list[list[int]]  # rows = gold, columns = predicted, both in `labels` order


class QuestionMetrics(_Model):
    n: int
    accuracy: float
    macro_f1: float  # over labels present in gold or predictions
    per_class_f1: dict[str, float]
    confusion: ConfusionMatrix
    majority_class: str
    majority_baseline_accuracy: float


class MultiLabelMetrics(_Model):
    questions: list[str]
    micro_f1: float
    macro_f1: float
    per_label_f1: dict[str, float]


class ReliabilityBin(_Model):
    lo: float
    hi: float
    n: int
    mean_confidence: float | None
    accuracy: float | None


class CalibrationMetrics(_Model):
    n: int
    ece_raw: float  # 15 equal-width bins on max probability
    ece_calibrated: float
    brier_raw: float  # multi-class: mean over units of sum_k (p_k - y_k)^2
    brier_calibrated: float
    auroc_raw: float | None  # max probability as a score for correctness; None if one class
    auroc_calibrated: float | None
    reliability_raw: list[ReliabilityBin]
    reliability_calibrated: list[ReliabilityBin]


class RoutingMetrics(_Model):
    counts: dict[Route, int]
    by_gold_pii: dict[str, dict[Route, int]]  # gold pii_present -> route -> count
    triggers: dict[str, int]


class SliceRow(_Model):
    dimension: str
    value: str
    n_units: int
    n_docs: int
    n_positive: int
    recall: float | None
    forward_rate: float
    false_forwards: int
    pii_accuracy: float
    small_sample: bool  # n_units < 30


class FailureCase(_Model):
    unit_id: str
    doc_id: str
    text_markdown: str  # unit text with gold spans in bold
    route: Route
    triggers: list[str]
    gold: GoldAnswers
    raw_probs: dict[str, dict[str, float]]
    calibrated_probs: dict[str, dict[str, float]]
    missed_value_kinds: list[str]


class SplitScores(_Model):
    coverage_units: int  # units in this split
    coverage_decided: int  # of those, units with a decision
    headline: Headline
    per_question: dict[str, QuestionMetrics]
    multilabel: MultiLabelMetrics | None  # qs_v2-style per-category binaries
    calibration: dict[str, CalibrationMetrics]
    routing: RoutingMetrics
    slices: list[SliceRow]
    false_forward_value_kinds: dict[str, int]
    failures: list[FailureCase]


class LatencyStats(_Model):
    n: int
    p50_ms: float
    p95_ms: float
    p99_ms: float
    mean_ms: float
    units_per_sec: float


class SpeedMetrics(_Model):
    hardware: str
    batch1: LatencyStats | None
    batched: LatencyStats | None
    per_doc_ms: LatencyStats | None  # wall time per document = sum over its units (batch-1)
    warmup_excluded: int
    # laya autocast per mode: "on", "off", "mixed" (switched mid-run: audit C8) or "unknown"
    batch1_autocast: str = "unknown"
    batched_autocast: str = "unknown"
    # batch-1 calls slower than OUTLIER_X x the median: a sign of outside interference such as
    # memory pressure and swapping (invariant 9)
    batch1_outliers: int = 0
    # batch-1 per-unit latency by state length (units differ in size across and within arms)
    batch1_by_length: dict[str, LatencyStats] = Field(default_factory=lambda: {})
    # median ms/token in the last eighth of the run over the first (> 1: latency drifted up)
    batch1_drift: float | None = None


class RunContext(_Model):
    arm: str
    qs: str
    splits: list[str]
    docs_sha256: str
    units_sha256: str
    decisions_sha256: str
    calib_hash: str
    calib_fit_on: Literal["calib", "fixture_debug"]
    calib_temperature_fallbacks: dict[str, str]
    # D-019: the git commit that froze the calib file, and its commit time
    calib_commit: str
    calib_committed_at: str
    batched_decisions_sha256: str | None = None  # the arm's batched run, for speed only (C6)
    doc_level: bool = False  # doc-level arm (B3, B4): report labels it underpowered (D-008)
    hw: HwInfo | None
    laya_version: str
    checkpoints: list[str]
    checkpoint_revs: list[str]
    created_at: str


class Scores(_Model):
    context: RunContext
    splits: dict[str, SplitScores]
    speed: SpeedMetrics
    caveats: list[str]


# Exported to schema/ and to the HUD.
EXPORTED: tuple[type[BaseModel], ...] = (
    Document,
    Unit,
    QuestionSet,
    Decision,
    RoutedDecision,
    RunMeta,
    CalibParams,
    HwInfo,
    Scores,
    GenManifest,
    Splits,
    LabelManifest,
)
