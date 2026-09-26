"""Label stage: segment documents into units and derive gold answers (docs/specs/gold-labels.md).

M2 scope: `chunk` units only. Sections and whole docs arrive in M5.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from pathlib import Path

from bench.config import Arm, ChunkUnit, Policy
from bench.domain import (
    CategoryAnswer,
    DocKindAnswer,
    Document,
    GoldAnswers,
    PiiCategory,
    RoleAnswer,
    Span,
    Unit,
)
from bench.tokenize import Offsets

BACKOFF_TOKENS = 8  # prefer to end a chunk on whitespace within its last 8 tokens


def _word_start(text: str, offsets: Sequence[tuple[int, int]], j: int) -> bool:
    """A cut before token j is clean if the token starts with, or follows, whitespace."""
    s = offsets[j][0]
    return text[s].isspace() or (s > 0 and text[s - 1].isspace())


def chunk_windows(
    text: str, offsets: Sequence[tuple[int, int]], size: int, overlap: int
) -> list[tuple[int, int]]:
    """Token windows [start, end) of at most `size` tokens (plus a whitespace-only tail).

    Ends back off up to 8 tokens to a word start; the next window starts `overlap` tokens back,
    snapped forward to a word start, so windows share at most `overlap` tokens.
    """
    if size - BACKOFF_TOKENS <= overlap:
        raise ValueError("chunk size must exceed overlap + backoff")
    n = len(offsets)
    windows: list[tuple[int, int]] = []
    start = 0
    while True:
        end = min(start + size, n)
        if end < n:
            for j in range(end, end - BACKOFF_TOKENS, -1):
                if _word_start(text, offsets, j):
                    end = j
                    break
        # a tail of whitespace-only tokens joins this window instead of becoming its own unit
        # (it would repeat the overlap and be scored twice)
        if end < n and all(text[a:b].isspace() for a, b in offsets[end:]):
            end = n
        windows.append((start, end))
        if end >= n:
            return windows
        # next window starts `overlap` tokens back, snapped forward to a word start
        start = end - overlap
        for j in range(start, end):
            if _word_start(text, offsets, j):
                start = j
                break


def member_spans(spans: Iterable[Span], start: int, end: int) -> list[Span]:
    """Spans sharing at least one character with [start, end)."""
    return [s for s in spans if s.start < end and s.end > start]


def derive_gold(doc: Document, members: Sequence[Span], policy: Policy) -> GoldAnswers:
    counted = [s for s in members if s.category in policy.effective_pii_categories]
    roles = {policy.role_map[s.role] for s in counted} - {"none"}
    role: RoleAnswer = "none"
    if roles == {"patient", "staff"}:
        role = "both"
    elif roles:
        role = "patient" if "patient" in roles else "staff"
    present = {s.category for s in counted}
    category: CategoryAnswer = "none"
    for c in policy.category_precedence:
        if c in present:
            category = policy.category_answer_map[c]
            break
    doc_kind: DocKindAnswer = policy.doc_kind_map[doc.doc_type]
    raw_present = {s.category for s in members}
    return GoldAnswers(
        pii_present="A" if counted else "B",
        subject_role=role,
        category=category,
        doc_kind=doc_kind,
        categories_multi={c: c in raw_present for c in PiiCategory},
    )


def chunk_units(
    doc: Document, arm: Arm, unit: ChunkUnit, offsets: Offsets, policy: Policy, tokenizer: str
) -> list[Unit]:
    toks = offsets(doc.text)
    if not toks:
        raise ValueError(f"{doc.id}: no tokens; units are never dropped")
    units: list[Unit] = []
    for idx, (ts, te) in enumerate(chunk_windows(doc.text, toks, unit.size, unit.overlap)):
        start, end = toks[ts][0], toks[te - 1][1]
        members = member_spans(doc.spans, start, end)
        units.append(
            Unit(
                id=f"{doc.id}:chunk:{arm.max_len}:{idx}",
                doc_id=doc.id,
                kind="chunk",
                start=start,
                end=end,
                tokens=te - ts,
                tokenizer=tokenizer,
                truncated=te - ts > arm.state_budget,
                split_span=any(s.start < start or s.end > end for s in members),
                gold=derive_gold(doc, members, policy),
            )
        )
    return units


def label_docs(
    docs: Iterable[Document], arm: Arm, policy: Policy, offsets: Offsets, tokenizer: str
) -> list[Unit]:
    if not isinstance(arm.unit, ChunkUnit):
        raise NotImplementedError(f"unit kind {arm.unit.kind!r} arrives in M5")
    chunk = arm.unit
    return [u for d in docs for u in chunk_units(d, arm, chunk, offsets, policy, tokenizer)]


def read_docs(path: Path) -> list[Document]:
    with path.open(encoding="utf-8") as f:
        return [Document.model_validate_json(line) for line in f if line.strip()]


def write_units(units: Iterable[Unit], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(u.model_dump_json() + "\n" for u in units), encoding="utf-8")


def read_units(path: Path) -> list[Unit]:
    with path.open(encoding="utf-8") as f:
        return [Unit.model_validate_json(line) for line in f if line.strip()]
