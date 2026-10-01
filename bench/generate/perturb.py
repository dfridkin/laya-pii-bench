"""Character-level perturbations with span remap (docs/specs/generator.md).

Each perturbation proposes `Edit`s (replace `length` chars at `pos` with `new`). Edits never
straddle a span/negative boundary: an edit lies wholly inside a labeled value (the value changes and
stays labeled, e.g. OCR noise or a wrapped name) or wholly outside. `apply` rewrites the text and
remaps every span, negative and section offset in one pass. Content-adding steps (headers/footers,
hard negatives, filler) happen before resolve instead, so they need no remap.
"""

from __future__ import annotations

import random
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from itertools import pairwise

from bench.domain import Document, Negative, Span

OCR_SUBS = {
    "l": "1",
    "1": "l",
    "O": "0",
    "0": "O",
    "Z": "2",
    "2": "Z",
    "S": "5",
    "5": "S",
    "B": "8",
}


@dataclass(frozen=True)
class Edit:
    pos: int
    length: int
    new: str


class RemapError(ValueError):
    pass


def _intervals(doc: Document) -> list[tuple[int, int]]:
    return sorted([(s.start, s.end) for s in doc.spans] + [(n.start, n.end) for n in doc.negatives])


def straddles(e: Edit, start: int, end: int) -> bool:
    """True if the edit crosses the boundary of [start, end) (partly inside, partly outside)."""
    a, b = e.pos, e.pos + e.length
    if e.length == 0:  # insertion: inside iff start < pos < end; at an edge it is outside
        return False
    inside = start <= a and b <= end
    outside = b <= start or a >= end
    return not (inside or outside)


def shift(x: int, edits: Sequence[Edit], *, is_end: bool = False) -> int:
    """New offset of old offset `x`: edits wholly before `x` move it. An insertion exactly at `x`
    moves a start (the inserted text precedes it) but not an end (it follows the span)."""
    d = 0
    for e in edits:
        b = e.pos + e.length
        if b < x or (b == x and (e.length > 0 or not is_end)):
            d += len(e.new) - e.length
    return x + d


def apply(doc: Document, edits: Iterable[Edit], tag: str | None = None) -> Document:
    es = sorted(edits, key=lambda e: e.pos)
    for x, y in pairwise(es):
        if x.pos + x.length > y.pos:
            raise RemapError("overlapping edits")
    for e in es:
        for start, end in _intervals(doc):
            if straddles(e, start, end):
                raise RemapError(f"edit at {e.pos} straddles labeled interval [{start}, {end})")
    text, last = doc.text, 0
    parts: list[str] = []
    for e in es:
        parts += [text[last : e.pos], e.new]
        last = e.pos + e.length
    parts.append(text[last:])
    new_text = "".join(parts)

    def re_span(s: Span) -> Span:
        a, b = shift(s.start, es), shift(s.end, es, is_end=True)
        return s.model_copy(update={"start": a, "end": b, "value": new_text[a:b]})

    def re_neg(n: Negative) -> Negative:
        a, b = shift(n.start, es), shift(n.end, es, is_end=True)
        return n.model_copy(update={"start": a, "end": b, "value": new_text[a:b]})

    meta = dict(doc.gen_meta)
    secs = meta.get("sections")
    if isinstance(secs, list):
        meta["sections"] = [shift(int(p), es) for p in secs]
    tags = [*doc.tags, tag] if tag and tag not in doc.tags else list(doc.tags)
    return doc.model_copy(update={
        "text": new_text, "spans": [re_span(s) for s in doc.spans],
        "negatives": [re_neg(n) for n in doc.negatives], "gen_meta": meta, "tags": tags,
    })  # fmt: skip


# --- perturbations ------------------------------------------------------------------------------


