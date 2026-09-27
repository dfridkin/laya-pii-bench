"""Document views: which world entities a doc type shows, and how a rendered view becomes a
`Document`. Length assembly (4e), negatives injection (4d) and perturbations (4f) wrap this."""

from __future__ import annotations

import random
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Any

from bench.domain import DocType, Document, Lang, LengthBucket, PiiCategory, WorldRefs
from bench.generate import negatives
from bench.generate.render import DocCtx, Mode, Rendered, finish, insert_at_section, render_raw
from bench.generate.world import (
    CONMEDS,
    STUDY_START,
    AdverseEvent,
    LabResult,
    Site,
    Study,
    Subject,
    World,
)

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
    extra: dict[str, Any] = field(default_factory=lambda: {})  # sizing knobs set by assembly (4e)


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


def subject_date_set(subs: list[Subject]) -> set[date]:
    out: set[date] = set()
    for s in subs:
        out |= {s.dob, s.enrolled, *s.visits, *(lab.collected for lab in s.labs)}
        out |= {d.on for d in s.deviations}
        for ae in s.aes:
            out |= {ae.onset} | ({ae.resolved} if ae.resolved else set())
        for cm in s.conmeds:
            out |= {cm.start} | ({cm.stop} if cm.stop else set())
    return out


def safe_date(r: random.Random, subs: list[Subject], lo: date = STUDY_START,
              span_days: int = 420) -> date:  # fmt: skip
    """A document date (not PHI) that shares no rendered form with any referenced subject date:
    `07/08/2025` is July 8 in US order and August 7 in European order, so string forms are
    compared, not calendar dates."""
    from bench.generate.variants import date_forms

    taken = {f for d in subject_date_set(subs) for f in date_forms(d)}
    for _ in range(1000):
        d = lo + timedelta(days=r.randint(0, span_days))
        if not set(date_forms(d)) & taken:
            return d
    raise RuntimeError("no free document date")


def _avoid(req: ViewRequest, subs: list[Subject]) -> list[Subject]:
    """Subjects whose dates document dates must avoid: the view's own plus any the assembler adds
    later (the PII-depth subject), passed as `extra["avoid_dates_of"]`."""
    extra: list[Subject] = list(req.extra.get("avoid_dates_of", []))
    return [*subs, *extra]


def _sae_subject(r: random.Random, site: Site, sub: Subject) -> tuple[Subject, AdverseEvent]:
    """An SAE form reports a real adverse event from the world (no invented events, so the same
    subject's dates agree across SAE form, narrative and logs). If the planned subject has no AE,
    another subject of the same site who has one is reported instead."""
    if not sub.aes:
        with_ae = [s for s in site.subjects if s.aes]
        if not with_ae:
            raise ValueError(f"site {site.key} has no subject with an adverse event")
        sub = with_ae[r.randrange(len(with_ae))]
    serious = [a for a in sub.aes if a.serious]
    return sub, r.choice(serious or sub.aes)


def _sae(req: ViewRequest, ctx: DocCtx) -> tuple[str, dict[str, Any], list[str]]:
    assert req.site is not None and req.subject is not None
    r = req.rng
    sub, ae = _sae_subject(r, req.site, req.subject)
    data = {
        "study": req.study, "site": req.site, "sub": sub, "ae": ae,
        "reporter": req.site.staff[r.choice(["pi", "subi"])],
        # the report follows the onset (and never shares a rendered form with the subject's dates)
        "report_date": safe_date(
            r, _avoid(req, [sub]), lo=ae.onset + timedelta(days=1), span_days=45
        ),
        "ctrl_no": f"FEN-{r.randint(2025000, 2025999)}",
        "followups": list(req.extra.get("followups", [])),
    }  # fmt: skip
    return f"sae_cioms/{req.lang}.j2", data, [sub.subject_id]


def _crf(req: ViewRequest, ctx: DocCtx) -> tuple[str, dict[str, Any], list[str]]:
    assert req.site is not None
    r = req.rng
    n = int(req.extra.get("rows", r.randint(3, 8)))
    rows: list[dict[str, Any]] = []
    for i in range(n):
        sub = req.site.subjects[r.randrange(len(req.site.subjects))]
        v = r.randint(1, len(sub.visits) - 1)
        rows.append({"sub": sub, "visit": f"Visit {v + 1}", "date": sub.visits[v],
                     "sbp": r.randint(105, 165), "dbp": r.randint(62, 98),
                     "hr": r.randint(55, 98), "temp": round(r.uniform(36.1, 37.8), 1),
                     "i": i})  # fmt: skip
    subs = sorted({x["sub"].subject_id for x in rows})
    data = {"study": req.study, "site": req.site, "rows": rows, "page": r.randint(8, 40),
            "entered_by": req.site.staff["coordinator"]}  # fmt: skip
    return "crf_page/en.j2", data, subs


