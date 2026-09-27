"""Sentinel renderer (docs/specs/generator.md, D-009, invariant 1).

Templates never write PII directly. Helpers (`name`, `dob`, `subject_id`, ...) choose a surface
variant and, if the document's PII profile enables the category, emit it through `pii()`, which
records a slot and returns `⟦sN⟧`. `neg()` does the same for hard negatives (`⟦nN⟧`), and
`section()` marks a section header (`⟦hN⟧`). One left-to-right pass then replaces sentinels and
records offsets. Nothing is ever located by searching the rendered text.
"""

from __future__ import annotations

import random
import re
from collections.abc import Iterable
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Literal

import jinja2

from bench.domain import Negative, PiiCategory, Span, SubjectRole
from bench.generate import variants as V
from bench.generate.world import Person, Study, Subject

TEMPLATES = Path(__file__).parent / "templates"
SENTINEL = re.compile(r"⟦([snh])(\d+)⟧")
Mode = Literal["normal", "clean", "redacted"]

REDACTIONS = ("[REDACTED]", "XX-XXXX", "***")
AE_TERMS_I18N: dict[str, dict[str, str]] = {  # audit J6: no English clinical terms in de/es/pl docs
    "de": {"headache": "Kopfschmerzen", "nausea": "Übelkeit", "fatigue": "Erschöpfung",
           "neutropenia": "Neutropenie", "rash": "Hautausschlag", "diarrhoea": "Diarrhö",
           "dizziness": "Schwindel", "pneumonia": "Pneumonie", "elevated ALT": "erhöhte ALT",
           "hypertension": "Hypertonie", "arthralgia": "Arthralgie", "insomnia": "Schlaflosigkeit"},
    "es": {"headache": "cefalea", "nausea": "náuseas", "fatigue": "fatiga",
           "neutropenia": "neutropenia", "rash": "exantema", "diarrhoea": "diarrea",
           "dizziness": "mareo", "pneumonia": "neumonía", "elevated ALT": "ALT elevada",
           "hypertension": "hipertensión", "arthralgia": "artralgia", "insomnia": "insomnio"},
    "pl": {"headache": "ból głowy", "nausea": "nudności", "fatigue": "zmęczenie",
           "neutropenia": "neutropenia", "rash": "wysypka", "diarrhoea": "biegunka",
           "dizziness": "zawroty głowy", "pneumonia": "zapalenie płuc",
           "elevated ALT": "podwyższona ALT", "hypertension": "nadciśnienie",
           "arthralgia": "bóle stawów", "insomnia": "bezsenność"},
}  # fmt: skip
ALT = {  # neutral text when a category is off (clean docs, or category not sampled)
    "en": {"patient": "the participant", "staff": "the investigator", "sponsor": "the sponsor"},
    "de": {"patient": "der Teilnehmer", "staff": "der Prüfarzt", "sponsor": "der Sponsor"},
    "es": {"patient": "el participante", "staff": "el investigador", "sponsor": "el promotor"},
    "pl": {"patient": "uczestnik", "staff": "badacz", "sponsor": "sponsor"},
}


class RenderError(ValueError):
    pass


@dataclass
class Slot:
    value: str
    meta: dict[str, str]


@dataclass
class Rendered:
    text: str
    spans: list[Span]
    negatives: list[Negative]
    sections: list[int]


def resolve(raw: str, slots: list[Slot], negs: list[Slot], heads: list[str]) -> Rendered:
    """Replace sentinels left to right, recording offsets as values are emitted."""
    out: list[str] = []
    spans: list[Span] = []
    negatives: list[Negative] = []
    sections: list[int] = []
    pos = last = 0
    for m in SENTINEL.finditer(raw):
        lit = raw[last : m.start()]
        out.append(lit)
        pos += len(lit)
        kind, idx = m.group(1), int(m.group(2))
        if kind == "h":
            value = heads[idx]
            sections.append(pos)
        else:
            slot = (slots if kind == "s" else negs)[idx]
            value = slot.value
            rec = {"start": pos, "end": pos + len(value), "value": value, **slot.meta}
            if kind == "s":
                spans.append(Span.model_validate(rec))
            else:
                negatives.append(Negative.model_validate(rec))
        out.append(value)
        pos += len(value)
        last = m.end()
    out.append(raw[last:])
    text = "".join(out)
    if "⟦" in text or "⟧" in text:
        raise RenderError("unresolved sentinel in rendered text")
    return Rendered(text, spans, negatives, sections)


