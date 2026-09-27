"""Full generation (4g): plan exact counts, assemble, perturb, validate, write docs + manifest.

Every allocation is deterministic (seeded shuffles of sorted candidates) and exact where
gen_spec gives counts; rates are converted to exact counts too, so realized distributions match by
construction and V5 verifies it.
"""

from __future__ import annotations

import hashlib
import random
from collections import Counter, defaultdict
from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path

from bench.config import GenSpec, Policy
from bench.domain import (
    DocType,
    Document,
    GenManifest,
    Lang,
    LengthBucket,
    PiiCategory,
    PiiDepth,
    ValidatorResult,
)
from bench.generate import checks, perturb
from bench.generate import world as W
from bench.generate.assemble import PROSE, DocSpec, assemble, realized_depth_of
from bench.generate.documents import SUBJECT_TYPES
from bench.generate.render import Mode, template_vocabulary
from bench.generate.seeds import rng

TokenCounter = Callable[[str], int]
TABLE_TYPES = frozenset(
    {DocType.CRF, DocType.LAB, DocType.DEVIATION, DocType.CONMED, DocType.DELEGATION}
)
REDACTED_TYPES = frozenset({DocType.NARRATIVE, DocType.SAE})  # their clean share is pre-redacted
WRAP_WIDTH = 78


class GenError(RuntimeError):
    pass


@dataclass
class Slot:
    """Mutable plan row, frozen into a DocSpec once complete."""

    idx: int
    doc_type: DocType
    site: W.Site | None = None
    lang: Lang = "en"
    bucket: LengthBucket | None = None
    mode: Mode = "normal"
    depth: PiiDepth | None = None
    enabled: frozenset[PiiCategory] = frozenset()
    subject: W.Subject | None = None
    hard_negative: bool = False
    headers_footers: bool = False
    partial_redact: bool = False
    post: list[str] = field(
        default_factory=lambda: []
    )  # "table:tab|fixed", "line_wrap", "ocr_noise"


def _take(r: random.Random, pool: Sequence[Slot], n: int, what: str) -> list[Slot]:
    if n > len(pool):
        raise GenError(f"need {n} docs for {what}, only {len(pool)} eligible")
    ordered = sorted(pool, key=lambda s: s.idx)
    r.shuffle(ordered)
    return ordered[:n]


def _may_be(spec: GenSpec, t: DocType, lang: str) -> bool:
    entry = spec.doc_plan[t]
    return lang in entry.langs and bool(set(entry.buckets) & set(spec.non_english_buckets))


