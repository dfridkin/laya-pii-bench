"""Inline sentinel markup for hand-labeled documents (the M1 fixture).

Labels are written where the value is, and offsets are recorded while resolving, left to right,
the same way the generator resolves `⟦sN⟧` slots (docs/specs/generator.md). Nothing is located by
searching rendered text (invariant 1).

    ⟦s|<value>|<category>|<role>|<value_kind>|<surface>⟧   PII span
    ⟦n|<value>|<kind>⟧                                     hard negative
"""

from __future__ import annotations

import re

from bench.domain import Negative, Span

MARK = re.compile(r"⟦([sn])\|([^⟦⟧]*)⟧")
_FIELDS = {"s": ("category", "role", "value_kind", "surface"), "n": ("kind",)}


class MarkupError(ValueError):
    pass


def resolve(raw: str) -> tuple[str, list[Span], list[Negative]]:
    out: list[str] = []
    spans: list[Span] = []
    negatives: list[Negative] = []
    pos = last = 0
    for m in MARK.finditer(raw):
        lit = raw[last : m.start()]
        out.append(lit)
        pos += len(lit)
        kind, body = m.group(1), m.group(2).split("|")
        value, meta = body[0], body[1:]
        names = _FIELDS[kind]
        if len(meta) != len(names) or not value:
            raise MarkupError(f"bad marker at char {m.start()}: {m.group(0)!r}")
        fields = dict(zip(names, meta, strict=True))
        end = pos + len(value)
        if kind == "s":
            spans.append(Span.model_validate({"start": pos, "end": end, **fields}))
        else:
            negatives.append(Negative.model_validate({"start": pos, "end": end, **fields}))
        out.append(value)
        pos, last = end, m.end()
    out.append(raw[last:])
    text = "".join(out)
    if "⟦" in text or "⟧" in text:
        raise MarkupError("unbalanced or malformed marker left in text")
    return text, spans, negatives