@dataclass
class DocCtx:
    """Per-document helpers exposed to templates."""

    lang: str
    rng: random.Random
    enabled: frozenset[PiiCategory]
    mode: Mode = "normal"
    # share of enabled PII values rendered as pre-redaction placeholders instead (audit N5: the
    # placeholders must not only occur in PII-free documents)
    partial_redact: float = 0.0
    _redact_next: bool = False
    slots: list[Slot] = field(default_factory=lambda: [])
    negs: list[Slot] = field(default_factory=lambda: [])
    heads: list[str] = field(default_factory=lambda: [])

    # --- primitives -------------------------------------------------------------------------

    def pii(self, value: str, category: str, role: str, value_kind: str, surface: str) -> str:
        if not value or "⟦" in value:
            raise RenderError(f"bad pii value {value!r}")
        self.slots.append(Slot(value, {"category": category, "role": role,
                                       "value_kind": value_kind, "surface": surface}))  # fmt: skip
        return f"⟦s{len(self.slots) - 1}⟧"

    def neg(self, value: str, kind: str) -> str:
        if not value or "⟦" in value:
            raise RenderError(f"bad negative value {value!r}")
        self.negs.append(Slot(value, {"kind": kind}))
        return f"⟦n{len(self.negs) - 1}⟧"

    def section(self, title: str) -> str:
        self.heads.append(title)
        return f"⟦h{len(self.heads) - 1}⟧"

    def tr(self, term: str) -> str:
        """Clinical term in the document's language."""
        return AE_TERMS_I18N.get(self.lang, {}).get(term, term)

    def pick(self, options: Iterable[str]) -> str:
        return self.rng.choice(sorted(options))

    # --- gating -----------------------------------------------------------------------------

    def _on(self, category: PiiCategory) -> bool:
        if self.mode != "normal" or category not in self.enabled:
            return False
        if self.partial_redact and self.rng.random() < self.partial_redact:
            self._redact_next = True
            return False
        return True

    def _off(self, role: str, alt: str | None) -> str:
        if self.mode == "redacted" or self._redact_next:
            self._redact_next = False
            return self.neg(self.pick(REDACTIONS), "pre_redacted")
        return alt if alt is not None else ALT[self.lang]["staff" if role == "sponsor" else role]

    @staticmethod
    def _cat(p: Person, patient_cat: PiiCategory) -> tuple[PiiCategory, str]:
        if p.role is SubjectRole.PATIENT:
            return patient_cat, "patient"
        return PiiCategory.STAFF_PII, p.role.value

    # --- person helpers ---------------------------------------------------------------------

    def name(self, p: Person, surface: str | None = None, alt: str | None = None) -> str:
        cat, role = self._cat(p, PiiCategory.PHI_DIRECT)
        if not self._on(cat):
            return self._off(role, alt)
        s = surface or self.pick(("first_last", "last_first_upper", "initial_last", "title_last"))
        return self.pii(V.name(p, s), cat, role, "person_name", s)

    def initials(self, p: Person, surface: str | None = None, alt: str | None = None) -> str:
        cat, role = self._cat(p, PiiCategory.PHI_QUASI)
        if not self._on(cat):
            return self._off(role, alt)
        s = surface or self.pick(V.INITIALS_SURFACES)
        return self.pii(V.initials(p, s), cat, role, "initials", s)

    def email(self, p: Person, alt: str | None = None) -> str:
        cat, role = self._cat(p, PiiCategory.PHI_DIRECT)
        if p.email is None or not self._on(cat):
            return self._off(role, alt if alt is not None else "")
        return self.pii(p.email, cat, role, "email", "institutional")

    def phone(self, p: Person, alt: str | None = None) -> str:
        cat, role = self._cat(p, PiiCategory.PHI_DIRECT)
        if p.phone is None or not self._on(cat):
            return self._off(role, alt if alt is not None else "")
        return self.pii(p.phone, cat, role, "phone", "local")

    # --- subject helpers --------------------------------------------------------------------

    def subject_id(self, sub: Subject, surface: str | None = None, alt: str | None = None) -> str:
        if not self._on(PiiCategory.CODED_ID):
            return self._off("patient", alt)
        s = surface or self.pick(V.SUBJECT_ID_SURFACES)
        return self.pii(V.subject_id(sub.subject_id, s), PiiCategory.CODED_ID, "patient",
                        "subject_id", s)  # fmt: skip

    def rand_no(self, sub: Subject, alt: str | None = None) -> str:
        if not self._on(PiiCategory.CODED_ID):
            return self._off("patient", alt)
        return self.pii(sub.rand_no, PiiCategory.CODED_ID, "patient", "rand_no", "prefixed")

    def mrn(self, sub: Subject, alt: str | None = None) -> str:
        if not self._on(PiiCategory.PHI_DIRECT):
            return self._off("patient", alt)
        return self.pii(sub.mrn, PiiCategory.PHI_DIRECT, "patient", "mrn", "site_format")

    def dob(self, sub: Subject, alt: str | None = None) -> str:
        if not self._on(PiiCategory.PHI_DIRECT):
            return self._off("patient", alt)
        s = self.pick(V.DATE_SURFACES[self.lang])
        return self.pii(V.fmt_date(sub.dob, s), PiiCategory.PHI_DIRECT, "patient", "dob", s)

    def address(self, sub: Subject, city: str, alt: str | None = None) -> str:
        if not self._on(PiiCategory.PHI_DIRECT):
            return self._off("patient", alt)
        return self.pii(f"{sub.street}, {city}", PiiCategory.PHI_DIRECT, "patient", "address",
                        "street_city")  # fmt: skip

    def postcode(self, sub: Subject, alt: str | None = None) -> str:
        if not self._on(PiiCategory.PHI_QUASI):
            return self._off("patient", alt)
        return self.pii(sub.postcode, PiiCategory.PHI_QUASI, "patient", "zip", "local")

    def event_date(self, d: date, alt: str | None = None) -> str:
        """A patient's visit/event date (phi_quasi)."""
        if not self._on(PiiCategory.PHI_QUASI):
            return self._off("patient", alt)
        s = self.pick(V.DATE_SURFACES[self.lang])
        return self.pii(V.fmt_date(d, s), PiiCategory.PHI_QUASI, "patient", "event_date", s)

    def age(self, sub: Subject) -> str:
        """Ages <= 89 are not identifiers; > 89 is phi_quasi."""
        a = sub.age
        if a <= 89:
            return str(a)
        if not self._on(PiiCategory.PHI_QUASI):
            return "over 89" if self.lang == "en" else ">89"
        return self.pii(str(a), PiiCategory.PHI_QUASI, "patient", "age", "over_89")

    # --- negatives --------------------------------------------------------------------------

    def protocol(self, st: Study) -> str:
        return self.neg(st.protocol_no, "protocol_no")

    def nct(self, st: Study) -> str:
        return self.neg(st.nct, "nct_id")

    def eudract(self, st: Study) -> str:
        return self.neg(st.eudract, "eudract_no")

    def compound(self, st: Study) -> str:
        return self.neg(st.compound, "compound_code")

    def site_no(self, site_no: str) -> str:
        return self.neg(site_no, "site_no")

    def doc_date(self, d: date) -> str:
        """A document date (effective, approval, report version): not PHI."""
        return self.neg(V.fmt_date(d, self.pick(V.DATE_SURFACES[self.lang])), "non_phi_date")

    def fmt(self, d: date) -> str:
        """A date with no label at all (e.g. a study milestone inside prose)."""
        return V.fmt_date(d, self.pick(V.DATE_SURFACES[self.lang]))

    def globals(self) -> dict[str, Any]:
        return {n: getattr(self, n) for n in (
            "pii", "neg", "section", "pick", "tr", "name", "initials", "email", "phone",
            "subject_id", "rand_no", "mrn", "dob", "address", "postcode", "event_date", "age",
            "protocol", "nct", "eudract", "compound", "site_no", "doc_date", "fmt",
        )}  # fmt: skip