def plan(spec: GenSpec, world: W.World) -> list[Slot]:
    seed = spec.seed
    slots: list[Slot] = []
    for t in sorted(spec.doc_types, key=lambda t: t.value):
        slots += [Slot(0, t) for _ in range(spec.doc_types[t])]
    rng(seed, "order").shuffle(slots)
    for i, s in enumerate(slots):
        s.idx = i

    # sites: round-robin per type over a shuffled site list (balanced for the site-grouped split)
    sites = world.sites()
    for t in sorted(spec.doc_types, key=lambda t: t.value):
        if spec.doc_plan[t].level == "sponsor":
            continue
        order = list(sites)
        rng(seed, "sites", t.value).shuffle(order)
        for k, s in enumerate(x for x in slots if x.doc_type is t):
            s.site = order[k % len(order)]

    # languages: non-English docs come from sites of that locale and site-facing types
    other: tuple[Lang, ...] = ("de", "es", "pl")
    for lang in other:
        n = spec.lang_counts.get(lang, 0)
        pool = [
            s for s in slots
            if s.site and s.site.lang == lang and s.lang == "en" and _may_be(spec, s.doc_type, lang)
        ]  # fmt: skip
        for s in _take(rng(seed, "lang", lang), pool, n, f"lang {lang}"):
            s.lang = lang

    # buckets: constrained docs first (non-English, short-only types), long/xl from English prose
    counts = dict(spec.bucket_counts)
    for s in slots:
        allowed = spec.doc_plan[s.doc_type].buckets
        if s.lang != "en":
            allowed = [b for b in allowed if b in spec.non_english_buckets]
        if len(allowed) == 1:
            s.bucket = allowed[0]
            counts[allowed[0]] -= 1
    for b in (LengthBucket.XL, LengthBucket.LONG, LengthBucket.MEDIUM, LengthBucket.SHORT):
        pool = [s for s in slots if s.bucket is None and b in spec.doc_plan[s.doc_type].buckets
                and (s.lang == "en" or b in spec.non_english_buckets)]  # fmt: skip
        if counts[b] < 0:
            raise GenError(f"bucket {b}: constrained docs exceed its count")
        for s in _take(rng(seed, "bucket", b.value), pool, counts[b], f"bucket {b}"):
            s.bucket = b
    if any(s.bucket is None for s in slots):
        raise GenError("bucket allocation left documents unassigned")

    # modes: exact clean share per type (pre-redacted for narratives/SAE)
    for t in sorted(spec.doc_types, key=lambda t: t.value):
        entry = spec.doc_plan[t]
        of_type = [s for s in slots if s.doc_type is t]
        n_clean = round(len(of_type) * entry.clean_rate)
        for s in _take(rng(seed, "clean", t.value), of_type, n_clean, f"clean {t}"):
            s.mode = "redacted" if t in REDACTED_TYPES else "clean"

    # PII depth: English, site-level long/xl prose docs with PII
    long_ = (LengthBucket.LONG, LengthBucket.XL)
    depth_pool = [
        s for s in slots
        if s.doc_type in PROSE and s.site is not None and s.lang == "en" and s.mode == "normal"
        and s.bucket in long_
    ]  # fmt: skip
    chosen = _take(rng(seed, "depth"), depth_pool, spec.pii_depth_docs, "pii depth")
    depths = sorted(spec.pii_depth_positions)
    for k, s in enumerate(chosen):
        s.depth = depths[k % len(depths)]

    # categories and subjects
    for s in slots:
        entry = spec.doc_plan[s.doc_type]
        r = rng(seed, "cats", s.idx)
        if s.mode == "normal" and entry.pii.any:
            probs = {c: getattr(entry.pii, c.value) for c in PiiCategory}
            chosen_cats = {c for c, p in probs.items() if p > 0 and r.random() < p}
            s.enabled = frozenset(chosen_cats or {max(probs, key=lambda c: (probs[c], c.value))})
        if s.site is not None and (s.doc_type in SUBJECT_TYPES or s.depth):
            s.subject = s.site.subjects[r.randrange(len(s.site.subjects))]

    # partial redaction: PII-bearing site docs (not depth docs, whose single block must stay PII)
    partial_pool = [s for s in slots if s.site is not None and s.mode == "normal" and s.enabled
                    and s.depth is None]  # fmt: skip
    for s in _take(
        rng(seed, "partial"), partial_pool, spec.partial_redaction_docs, "partial redaction"
    ):
        s.partial_redact = True

    # hard negatives, headers/footers, post-resolve perturbations: exact counts
    total = len(slots)
    for s in _take(rng(seed, "hardneg"), slots, spec.hard_negative_count, "hard negatives"):
        s.hard_negative = True
    p = spec.perturbations
    for s in _take(rng(seed, "hf"), slots, round(total * p.headers_footers), "headers/footers"):
        s.headers_footers = True
    tables = _take(rng(seed, "table"), [s for s in slots if s.doc_type in TABLE_TYPES],
                   round(total * p.table), "table")  # fmt: skip
    for k, s in enumerate(tables):
        s.post.append("table:tab" if k % 2 == 0 else "table:fixed")
    for s in _take(rng(seed, "wrap"), slots, round(total * p.line_wrap), "line wrap"):
        s.post.append("line_wrap")
    for s in _take(rng(seed, "ocr"), slots, round(total * p.ocr_noise), "ocr noise"):
        s.post.append("ocr_noise")
    return slots


def doc_spec(s: Slot, world: W.World) -> DocSpec:
    site = s.site
    study = world.study_of(site) if site else world.studies[s.idx % len(world.studies)]
    assert s.bucket is not None
    return DocSpec(
        doc_id=f"d{s.idx:04d}", doc_type=s.doc_type, lang=s.lang, bucket=s.bucket, study=study,
        site=site, subject=s.subject, mode=s.mode, enabled=s.enabled,
        hard_negative=s.hard_negative, headers_footers=s.headers_footers, pii_depth=s.depth,
        partial_redact=s.partial_redact,
    )  # fmt: skip


def post_process(doc: Document, s: Slot, seed: int) -> Document:
    """Character-level perturbations after resolve (span remap)."""
    for step in s.post:
        if step.startswith("table:"):
            doc = perturb.apply(doc, perturb.table_style(doc, step.split(":")[1]), "table")
        elif step == "line_wrap":
            doc = perturb.apply(doc, perturb.line_wrap(doc, WRAP_WIDTH), "line_wrap")
        elif step == "ocr_noise":
            doc = perturb.apply(
                doc, perturb.ocr_noise(doc, rng(seed, "ocr", doc.id), 0.01), "ocr_noise"
            )
    return doc


@dataclass
class Result:
    docs: list[Document]
    problems: dict[str, list[str]]  # doc id -> problems


def generate(spec: GenSpec, policy: Policy, count: TokenCounter,
             only: Sequence[int] | None = None) -> Result:  # fmt: skip
    world = W.build(spec, frozenset(template_vocabulary()))
    scanner = checks.Scanner(world)
    slots = plan(spec, world)
    docs: list[Document] = []
    problems: dict[str, list[str]] = defaultdict(list)
    for s in slots if only is None else [slots[i] for i in only]:
        ds = doc_spec(s, world)
        try:
            doc = assemble(ds, spec, count, post=lambda d, s=s: post_process(d, s, spec.seed))
        except Exception as e:
            problems[ds.doc_id].append(f"ASSEMBLY {type(e).__name__}: {e}")
            continue
        found = checks.check(doc, policy, scanner)
        n = count(doc.text)
        lo, hi = spec.length_tokens[doc.length_bucket]
        if not lo <= n <= hi:
            found.append(f"V4 {n} tokens outside {doc.length_bucket} [{lo}, {hi}]")
        if doc.pii_depth is not None:
            f_lo, f_hi = spec.pii_depth_positions[doc.pii_depth]
            if not f_lo <= realized_depth_of(doc, count) <= f_hi:
                found.append(
                    f"V4 pii depth {realized_depth_of(doc, count):.3f} outside {doc.pii_depth}"
                )
        doc = replace_meta(doc, n)
        if found:
            problems[doc.id] += found
        docs.append(doc)
    return Result(sorted(docs, key=lambda d: d.id), dict(problems))


