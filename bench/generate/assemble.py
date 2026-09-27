"""Length buckets and PII-depth placement (docs/specs/generator.md, D-015).

A document is assembled from raw pieces (view + optional hard-negative paragraph + filler sections
+ optional single PII block) that share one DocCtx and are resolved once, so every label comes from
the sentinel pass. Token counts use the multilingual tokenizer (gen_spec `length_tokens`); the
result is checked exactly and adjusted until it lands in its bucket (V4) and, for depth docs, until
the PII block sits in its depth band.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from bench.config import GenSpec
from bench.domain import DocType, Document, Lang, LengthBucket, PiiCategory, PiiDepth, WorldRefs
from bench.generate import filler, negatives
from bench.generate.documents import SPONSOR_SITE, VIEWS, ViewRequest, safe_date
from bench.generate.render import (
    SENTINEL,
    DocCtx,
    Mode,
    Rendered,
    finish,
    insert_at_section,
    render_raw,
)
from bench.generate.seeds import rng
from bench.generate.world import Site, Study, Subject

TokenCounter = Callable[[str], int]

PROSE = frozenset({DocType.PROTOCOL, DocType.NARRATIVE, DocType.MONITORING, DocType.SITE_EMAIL})
# row knob per form type: (tokens per row, estimated; row cap)
ROWS: dict[DocType, tuple[int, int]] = {
    DocType.CRF: (32, 60), DocType.DEVIATION: (30, 60), DocType.CONMED: (26, 40),
    DocType.LAB: (80, 3),
}  # fmt: skip
PII_BLOCK = {  # the single PII paragraph of a depth doc (English: depth docs are long, so English)
    "en": "Note to file: {name} (subject {sid}) attended the visit on {date}; "
    "the source record was reviewed by {staff}.",
}


class AssemblyError(RuntimeError):
    pass


@dataclass(frozen=True)
class DocSpec:
    doc_id: str
    doc_type: DocType
    lang: Lang
    bucket: LengthBucket
    study: Study
    site: Site | None
    subject: Subject | None
    mode: Mode
    enabled: frozenset[PiiCategory]
    hard_negative: bool = False
    headers_footers: bool = False
    pii_depth: PiiDepth | None = None
    extra: dict[str, Any] = field(default_factory=lambda: {})


def _strip(raw: str) -> str:
    return SENTINEL.sub("x", raw)


def assemble(ds: DocSpec, spec: GenSpec, count: TokenCounter, max_rounds: int = 60) -> Document:
    lo, hi = spec.length_tokens[ds.bucket]
    r = rng(spec.seed, "assemble", ds.doc_id)
    margin = max(10, (hi - lo) // 20)
    target = r.randint(lo + margin, hi - margin)
    extra = dict(ds.extra)
    if ds.doc_type in ROWS and ds.bucket is not LengthBucket.SHORT:
        per_row, cap = ROWS[ds.doc_type]
        extra["rows"] = min(cap, max(3, int(0.6 * target / per_row)))

    ctx = DocCtx(lang=ds.lang, rng=r, enabled=ds.enabled,
                 mode="clean" if ds.pii_depth else ds.mode)  # fmt: skip
    req = ViewRequest(
        ds.doc_type, ds.lang, ds.study, ds.site, ds.subject, ctx.mode, ds.enabled, r, extra
    )
    template, data, subjects = VIEWS[ds.doc_type](req, ctx)
    base = render_raw(template, ctx, **data)
    refs = [s for s in (ds.site.subjects if ds.site else []) if s.subject_id in subjects]
    tags: list[str] = ["email_quoting"] if ds.doc_type is DocType.SITE_EMAIL else []
    if ds.headers_footers:
        tags.append("headers_footers")
    if ds.hard_negative:
        base = insert_at_section(base, negatives.block(ctx, ds.study, safe_date(r, refs)), r)
        tags.append("hard_negative")

    pii_block = ""
    if ds.pii_depth:
        if ds.subject is None or ds.site is None:
            raise AssemblyError(f"{ds.doc_id}: depth docs need a site and subject")
        ctx.mode = "normal"
        sub = ds.subject
        pii_block = PII_BLOCK["en"].format(
            name=ctx.name(sub.person, "first_last"), sid=ctx.subject_id(sub, "plain"),
            date=ctx.event_date(sub.visits[1]), staff=ctx.name(ds.site.staff["pi"], "title_last"),
        )  # fmt: skip
        ctx.mode = "clean"
        subjects = sorted({*subjects, sub.subject_id})

    sections: list[str] = []
    topics = list(filler.TOPICS)
    r.shuffle(topics)

    def compose(n_sections: int, depth_at: int | None, paginate: bool = True) -> str:
        raw = base
        for k, sec in enumerate(sections[:n_sections]):
            if ds.doc_type in PROSE:  # fixed position per section, so layouts are stable
                raw = insert_at_section(raw, sec, rng(spec.seed, "filler_at", ds.doc_id, k))
            else:
                raw = raw.rstrip("\n") + "\n\n" + sec
        if pii_block:
            paras = raw.split("\n\n")
            i = min(max(depth_at or 0, 1), len(paras))  # never before the title line
            raw = "\n\n".join([*paras[:i], pii_block, *paras[i:]])
        if ds.headers_footers and paginate:
            raw = _paginate(raw, header)
        return raw

    headers: list[str] = []

    def header(page: int) -> str:
        while len(headers) < page:  # one labeled protocol-number negative per page header
            headers.append(
                f"{spec.world.sponsor} | Protocol {ctx.protocol(ds.study)} | Confidential"
            )
        return headers[page - 1]

    def new_section() -> str:
        t = topics[len(sections) % len(topics)]
        body = "\n\n".join(filler.paragraph(r, t) for _ in range(r.randint(2, 4)))
        return f"{ctx.section(filler.title(r, t))}\n{body}"

    # grow to the target by estimate, then settle on exact counts
    n_sec = 0
    est = count(_strip(base))
    while est < target:
        sections.append(new_section())
        est += count(_strip(sections[-1]))
        n_sec += 1
    depth_at: int | None = None
    for _ in range(max_rounds):
        if pii_block and depth_at is None:
            depth_at = _depth_index(compose(n_sec, None, paginate=False), ds, spec, count)
        out: Rendered = finish(compose(n_sec, depth_at), ctx)
        n = count(out.text)
        if n < lo or n > hi:
            if n < lo:
                if n_sec == len(sections):
                    sections.append(new_section())
                n_sec += 1
            else:
                if n_sec == 0:
                    raise AssemblyError(f"{ds.doc_id}: base document alone is {n} tokens > {hi}")
                n_sec -= 1
            depth_at = None  # layout changed: recompute the depth position
            continue
        if pii_block:
            assert depth_at is not None and ds.pii_depth is not None
            frac = realized_depth_of(out, count)
            lo_f, hi_f = spec.pii_depth_positions[ds.pii_depth]
            if not lo_f <= frac <= hi_f:
                depth_at += 1 if frac < lo_f else -1
                continue
        return Document(
            id=ds.doc_id, doc_type=ds.doc_type, lang=ds.lang, text=out.text,
            spans=sorted(out.spans, key=lambda s: s.start),
            negatives=sorted(out.negatives, key=lambda x: x.start),
            tags=tags + (["pre_redacted"] if ds.mode == "redacted" and any(
                x.kind == "pre_redacted" for x in out.negatives) else []),
            length_bucket=ds.bucket, pii_depth=ds.pii_depth,
            world_refs=WorldRefs(study=ds.study.protocol_no,
                                 site=ds.site.site_no if ds.site else SPONSOR_SITE,
                                 subjects=subjects),
            gen_meta={"template": template, "mode": ds.mode, "sections": out.sections,
                      "tokens_multilingual": n, "target_tokens": target},
        )  # fmt: skip
    raise AssemblyError(f"{ds.doc_id}: could not reach {ds.bucket} ({lo}-{hi}) / depth")


PARAS_PER_PAGE = 12


def _paginate(raw: str, header: Callable[[int], str]) -> str:
    """Repeated page header (with the protocol number) and page footer every PARAS_PER_PAGE
    paragraphs; inserted before resolve so the header negatives are labeled natively."""
    paras = raw.split("\n\n")
    out: list[str] = [header(1)]
    page = 1
    for k, p in enumerate(paras, start=1):
        out.append(p)
        if k % PARAS_PER_PAGE == 0 and k < len(paras):
            page += 1
            out += [f"Page {page - 1}", header(page)]
    out.append(f"Page {page}")
    return "\n\n".join(out)


def _depth_index(raw: str, ds: DocSpec, spec: GenSpec, count: TokenCounter) -> int:
    """Paragraph index whose start falls in the depth band (by cumulative token estimate)."""
    assert ds.pii_depth is not None
    lo_f, hi_f = spec.pii_depth_positions[ds.pii_depth]
    paras = raw.split("\n\n")
    sizes = [count(_strip(p)) for p in paras]
    total = sum(sizes) or 1
    mid = (lo_f + hi_f) / 2
    best, best_gap = 0, 2.0
    acc = 0
    for i, s in enumerate([*sizes, 0]):
        frac = acc / total
        if lo_f <= frac <= hi_f and abs(frac - mid) < best_gap:
            best, best_gap = i, abs(frac - mid)
        acc += s
    if best_gap == 2.0:  # no boundary inside the band: nearest boundary to the middle
        acc = 0
        for i, s in enumerate([*sizes, 0]):
            if abs(acc / total - mid) < best_gap:
                best, best_gap = i, abs(acc / total - mid)
            acc += s
    return best


def realized_depth_of(out: Rendered | Document, count: TokenCounter) -> float:
    """Token fraction before the first PII span."""
    first = min(sp.start for sp in out.spans)
    return count(out.text[:first]) / max(1, count(out.text))