_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(str(TEMPLATES)),
    undefined=jinja2.StrictUndefined,
    autoescape=False,
    trim_blocks=True,
    lstrip_blocks=True,
    keep_trailing_newline=True,
)


def template_names() -> list[str]:
    return sorted(_ENV.list_templates(extensions=["j2"]))


def render_raw(template: str, ctx: DocCtx, **data: Any) -> str:
    """Rendered text still containing sentinels. Blocks rendered with the same ctx (hard
    negatives, filler, headers/footers) can be spliced in before `finish` resolves once, so
    inserted content is labeled by the same left-to-right pass (no span remap needed)."""
    return _ENV.get_template(template).render(**ctx.globals(), lang=ctx.lang, mode=ctx.mode, **data)


def finish(raw: str, ctx: DocCtx) -> Rendered:
    raw = re.sub(r"\n{3,}", "\n\n", raw).strip() + "\n"
    return resolve(raw, ctx.slots, ctx.negs, ctx.heads)


def render(template: str, ctx: DocCtx, **data: Any) -> Rendered:
    return finish(render_raw(template, ctx, **data), ctx)


def insert_at_section(raw: str, block: str, r: random.Random) -> str:
    """Insert `block` (a paragraph) before a random section header other than the first, or at
    the end when the document has a single section."""
    heads = [m.start() for m in SENTINEL.finditer(raw) if m.group(1) == "h"][1:]
    if not heads:
        return raw.rstrip("\n") + "\n\n" + block.strip("\n") + "\n"
    at = r.choice(heads)
    line_start = raw.rfind("\n", 0, at) + 1
    return raw[:line_start] + block.strip("\n") + "\n\n" + raw[line_start:]


GENERATOR_DIR = Path(__file__).parent


def template_vocabulary() -> set[str]:
    """Every word the generator can emit (lowercased): templates, filler grammar, and the string
    constants in generator code (month names, AE terms, findings, ...). The world avoids person
    names that collide with any of them, so V2 never mistakes ordinary text for a person."""
    words: set[str] = set()
    for p in sorted(GENERATOR_DIR.rglob("*")):
        if p.is_file() and p.suffix in (".j2", ".py", ".txt", ".yaml"):
            words |= {w.lower() for w in re.findall(r"[^\W\d_]{2,}", p.read_text(encoding="utf-8"))}
    return words
