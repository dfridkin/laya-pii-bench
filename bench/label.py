"""Label stage: segment documents into units and derive gold answers (docs/specs/gold-labels.md).

Unit kinds per arm: `chunk` (token windows), `section` (generator sections merged up to a token
target), `doc` (whole document). Token counts use the arm checkpoint's tokenizer; a unit over the
state budget is flagged `truncated`, never dropped.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from pathlib import Path

from bench.config import Arm, ChunkUnit, DocUnit, Policy, SectionUnit
from bench.domain import (
    CategoryAnswer,
    DocKindAnswer,
    Document,
    GoldAnswers,
    PiiCategory,
    RoleAnswer,
    Span,
    Unit,
    UnitKind,
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
    # category: the most sensitive kind present, from raw presence (D-001: coded ids are not PII
    # for pii_present/subject_role, but "coded" stays a reachable category answer)
    present = {s.category for s in members}
    category: CategoryAnswer = "none"
    for c in policy.category_precedence:
        if c in present:
            category = policy.category_answer_map[c]
            break
    doc_kind: DocKindAnswer = policy.doc_kind_map[doc.doc_type]
    return GoldAnswers(
        pii_present="A" if counted else "B",
        subject_role=role,
        category=category,
        doc_kind=doc_kind,
        categories_multi={c: c in present for c in PiiCategory},
    )


def _unit(doc: Document, arm: Arm, kind: UnitKind, idx: int, start: int, end: int, tokens: int,
          policy: Policy, tokenizer: str) -> Unit:  # fmt: skip
    members = member_spans(doc.spans, start, end)
    return Unit(
        id=f"{doc.id}:{kind}:{arm.max_len}:{idx}",
        doc_id=doc.id,
        kind=kind,
        start=start,
        end=end,
        tokens=tokens,
        tokenizer=tokenizer,
        truncated=tokens > arm.state_budget,
        split_span=any(s.start < start or s.end > end for s in members),
        gold=derive_gold(doc, members, policy),
    )


def _tokens(doc: Document, offsets: Offsets) -> list[tuple[int, int]]:
    toks = offsets(doc.text)
    if not toks:
        raise ValueError(f"{doc.id}: no tokens; units are never dropped")
    return toks


def chunk_units(
    doc: Document, arm: Arm, unit: ChunkUnit, offsets: Offsets, policy: Policy, tokenizer: str
) -> list[Unit]:
    toks = _tokens(doc, offsets)
    return [
        _unit(doc, arm, "chunk", idx, toks[ts][0], toks[te - 1][1], te - ts, policy, tokenizer)
        for idx, (ts, te) in enumerate(chunk_windows(doc.text, toks, unit.size, unit.overlap))
    ]


def section_bounds(doc: Document) -> list[int]:
    """Character offsets where sections start: 0 plus the generator's section headers."""
    raw = doc.gen_meta.get("sections", [])
    heads = {int(x) for x in raw} if isinstance(raw, list) else set[int]()
    return sorted({0, *(h for h in heads if 0 < h < len(doc.text))})


def section_windows(
    bounds: Sequence[int], text_len: int, toks: Sequence[tuple[int, int]], target: int
) -> list[tuple[int, int]]:
    """Token windows made of whole sections, merged greedily while they fit `target` tokens.
    A single section larger than `target` is its own window (flagged truncated later, never cut)."""
    ends = [*bounds[1:], text_len]
    segs: list[tuple[int, int]] = []  # (first token, end token) per section
    t = 0
    for s_end in ends:
        first = t
        while t < len(toks) and toks[t][0] < s_end:
            t += 1
        segs.append((first, t))
    windows: list[tuple[int, int]] = []
    cur: tuple[int, int] | None = None
    for a, b in segs:
        if a == b:
            continue  # section with no tokens
        if cur is None:
            cur = (a, b)
        elif b - cur[0] <= target:
            cur = (cur[0], b)
        else:
            windows.append(cur)
            cur = (a, b)
    if cur is not None:
        windows.append(cur)
    return windows


def section_units(
    doc: Document, arm: Arm, unit: SectionUnit, offsets: Offsets, policy: Policy, tokenizer: str
) -> list[Unit]:
    toks = _tokens(doc, offsets)
    windows = section_windows(section_bounds(doc), len(doc.text), toks, unit.target_tokens)
    return [
        _unit(doc, arm, "section", idx, toks[ts][0], toks[te - 1][1], te - ts, policy, tokenizer)
        for idx, (ts, te) in enumerate(windows)
    ]


def doc_units(
    doc: Document, arm: Arm, offsets: Offsets, policy: Policy, tokenizer: str
) -> list[Unit]:
    toks = _tokens(doc, offsets)
    return [_unit(doc, arm, "doc", 0, toks[0][0], toks[-1][1], len(toks), policy, tokenizer)]


def label_docs(
    docs: Iterable[Document], arm: Arm, policy: Policy, offsets: Offsets, tokenizer: str
) -> list[Unit]:
    out: list[Unit] = []
    for d in docs:
        match arm.unit:
            case ChunkUnit():
                out += chunk_units(d, arm, arm.unit, offsets, policy, tokenizer)
            case SectionUnit():
                out += section_units(d, arm, arm.unit, offsets, policy, tokenizer)
            case DocUnit():
                out += doc_units(d, arm, offsets, policy, tokenizer)
    return out


def read_docs(path: Path) -> list[Document]:
    with path.open(encoding="utf-8") as f:
        return [Document.model_validate_json(line) for line in f if line.strip()]


def write_units(units: Iterable[Unit], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(u.model_dump_json() + "\n" for u in units), encoding="utf-8")


def read_units(path: Path) -> list[Unit]:
    with path.open(encoding="utf-8") as f:
        return [Unit.model_validate_json(line) for line in f if line.strip()]