def _lab(req: ViewRequest, ctx: DocCtx) -> tuple[str, dict[str, Any], list[str]]:
    assert req.site is not None and req.subject is not None
    sub = req.subject
    by_date: dict[date, list[LabResult]] = {}
    for lab in sub.labs:
        by_date.setdefault(lab.collected, []).append(lab)
    dates = sorted(by_date)[: int(req.extra.get("rows", 1 + req.rng.randint(0, 1)))]
    visits = [{"date": d, "results": by_date[d]} for d in dates]
    data = {"study": req.study, "site": req.site, "sub": sub, "visits": visits,
            "reviewer": req.site.staff[req.rng.choice(["subi", "pharmacist"])]}  # fmt: skip
    return f"lab_report/{req.lang}.j2", data, [sub.subject_id]


FINDINGS = (
    "a concomitant medication in the clinic notes was missing from the case report form",
    "the source document listed an outdated contact address; the coordinator updated it",
    "a laboratory value was transcribed with the wrong unit and has been queried",
    "the dosing diary was incomplete for two days; the participant was retrained",
    "an adverse event recorded in the notes had not been entered; now entered",
)


def _monitoring(req: ViewRequest, ctx: DocCtx) -> tuple[str, dict[str, Any], list[str]]:
    assert req.site is not None
    r, st = req.rng, req.site.staff
    picks = r.sample(req.site.subjects, r.randint(1, 3))
    findings = [{"sub": s, "text": r.choice(FINDINGS), "date": s.visits[r.randint(1, 4)]
                 if r.random() < 0.7 else None} for s in picks]  # fmt: skip
    data = {"study": req.study, "site": req.site, "cra": st["cra"], "pi": st["pi"],
            "coordinator": st["coordinator"], "visit_no": r.randint(2, 9), "findings": findings,
            "paragraphs": list(req.extra.get("paragraphs", []))}  # fmt: skip
    return "monitoring_visit_report/en.j2", data, sorted(s.subject_id for s in picks)


def _deviation(req: ViewRequest, ctx: DocCtx) -> tuple[str, dict[str, Any], list[str]]:
    assert req.site is not None
    r, site = req.rng, req.site
    rows: list[dict[str, Any]] = []
    for sub in site.subjects:
        rows += [{"sub": sub, "date": d.on, "text": d.description} for d in sub.deviations]
    n = int(req.extra.get("rows", r.randint(3, 8)))
    while len(rows) < n:
        sub = r.choice(site.subjects)
        rows.append({"sub": sub, "date": sub.visits[r.randint(1, 4)],
                     "text": "visit performed outside the protocol window"})  # fmt: skip
    rows = sorted(rows[:n], key=lambda x: (x["date"], x["sub"].subject_id))
    for x in rows:
        x["category"] = r.choice(["minor", "minor", "major"])
        x["reporter"] = site.staff[r.choice(["coordinator", "pi"])]
    data = {"study": req.study, "site": site, "rows": rows}
    return "deviation_log/en.j2", data, sorted({x["sub"].subject_id for x in rows})


INDICATIONS_CM = ("pain", "hypertension", "type 2 diabetes", "hyperlipidaemia", "reflux",
                  "infection", "hypothyroidism")  # fmt: skip


def _conmed(req: ViewRequest, ctx: DocCtx) -> tuple[str, dict[str, Any], list[str]]:
    assert req.site is not None and req.subject is not None
    r, sub = req.rng, req.subject
    rows = [{"drug": c.drug, "dose": c.dose, "start": c.start, "stop": c.stop,
             "indication": r.choice(INDICATIONS_CM)} for c in sub.conmeds]  # fmt: skip
    n = int(req.extra.get("rows", max(2, len(rows))))
    while len(rows) < n:
        drug, dose = r.choice(CONMEDS)
        start = sub.visits[r.randint(0, 3)]
        rows.append({"drug": drug, "dose": dose, "start": start, "stop": None,
                     "indication": r.choice(INDICATIONS_CM)})  # fmt: skip
    data = {"study": req.study, "site": req.site, "sub": sub, "rows": rows[:n],
            "reviewer": req.site.staff[r.choice(["coordinator", "subi"])]}  # fmt: skip
    return "conmed_log/en.j2", data, [sub.subject_id]


TASKS = ("1-6", "2, 3, 6", "3, 4, 6", "5", "1, 2", "3, 6")


def _delegation(req: ViewRequest, ctx: DocCtx) -> tuple[str, dict[str, Any], list[str]]:
    assert req.site is not None
    r, st = req.rng, req.site.staff
    rows = [
        {"person": st[j], "tasks": r.choice(TASKS)}
        for j in ("pi", "subi", "coordinator", "pharmacist")
    ]
    data = {"study": req.study, "site": req.site, "staff_rows": rows,
            "history": list(req.extra.get("history", []))}  # fmt: skip
    return "delegation_log/en.j2", data, []


