"""Typed loaders for config/*.yaml. Unknown keys are errors (extra="forbid" everywhere)."""

from __future__ import annotations

import math
from pathlib import Path
from typing import Annotated, Literal, TypeVar

import yaml
from pydantic import BaseModel, ConfigDict, Field, model_validator

from bench.domain import (
    CategoryAnswer,
    DocKindAnswer,
    DocType,
    Lang,
    LengthBucket,
    PiiCategory,
    PiiDepth,
    QuestionSet,
    Split,
    SubjectRole,
)

CONFIG_DIR = Path("config")


class _Cfg(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


def _check_mix(name: str, mix: dict[str, float]) -> None:
    if any(v < 0 for v in mix.values()):
        raise ValueError(f"{name}: negative weight")
    if not math.isclose(sum(mix.values()), 1.0, abs_tol=1e-9):
        raise ValueError(f"{name}: weights sum to {sum(mix.values())}, expected 1")


# --- policy.yaml -------------------------------------------------------------------------------


class Routing(_Cfg):
    recall_target: float = Field(gt=0, le=1)
    precision_target: float = Field(gt=0, le=1)
    patient_role_forces_redact: bool


class Bootstrap(_Cfg):
    resamples: int = Field(ge=1)
    unit: Literal["document"]
    seed: int


class Policy(_Cfg):
    version: int
    coded_id_is_pii: bool  # D-001
    pii_categories: list[PiiCategory]
    category_precedence: list[PiiCategory]
    category_answer_map: dict[PiiCategory, CategoryAnswer]
    role_map: dict[SubjectRole, Literal["patient", "staff", "none"]]
    doc_kind_map: dict[DocType, DocKindAnswer]
    routing: Routing
    bootstrap: Bootstrap

    @model_validator(mode="after")
    def _complete(self) -> Policy:
        if PiiCategory.CODED_ID in self.pii_categories:
            raise ValueError("pii_categories must not list coded_id; set coded_id_is_pii instead")
        if sorted(self.category_precedence) != sorted(PiiCategory):
            raise ValueError("category_precedence must list every PiiCategory exactly once")
        for name, keys in (
            ("category_answer_map", set(self.category_answer_map)),
            ("role_map", set(self.role_map)),
            ("doc_kind_map", set(self.doc_kind_map)),
        ):
            want = {
                "category_answer_map": set(PiiCategory),
                "role_map": set(SubjectRole),
                "doc_kind_map": set(DocType),
            }[name]
            if keys != want:
                raise ValueError(f"{name} missing keys: {sorted(want - keys)}")
        return self

    @property
    def effective_pii_categories(self) -> frozenset[PiiCategory]:
        """Categories that make pii_present = A (coded_id added iff coded_id_is_pii)."""
        cats = set(self.pii_categories)
        if self.coded_id_is_pii:
            cats.add(PiiCategory.CODED_ID)
        return frozenset(cats)


# --- gen_spec.yaml -----------------------------------------------------------------------------


class World(_Cfg):
    sponsor: str
    compound_prefix: str
    studies: int = Field(ge=1)
    sites_per_study: int = Field(ge=1)
    subjects_per_site: int = Field(ge=1)
    site_locales: dict[Lang, int]  # number of sites per language; sums to studies x sites

    @model_validator(mode="after")
    def _sites(self) -> World:
        if sum(self.site_locales.values()) != self.studies * self.sites_per_study:
            raise ValueError("world.site_locales must sum to studies x sites_per_study")
        return self


class Perturbations(_Cfg):
    line_wrap: float = Field(ge=0, le=1)
    ocr_noise: float = Field(ge=0, le=1)
    table: float = Field(ge=0, le=1)
    headers_footers: float = Field(ge=0, le=1)
    email_quoting: Literal["site_correspondence_only"]


class PiiProfile(_Cfg):
    """Probability that a non-clean document of this type contains each category."""

    phi_direct: float = Field(default=0.0, ge=0, le=1)
    phi_quasi: float = Field(default=0.0, ge=0, le=1)
    coded_id: float = Field(default=0.0, ge=0, le=1)
    staff_pii: float = Field(default=0.0, ge=0, le=1)

    @property
    def any(self) -> bool:
        return any(v > 0 for v in (self.phi_direct, self.phi_quasi, self.coded_id, self.staff_pii))

    @property
    def patient(self) -> bool:
        return any(v > 0 for v in (self.phi_direct, self.phi_quasi, self.coded_id))


class DocPlanEntry(_Cfg):
    """How one doc type is generated (D-015)."""

    level: Literal["site", "sponsor"]  # sponsor-level: no site, no subjects, no persons (D-005)
    buckets: list[LengthBucket] = Field(min_length=1)
    langs: list[Lang] = Field(min_length=1)
    clean_rate: float = Field(ge=0, le=1)  # share rendered without any person data
    pii: PiiProfile

    @model_validator(mode="after")
    def _consistent(self) -> DocPlanEntry:
        if self.level == "sponsor" and (self.clean_rate != 1.0 or self.pii.any):
            raise ValueError("sponsor-level doc types carry no person data (clean_rate 1, no pii)")
        if self.clean_rate < 1.0 and not self.pii.any:
            raise ValueError("clean_rate < 1 needs at least one pii category")
        if "en" not in self.langs:
            raise ValueError("every doc type must allow English")
        return self


def largest_remainder(total: int, shares: dict[str, float]) -> dict[str, int]:
    """Integer counts summing to `total`, proportional to `shares` (deterministic tie-break)."""
    raw = {k: total * v for k, v in shares.items()}
    out = {k: int(v) for k, v in raw.items()}
    rest = total - sum(out.values())
    for k in sorted(raw, key=lambda k: (-(raw[k] - out[k]), k))[:rest]:
        out[k] += 1
    return out


class Paraphrase(_Cfg):
    enabled: bool
    model: str | None


class GenSpec(_Cfg):
    seed: int
    world: World
    doc_types: dict[DocType, int]
    lang_counts: dict[Lang, int]  # exact (D-015)
    non_english_buckets: list[LengthBucket]  # non-English docs only in these buckets
    locales: dict[Lang, str]
    length_mix: dict[LengthBucket, float]
    length_tokens: dict[LengthBucket, tuple[int, int]]
    hard_negative_rate: float = Field(ge=0, le=1)
    pii_depth_docs: int = Field(ge=0)
    # PII-bearing docs where some values appear as pre-redaction placeholders (so placeholders are
    # not a "no PII" cue; M4 gold audit N5)
    partial_redaction_docs: int = Field(default=0, ge=0)
    # PII-bearing docs where some values render as neutral alt text instead (so alt phrases are not
    # a "no PII" cue; M4 gold audit R4). Allocated per doc type, disjoint from partial redaction.
    partial_alt_docs: int = Field(default=0, ge=0)
    pii_depth_positions: dict[PiiDepth, tuple[float, float]]
    perturbations: Perturbations
    paraphrase: Paraphrase
    distribution_tolerance_pp: float = Field(gt=0)
    doc_plan: dict[DocType, DocPlanEntry]

    @model_validator(mode="after")
    def _consistent(self) -> GenSpec:
        if set(self.doc_types) != set(DocType):
            raise ValueError("doc_types must give a count for every DocType")
        if any(n < 0 for n in self.doc_types.values()):
            raise ValueError("doc_types counts must be >= 0")
        if any(n < 0 for n in self.lang_counts.values()):
            raise ValueError("lang_counts must be >= 0")
        if sum(self.lang_counts.values()) != self.total_docs:
            raise ValueError(
                f"lang_counts sum to {sum(self.lang_counts.values())}, "
                f"doc_types to {self.total_docs}"
            )
        _check_mix("length_mix", {str(k): v for k, v in self.length_mix.items()})
        if set(self.locales) != set(self.lang_counts):
            raise ValueError("locales and lang_counts must cover the same languages")
        if set(self.length_tokens) != set(LengthBucket) or set(self.length_mix) != set(
            LengthBucket
        ):
            raise ValueError("length_mix and length_tokens must cover every LengthBucket")
        for bucket, (lo, hi) in self.length_tokens.items():
            if not 0 <= lo < hi:
                raise ValueError(f"length_tokens.{bucket}: need 0 <= lo < hi")
        for depth, (lo, hi) in self.pii_depth_positions.items():
            if not 0.0 <= lo < hi <= 1.0:
                raise ValueError(f"pii_depth_positions.{depth}: need 0 <= lo < hi <= 1")
        self._check_plan()
        return self

    def _check_plan(self) -> None:
        """The plan must be able to realize the exact counts (fail at load, not mid-generation)."""
        if set(self.doc_plan) != set(DocType):
            raise ValueError("doc_plan must have an entry for every DocType")
        irb = self.doc_plan[DocType.IRB]
        if irb.pii.patient:
            raise ValueError("irb_letter names no subjects (D-005): no patient categories")
        buckets = self.bucket_counts
        for b, need in buckets.items():
            cap = sum(n for t, n in self.doc_types.items() if b in self.doc_plan[t].buckets)
            if cap < need:
                raise ValueError(f"only {cap} docs may be {b}, {need} needed")
        for lang, need in self.lang_counts.items():
            if lang == "en":
                continue
            cap = sum(
                n for t, n in self.doc_types.items()
                if lang in self.doc_plan[t].langs
                and set(self.doc_plan[t].buckets) & set(self.non_english_buckets)
            )  # fmt: skip
            if cap < need:
                raise ValueError(f"only {cap} docs may be {lang}, {need} needed")
        non_en = sum(n for lang, n in self.lang_counts.items() if lang != "en")
        slots = sum(buckets[b] for b in self.non_english_buckets)
        if non_en > slots:
            raise ValueError(
                f"{non_en} non-English docs don't fit {slots} {self.non_english_buckets} slots"
            )
        depth_cap = sum(
            int(n * (1 - self.doc_plan[t].clean_rate)) for t, n in self.doc_types.items()
            if self.doc_plan[t].level == "site"
            and {LengthBucket.LONG, LengthBucket.XL} & set(self.doc_plan[t].buckets)
        )  # fmt: skip
        if depth_cap < self.pii_depth_docs:
            raise ValueError(
                f"only ~{depth_cap} PII-bearing long docs for {self.pii_depth_docs} depth docs"
            )

    @property
    def bucket_counts(self) -> dict[LengthBucket, int]:
        counts = largest_remainder(self.total_docs, {str(k): v for k, v in self.length_mix.items()})
        return {LengthBucket(k): v for k, v in counts.items()}

    @property
    def hard_negative_count(self) -> int:
        return round(self.total_docs * self.hard_negative_rate)

    @property
    def total_docs(self) -> int:
        return sum(self.doc_types.values())


# --- arms.yaml ---------------------------------------------------------------------------------


class ChunkUnit(_Cfg):
    kind: Literal["chunk"]
    size: int = Field(ge=1)
    overlap: int = Field(ge=0)

    @model_validator(mode="after")
    def _overlap(self) -> ChunkUnit:
        if self.overlap >= self.size:
            raise ValueError("chunk overlap must be smaller than size")
        return self


class SectionUnit(_Cfg):
    kind: Literal["section"]
    target_tokens: int = Field(ge=1)


class DocUnit(_Cfg):
    kind: Literal["doc"]


UnitSpec = Annotated[ChunkUnit | SectionUnit | DocUnit, Field(discriminator="kind")]
Checkpoint = Literal["english", "multilingual", "finetuned_english"]


class Arm(_Cfg):
    checkpoint: Checkpoint
    unit: UnitSpec
    max_len: int = Field(ge=1)  # always explicit (invariant 8)
    head_max_len: int = Field(ge=1)
    enabled: bool = True
    doc_level: bool = False  # few units per doc: reported as underpowered (D-008 amended)

    @model_validator(mode="after")
    def _budget(self) -> Arm:
        if self.head_max_len >= self.max_len:
            raise ValueError("head_max_len must be smaller than max_len")
        return self

    @property
    def state_budget(self) -> int:
        """Tokens available for the unit text (docs/specs/gold-labels.md)."""
        return self.max_len - self.head_max_len


class ArmDefaults(_Cfg):
    warmup_calls: int = Field(ge=0)
    device: Literal["auto", "cuda", "mps", "cpu"]
    splits_to_run: list[Split]
    question_sets: list[str]


class ArmsConfig(_Cfg):
    defaults: ArmDefaults
    arms: dict[str, Arm] = Field(min_length=1)


# --- split.yaml ----------------------------------------------------------------------------------


class SplitConfig(_Cfg):
    """Split design (D-005 amended, D-016, D-018; audit C8: split settings live in config)."""

    seed: int
    ratios: dict[Literal["train", "calib", "test"], float]  # among non-holdout docs
    holdout_doc_type: DocType
    search_iterations: int = Field(ge=1)
    ratio_tolerance: float = Field(gt=0, le=0.5)  # accepted |realized - target| per split (docs)

    @model_validator(mode="after")
    def _ratios(self) -> SplitConfig:
        if set(self.ratios) != {"train", "calib", "test"}:
            raise ValueError("ratios must give train, calib and test")
        _check_mix("ratios", {str(k): v for k, v in self.ratios.items()})
        return self


# --- loaders -----------------------------------------------------------------------------------

_M = TypeVar("_M", bound=BaseModel)


def _load(path: Path, model: type[_M]) -> _M:
    raw = yaml.safe_load(path.read_text())
    if not isinstance(raw, dict):
        raise ValueError(f"{path}: expected a mapping at top level")
    return model.model_validate(raw)


def load_policy(path: Path = CONFIG_DIR / "policy.yaml") -> Policy:
    return _load(path, Policy)


def load_gen_spec(path: Path = CONFIG_DIR / "gen_spec.yaml") -> GenSpec:
    return _load(path, GenSpec)


def load_split(path: Path = CONFIG_DIR / "split.yaml") -> SplitConfig:
    return _load(path, SplitConfig)


def load_arms(path: Path = CONFIG_DIR / "arms.yaml", qs_dir: Path | None = None) -> ArmsConfig:
    arms = _load(path, ArmsConfig)
    qs_dir = qs_dir if qs_dir is not None else path.parent / "questions"
    missing = [q for q in arms.defaults.question_sets if not (qs_dir / f"{q}.yaml").exists()]
    if missing:
        raise ValueError(f"{path}: question sets not found in {qs_dir}: {missing}")
    return arms


def load_question_set(path: Path) -> QuestionSet:
    qs = _load(path, QuestionSet)
    if qs.id != path.stem:
        raise ValueError(f"{path}: id {qs.id!r} does not match file name")
    return qs


def load_question_sets(qs_dir: Path = CONFIG_DIR / "questions") -> dict[str, QuestionSet]:
    return {p.stem: load_question_set(p) for p in sorted(qs_dir.glob("*.yaml"))}
