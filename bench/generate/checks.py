"""Generation-time validators (docs/specs/generator.md). Generation fails loudly on any failure.

V1 offset integrity: every span and negative's recorded value equals `text[start:end]`, plus the
   structural checks of `bench.validate` (bounds, overlaps, word edges, roles, tags).
V2 no unlabeled world PII: every distinctive identifier of every person/subject in the world, in
   every variant form, and every date of the subjects a document refers to, must fall inside a
   labeled span wherever it occurs. Matching is on whole words, via a first-token index.
V3 negatives don't overlap spans (part of V1's structural checks, reported separately).
V4..V6 (token budget, distributions, determinism) run on the whole corpus (`bench gen`).
"""

from __future__ import annotations

import re
from collections import defaultdict
from collections.abc import Iterable, Sequence
from dataclasses import dataclass

from bench.config import Policy
from bench.domain import Document
from bench.generate import variants as V
from bench.generate.world import Subject, World
from bench.validate import check_document

_WORD = re.compile(r"\w+")


@dataclass(frozen=True)
class _Form:
    text: str
    prefix: str  # characters before the first word run (e.g. "(" or "#")
    what: str  # description for failure messages


def _index(forms: Iterable[tuple[str, str]]) -> dict[str, list[_Form]]:
    idx: dict[str, list[_Form]] = defaultdict(list)
    for text, what in forms:
        m = _WORD.search(text)
        if m is None:
            continue
        idx[m.group(0)].append(_Form(text, text[: m.start()], what))
    for k in idx:
        idx[k].sort(key=lambda f: -len(f.text))
    return dict(idx)


def world_forms(world: World) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for site in world.sites():
        people = [(p, p.id) for p in site.staff.values()] + [
            (s.person, s.person.id) for s in site.subjects
        ]
        for p, pid in people:
            out += [(f, f"name of {pid}") for f in V.name_forms(p)]
            out += [(f, f"initials of {pid}") for f in V.initials_forms(p)]
            out += [(x, f"contact of {pid}") for x in (p.email, p.phone) if x]
        for s in site.subjects:
            sid = s.person.id
            out += [(f, f"subject id of {sid}") for f in V.subject_id_forms(s.subject_id)]
            out += [(s.rand_no, f"rand no of {sid}"), (s.mrn, f"mrn of {sid}"),
                    (s.street, f"street of {sid}")]  # fmt: skip
    return out


def subject_dates(s: Subject) -> list[tuple[str, str]]:
    ds = {s.dob, s.enrolled, *s.visits}
    for ae in s.aes:
        ds |= {ae.onset} | ({ae.resolved} if ae.resolved else set())
    for cm in s.conmeds:
        ds |= {cm.start} | ({cm.stop} if cm.stop else set())
    ds |= {lab.collected for lab in s.labs} | {d.on for d in s.deviations}
    return [(f, f"date of {s.person.id}") for d in sorted(ds) for f in V.date_forms(d)]


class Scanner:
    """V2: finds identifier occurrences not covered by a labeled span."""

    def __init__(self, world: World) -> None:
        self.world_index = _index(world_forms(world))
        self.subjects = {s.subject_id: s for site in world.sites() for s in site.subjects}

    def unlabeled(self, doc: Document) -> list[str]:
        extra = _index(
            f for sid in doc.world_refs.subjects for f in subject_dates(self.subjects[sid])
        )
        text = doc.text
        covered = sorted((s.start, s.end) for s in doc.spans)
        problems: list[str] = []
        for m in _WORD.finditer(text):
            for idx in (self.world_index, extra):
                for form in idx.get(m.group(0), ()):
                    a = m.start() - len(form.prefix)
                    b = a + len(form.text)
                    if a < 0 or text[a:b] != form.text:
                        continue
                    if (a > 0 and text[a - 1].isalnum()) or (b < len(text) and text[b].isalnum()):
                        continue
                    if not any(s <= a and b <= e for s, e in covered):
                        problems.append(f"V2 unlabeled {form.what}: {form.text!r} at {a}")
                    break  # longest form at this position decided
        return problems


def v1(doc: Document, policy: Policy) -> list[str]:
    errs: list[str] = []
    for kind, items in (("span", doc.spans), ("negative", doc.negatives)):
        for i, it in enumerate(items):
            if it.value is None or doc.text[it.start : it.end] != it.value:
                errs.append(
                    f"V1 {kind}[{i}] value {it.value!r} != text {doc.text[it.start : it.end]!r}"
                )
    return errs + [
        f"V3 {e}" if "overlaps negatives" in e else f"V1 {e}" for e in check_document(doc, policy)
    ]


def check(doc: Document, policy: Policy, scanner: Scanner) -> list[str]:
    return v1(doc, policy) + scanner.unlabeled(doc)


def failures_by_validator(problems: Sequence[str]) -> dict[str, int]:
    out: dict[str, int] = defaultdict(int)
    for p in problems:
        out[p.split(" ", 1)[0]] += 1
    return dict(out)