TOPICS = ("open data queries", "monitoring visit follow-up", "drug shipment receipt",
          "conmed page query", "visit window question")  # fmt: skip
BODY = ("I resolved the open queries and updated the eCRF this morning.",
        "The shipment arrived intact and the temperature log shows no excursions.",
        "Please find the corrected pages attached for your review.",
        "The investigator has signed the updated delegation log.")  # fmt: skip
ASK = ("could you check the open queries before Friday?", "is the visit window still +/- 2 days?",
       "please confirm the corrected pages have been filed.")  # fmt: skip


def _correspondence(req: ViewRequest, ctx: DocCtx) -> tuple[str, dict[str, Any], list[str]]:
    assert req.site is not None
    r, st = req.rng, req.site.staff
    subs = r.sample(req.site.subjects, r.choice((0, 1, 1, 2)))
    data = {
        "study": req.study, "site": req.site, "a": st[r.choice(["coordinator", "pi"])],
        "b": st[r.choice(["cra", "sponsor_contact"])], "subs": subs, "topic": r.choice(TOPICS),
        "body_lines": [*r.sample(BODY, 2), *req.extra.get("body", [])],
        "ask_lines": r.sample(ASK, 1),
        "sent": safe_date(
            r, _avoid(req, subs), span_days=40,
            lo=max((x.visits[1] for x in subs), default=STUDY_START) + timedelta(days=1),
        ),
    }  # fmt: skip
    return f"site_correspondence/{req.lang}.j2", data, sorted(s.subject_id for s in subs)


def _icf(req: ViewRequest, ctx: DocCtx) -> tuple[str, dict[str, Any], list[str]]:
    assert req.site is not None and req.subject is not None
    sub = req.subject
    data = {
        "study": req.study,
        "sub": sub,
        "investigator": req.site.staff[req.rng.choice(["pi", "subi"])],
        "version_date": safe_date(
            req.rng, _avoid(req, [sub]), lo=sub.enrolled - timedelta(days=150), span_days=140
        ),  # version dated before the signature
    }
    return f"icf_signature_page/{req.lang}.j2", data, [sub.subject_id]


CONDITIONS = (
    "Use only the approved version of the informed consent form.",
    "Report serious adverse events to the Board within 7 days of awareness.",
    "Submit a progress report at least 30 days before the approval expires.",
    "Any change to the approved research requires prior Board review.",
)


def _irb(req: ViewRequest, ctx: DocCtx) -> tuple[str, dict[str, Any], list[str]]:
    assert req.site is not None
    r, st = req.rng, req.site.staff
    data = {
        "study": req.study,
        "site": req.site,
        "chair": st["irb_chair"],
        "admin": st["irb_admin"],
        "pi": st["pi"],
        "meeting": safe_date(r, _avoid(req, [])),
        "amendment": f"A{r.randint(1, 6)}",
        "conditions": [*r.sample(CONDITIONS, 3), *req.extra.get("conditions", [])],
    }
    return "irb_letter/en.j2", data, []


VIEWS: dict[DocType, View] = {
    DocType.NARRATIVE: _narrative,
    DocType.PROTOCOL: _protocol,
    DocType.SAE: _sae,
    DocType.CRF: _crf,
    DocType.LAB: _lab,
    DocType.MONITORING: _monitoring,
    DocType.DEVIATION: _deviation,
    DocType.CONMED: _conmed,
    DocType.DELEGATION: _delegation,
    DocType.SITE_EMAIL: _correspondence,
    DocType.ICF: _icf,
    DocType.IRB: _irb,
}
SUBJECT_TYPES = frozenset(
    {DocType.NARRATIVE, DocType.SAE, DocType.LAB, DocType.CONMED, DocType.ICF}
)


def build(doc_id: str, req: ViewRequest) -> Document:
    """Render the view; when `req.extra["hard_negative"]` is set, splice in a hard-negative
    paragraph (4d) before resolving, and tag the document."""
    ctx = DocCtx(lang=req.lang, rng=req.rng, enabled=req.enabled, mode=req.mode)
    template, data, subjects = VIEWS[req.doc_type](req, ctx)
    raw = render_raw(template, ctx, **data)
    tags: list[str] = []
    if req.extra.get("hard_negative"):
        refs = [s for s in (req.site.subjects if req.site else []) if s.subject_id in subjects]
        para = negatives.block(ctx, req.study, safe_date(req.rng, refs))
        raw = insert_at_section(raw, para, req.rng)
        tags.append("hard_negative")
    out: Rendered = finish(raw, ctx)
    if req.mode == "redacted" and any(n.kind == "pre_redacted" for n in out.negatives):
        tags.append("pre_redacted")
    return Document(
        id=doc_id,
        doc_type=req.doc_type,
        lang=req.lang,
        text=out.text,
        spans=sorted(out.spans, key=lambda s: s.start),
        negatives=sorted(out.negatives, key=lambda n: n.start),
        tags=tags,
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