def line_wrap(doc: Document, width: int) -> list[Edit]:
    """Hard-wrap prose lines at `width` by turning the last space before the limit into a newline.
    A labeled value that gets wrapped keeps its label (it now contains a newline)."""
    edits: list[Edit] = []
    pos = 0
    for line in doc.text.split("\n"):
        if len(line) > width and "|" not in line and "\t" not in line:
            col = 0
            while len(line) - col > width:
                cut = line.rfind(" ", col, col + width + 1)
                if cut <= col:
                    break
                edits.append(Edit(pos + cut, 1, "\n"))
                col = cut + 1
        pos += len(line) + 1
    return edits


def _word_at(text: str, i: int) -> tuple[int, int]:
    a, b = i, i + 1
    while a > 0 and text[a - 1].isalpha():
        a -= 1
    while b < len(text) and text[b].isalpha():
        b += 1
    return a, b


def ocr_noise(
    doc: Document, r: random.Random, rate: float = 0.01,
    protected: frozenset[str] = frozenset(),
) -> list[Edit]:  # fmt: skip
    """Character confusions (l/1, O/0, Z/2, S/5, B/8) and dropped letters. Drops stay away from
    labeled-value edges and never empty a value; spans keep their labels. If the edits in a word
    together turn it into a `protected` word (a world person's name token, lowercased), all of
    that word's edits are dropped, so noise never fabricates an unlabeled name ("Samples" ->
    "Sales" by two drops; M8 scale-up, gold audit). The random draws are unchanged."""
    text = doc.text
    edges = {p for s, e in _intervals(doc) for p in (s, e - 1)}
    inside = [(s, e) for s, e in _intervals(doc)]
    edits: list[Edit] = []
    for i, ch in enumerate(text):
        if r.random() >= rate:
            continue
        if ch in OCR_SUBS:
            edits.append(Edit(i, 1, OCR_SUBS[ch]))
        elif (
            ch.isalpha()
            and i not in edges
            and i > 0
            and text[i - 1].isalpha()
            and (i + 1 < len(text) and text[i + 1].isalpha())
        ):
            if any(s <= i < e and e - s <= 3 for s, e in inside):
                continue  # never shrink a short value toward empty
            edits.append(Edit(i, 1, ""))
    if not protected:
        return edits
    by_word: dict[tuple[int, int], list[Edit]] = {}
    for e in edits:
        if text[e.pos].isalpha():
            by_word.setdefault(_word_at(text, e.pos), []).append(e)
    dropped: set[int] = set()
    for (a, b), group in by_word.items():
        word: list[str] = []
        pos = a
        for e in sorted(group, key=lambda x: x.pos):
            word.append(text[pos : e.pos] + e.new)
            pos = e.pos + e.length
        word.append(text[pos:b])
        if "".join(word).lower() in protected:
            dropped |= {id(e) for e in group}
    return [e for e in edits if id(e) not in dropped]


def _table_blocks(text: str) -> list[list[tuple[int, str]]]:
    """Runs of >= 2 consecutive lines with ` | ` separators, as (line start, line) pairs.
    Single pipe lines (e.g. page headers) are not tables."""
    blocks: list[list[tuple[int, str]]] = []
    run: list[tuple[int, str]] = []
    pos = 0
    for line in text.split("\n"):
        if " | " in line:
            run.append((pos, line))
        else:
            if len(run) >= 2:
                blocks.append(run)
            run = []
        pos += len(line) + 1
    if len(run) >= 2:
        blocks.append(run)
    return blocks


def table_style(doc: Document, style: str) -> list[Edit]:
    """Re-render pipe tables as tab-separated or fixed-width columns (separators are never inside
    labeled values, so only unlabeled text changes)."""
    edits: list[Edit] = []
    for block in _table_blocks(doc.text):
        rows = [line.split(" | ") for _, line in block]
        ncol = max(len(r) for r in rows)
        widths = [max((len(r[k]) for r in rows if k < len(r)), default=0) for k in range(ncol)]
        for (start, _), cells in zip(block, rows, strict=True):
            col = 0
            for k, cell in enumerate(cells[:-1]):
                col += len(cell)
                sep = "\t" if style == "tab" else " " * (widths[k] - len(cell) + 2)
                edits.append(Edit(start + col, 3, sep))
                col += 3
    return edits
