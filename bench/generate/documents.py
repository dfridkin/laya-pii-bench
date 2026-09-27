"""Document views: which world entities a doc type shows, and how a rendered view becomes a
`Document`. Length assembly (4e), negatives injection (4d) and perturbations (4f) wrap this."""

from __future__ import annotations

import random
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from bench.domain import DocType, Document, Lang, LengthBucket, PiiCategory, WorldRefs
from bench.generate.render import DocCtx, Mode, Rendered, render
from bench.generate.world import Site, Study, Subject, World

SPONSOR_SITE = "SPONSOR"


@dataclass(frozen=True)
class ViewRequest:
    doc_type: DocType
    lang: Lang
    study: Study
    site: Site | None  # None for sponsor-level docs
    subject: Subject | None
    mode: Mode
    enabled: frozenset[PiiCategory]
    rng: random.Random


View = Callable[[ViewRequest, DocCtx], tuple[str, dict[str, Any], list[str]]]
"""Returns (template name, template data, referenced subject ids)."""


def _narrative(req: ViewRequest, ctx: DocCtx) -> tuple[str, dict[str, Any], list[str]]:
    assert req.site is not None and req.subject is not None
    sub = req.subject
    ae = req.rng.choice(sub.aes) if sub.aes else None
    data = {"study": req.study, "site": req.site, "sub": sub, "pi": req.site.staff["pi"], "ae": ae}
    return f"csr_patient_narrative/{req.lang}.j2", data, [sub.subject_id]


def _protocol(req: ViewRequest, ctx: DocCtx) -> tuple[str, dict[str, Any], list[str]]:
    part = req.rng.choice(["eligibility", "statistics", "treatment"])
    return "protocol_section/en.j2", {"study": req.study, "part": part}, []


VIEWS: dict[DocType, View] = {
    DocType.NARRATIVE: _narrative,
    DocType.PROTOCOL: _protocol,
}


def build(doc_id: str, req: ViewRequest) -> Document:
    ctx = DocCtx(lang=req.lang, rng=req.rng, enabled=req.enabled, mode=req.mode)
    template, data, subjects = VIEWS[req.doc_type](req, ctx)
    out: Rendered = render(template, ctx, **data)
    return Document(
        id=doc_id,
        doc_type=req.doc_type,
        lang=req.lang,
        text=out.text,
        spans=sorted(out.spans, key=lambda s: s.start),
        negatives=sorted(out.negatives, key=lambda n: n.start),
        tags=["pre_redacted"] if req.mode == "redacted" and out.negatives else [],
        length_bucket=LengthBucket.SHORT,  # set by assembly (4e)
        pii_depth=None,
        world_refs=WorldRefs(
            study=req.study.protocol_no,
            site=req.site.site_no if req.site else SPONSOR_SITE,
            subjects=subjects,
        ),
        gen_meta={"template": template, "mode": req.mode, "sections": out.sections},
    )


def world_subject(world: World, subject_id: str) -> Subject:
    return next(s for site in world.sites() for s in site.subjects if s.subject_id == subject_id)