def replace_meta(doc: Document, tokens: int) -> Document:
    meta = dict(doc.gen_meta) | {"tokens_multilingual": tokens}
    return doc.model_copy(update={"gen_meta": meta})


def distributions(docs: Sequence[Document]) -> tuple[dict[str, dict[str, int]], dict[str, float]]:
    counts = {
        "doc_type": Counter(d.doc_type.value for d in docs),
        "lang": Counter(d.lang for d in docs),
        "length_bucket": Counter(d.length_bucket.value for d in docs),
        "pii_depth": Counter(d.pii_depth.value for d in docs if d.pii_depth),
        "mode": Counter(str(d.gen_meta.get("mode")) for d in docs),
    }
    tags = Counter(t for d in docs for t in d.tags)
    rates = {t: tags[t] / len(docs) for t in sorted(tags)} if docs else {}
    return {k: dict(sorted(v.items())) for k, v in counts.items()}, rates


def v5(spec: GenSpec, docs: Sequence[Document]) -> list[str]:
    counts, rates = distributions(docs)
    out: list[str] = []
    want: dict[str, dict[str, int]] = {
        "doc_type": {t.value: n for t, n in spec.doc_types.items()},
        "lang": {str(k): v for k, v in spec.lang_counts.items()},
        "length_bucket": {b.value: n for b, n in spec.bucket_counts.items()},
    }
    for dim, exp in want.items():
        got = counts[dim]
        for k, n in exp.items():
            if got.get(k, 0) != n:
                out.append(f"V5 {dim}={k}: {got.get(k, 0)} docs, spec says {n}")
    tol = spec.distribution_tolerance_pp / 100
    p = spec.perturbations
    for tag, target in (("hard_negative", spec.hard_negative_rate), ("line_wrap", p.line_wrap),
                        ("ocr_noise", p.ocr_noise), ("table", p.table),
                        ("headers_footers", p.headers_footers)):  # fmt: skip
        if abs(rates.get(tag, 0.0) - target) > tol:
            out.append(f"V5 rate {tag}: {rates.get(tag, 0.0):.3f} vs {target:.3f} (+/-{tol:.2f})")
    n_email = sum(d.doc_type is DocType.SITE_EMAIL for d in docs)
    if sum("email_quoting" in d.tags for d in docs) != n_email:
        out.append("V5 email_quoting must be on every site_correspondence doc")
    if sum(d.gen_meta.get("partial_redact") == 1 for d in docs) != spec.partial_redaction_docs:
        out.append("V5 partial_redaction docs count")
    if len([d for d in docs if d.pii_depth]) != spec.pii_depth_docs:
        out.append("V5 pii_depth docs count")
    return out


def serialize(docs: Sequence[Document]) -> str:
    return "".join(d.model_dump_json() + "\n" for d in docs)


def write(result: Result, spec: GenSpec, spec_path: Path, out: Path,
          rerun_sha256: str | None = None) -> GenManifest:  # fmt: skip
    """`rerun_sha256`: hash of an independent second generation (V6); None skips V6."""
    out.parent.mkdir(parents=True, exist_ok=True)
    body = serialize(result.docs)
    out.write_text(body, encoding="utf-8")
    sha = hashlib.sha256(body.encode()).hexdigest()
    counts, rates = distributions(result.docs)
    per_v: dict[str, list[str]] = defaultdict(list)
    for doc_id, ps in sorted(result.problems.items()):
        for p in ps:
            per_v[p.split(" ", 1)[0]].append(f"{doc_id}: {p}")
    per_v["V5"] += v5(spec, result.docs)
    if rerun_sha256 is not None and rerun_sha256 != sha:
        per_v["V6"].append(f"second generation sha256 {rerun_sha256[:16]} != {sha[:16]}")
    validators = [
        ValidatorResult(
            name=v,
            passed=not per_v.get(v),
            failures=len(per_v.get(v, [])),
            detail=per_v.get(v, [])[:20],
        )
        for v in ("ASSEMBLY", "V1", "V2", "V3", "V4", "V5", *(["V6"] if rerun_sha256 else []))
    ]
    manifest = GenManifest(
        seed=spec.seed, n_docs=len(result.docs), sha256=sha,
        gen_spec_sha256=hashlib.sha256(spec_path.read_bytes()).hexdigest(),
        counts=counts, rates=rates, validators=validators,
        created_at=datetime.now(UTC).isoformat(timespec="seconds"),
    )  # fmt: skip
    (out.parent / "gen_manifest.json").write_text(manifest.model_dump_json(indent=2) + "\n")
    return manifest
