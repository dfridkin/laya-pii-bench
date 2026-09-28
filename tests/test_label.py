import re
from itertools import pairwise
from pathlib import Path
from typing import Any

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from bench.config import Arm, load_arms, load_policy
from bench.domain import Document, PiiCategory, Span
from bench.label import (
    BACKOFF_TOKENS,
    chunk_windows,
    derive_gold,
    label_docs,
    member_spans,
    read_docs,
    section_windows,
)
from tests.fixture_expected import FIXTURE_UNIT_OFFSETS, FIXTURE_UNITS

ROOT = Path(__file__).resolve().parent.parent
POLICY = load_policy(ROOT / "config" / "policy.yaml")
FIXTURE_POLICY = POLICY.model_copy(update={"coded_id_is_pii": True})
ARMS = load_arms(ROOT / "config" / "arms.yaml")


def fake_offsets(text: str) -> list[tuple[int, int]]:
    """ByteLevel-like: leading whitespace attaches to the word; words split into 3-char pieces."""
    out: list[tuple[int, int]] = []
    for m in re.finditer(r"\s*\S+", text):
        ws = len(m.group(0)) - len(m.group(0).lstrip())
        word_start = m.start() + ws
        out.append((m.start(), min(word_start + 3, m.end())))
        for p in range(word_start + 3, m.end(), 3):
            out.append((p, min(p + 3, m.end())))
    return out


def span(start: int, end: int, cat: str = "phi_direct", role: str = "patient") -> Span:
    return Span.model_validate(
        {
            "start": start,
            "end": end,
            "category": cat,
            "role": role,
            "value_kind": "k",
            "surface": "s",
        }
    )


def doc(text: str, spans: list[Span], doc_type: str = "csr_patient_narrative") -> Document:
    return Document.model_validate(
        {
            "id": "d",
            "doc_type": doc_type,
            "lang": "en",
            "text": text,
            "spans": [s.model_dump() for s in spans],
            "negatives": [],
            "tags": [],
            "length_bucket": "short",
            "pii_depth": None,
            "world_refs": {"study": "s", "site": "1", "subjects": []},
            "gen_meta": {},
        }
    )


# --- segmentation ------------------------------------------------------------------------------


def test_fake_tokenizer_shape() -> None:
    assert fake_offsets("ab abcdefg") == [(0, 2), (2, 6), (6, 9), (9, 10)]


def test_short_doc_is_one_window() -> None:
    text = "one two three"
    assert chunk_windows(text, fake_offsets(text), 64, 8) == [(0, 4)]


def test_backoff_lands_on_word_start() -> None:
    text = " ".join(["abcdefghi"] * 20)  # every word = 3 pieces; word starts every 3rd token
    offs = fake_offsets(text)
    windows = chunk_windows(text, offs, 20, 4)
    first_end = windows[0][1]
    assert first_end == 18  # 20 is mid-word; 18 starts a word
    assert text[offs[first_end][0]].isspace()
    assert windows[1][0] == first_end - 3  # 18 - 4 = 14 is mid-word; snapped to the word at 15


def test_hard_cut_without_word_start() -> None:
    text = "x" * 200  # one long word: no clean cut available
    offs = fake_offsets(text)
    windows = chunk_windows(text, offs, 20, 4)
    assert windows[0] == (0, 20)


def test_whitespace_tail_joins_previous_window() -> None:
    # audit A7: exactly `size` word tokens then a newline gave [(0, 20), (16, 21)], a duplicate unit
    text = " ".join(["ab"] * 20) + "\n"
    offs = fake_offsets(text)
    assert len(offs) == 20  # the trailing newline is part of no token here; add one explicitly
    offs = [*offs, (len(text) - 1, len(text))]
    assert chunk_windows(text, offs, 20, 4) == [(0, 21)]


def test_next_window_starts_on_a_word() -> None:
    text = " ".join(["abcdefghi"] * 20)  # words = 3 pieces; word starts at tokens 0, 3, 6, ...
    offs = fake_offsets(text)
    windows = chunk_windows(text, offs, 20, 4)
    assert windows[0] == (0, 18) and windows[1][0] == 15  # 18 - 4 = 14 (mid-word) -> 15


def test_size_must_exceed_overlap_plus_backoff() -> None:
    with pytest.raises(ValueError):
        chunk_windows("a b", [(0, 1), (1, 3)], BACKOFF_TOKENS + 4, 4)


words = st.lists(st.text(alphabet="abcdefghijklmnop", min_size=1, max_size=12), min_size=1)


@settings(max_examples=500)
@given(words, st.integers(min_value=13, max_value=40), st.integers(min_value=0, max_value=4))
def test_windows_cover_every_token(ws: list[str], size: int, overlap: int) -> None:
    text = " ".join(ws)
    offs = fake_offsets(text)
    windows = chunk_windows(text, offs, size, overlap)
    assert windows[0][0] == 0 and windows[-1][1] == len(offs)
    for (s0, e0), (s1, _) in pairwise(windows):
        assert e0 - overlap <= s1 <= e0 and s1 > s0
        assert s1 < e0 or overlap == 0  # windows share tokens only when overlap > 0
        # snapped forward to a word start unless none exists in the overlap
        assert s1 == e0 - overlap or text[offs[s1][0]].isspace() or text[offs[s1][0] - 1].isspace()
    for s, e in windows:
        assert 0 < e - s <= size


# --- gold ---------------------------------------------------------------------------------------


def test_member_spans_overlap_semantics() -> None:
    spans = [span(0, 4), span(10, 20), span(30, 31)]
    assert member_spans(spans, 4, 10) == []
    assert member_spans(spans, 3, 11) == spans[:2]


@pytest.mark.parametrize(
    ("spans", "want"),
    [
        ([], ("B", "none", "none")),
        ([span(0, 4)], ("A", "patient", "direct")),
        ([span(0, 4, "staff_pii", "staff")], ("A", "staff", "staff")),
        ([span(0, 4, "staff_pii", "sponsor")], ("A", "staff", "staff")),  # D-017
        # D-001: coded ids don't make a unit PII or add a role, but stay the category answer
        ([span(0, 4, "coded_id"), span(5, 9, "staff_pii", "staff")], ("A", "staff", "coded")),
        ([span(0, 4, "coded_id")], ("B", "none", "coded")),
        ([span(0, 4, "phi_quasi"), span(5, 9, "phi_direct")], ("A", "patient", "direct")),
    ],
)
def test_derive_gold(spans: list[Span], want: tuple[str, str, str]) -> None:
    gold = derive_gold(doc("x" * 20, spans), spans, POLICY)
    assert (gold.pii_present, gold.subject_role, gold.category) == want
    assert gold.doc_kind == "narrative"


def test_coded_ids_count_when_policy_says_so() -> None:
    policy = POLICY.model_copy(update={"coded_id_is_pii": True})  # the D-001 alternative
    spans = [span(0, 4, "coded_id")]
    gold = derive_gold(doc("x" * 20, spans), spans, policy)
    assert (gold.pii_present, gold.subject_role, gold.category) == ("A", "patient", "coded")
    assert gold.categories_multi[PiiCategory.CODED_ID] is True


def arm(**kw: Any) -> Arm:
    base: dict[str, Any] = {
        "checkpoint": "english",
        "unit": {"kind": "chunk", "size": 20, "overlap": 4},
        "max_len": 64,
        "head_max_len": 16,
    }
    return Arm.model_validate(base | kw)


def test_units_split_span_and_truncation() -> None:
    text = " ".join(["abcdefghi"] * 20)
    offs = fake_offsets(text)
    cut = offs[18][0]  # first window ends before token 18
    s = span(cut - 5, cut + 5)  # straddles the first boundary
    units = label_docs([doc(text, [s])], arm(), POLICY, fake_offsets, "fake")
    assert units[0].split_span and units[0].gold.pii_present == "A"
    assert units[0].id == "d:chunk:64:0" and units[0].tokens == 18
    assert not units[0].truncated
    tiny = label_docs([doc(text, [])], arm(max_len=30, head_max_len=16), POLICY, fake_offsets, "f")
    assert tiny[0].truncated  # 18 tokens > budget 14; flagged, never dropped


def test_empty_doc_rejected() -> None:
    with pytest.raises(ValueError, match="never dropped"):
        label_docs([doc(" ", [])], arm(), POLICY, fake_offsets, "fake")


def doc_with_sections(text: str, heads: list[int]) -> Document:
    d = doc(text, [])
    return d.model_copy(update={"gen_meta": {"sections": heads}})


def test_section_windows_merge_and_oversize() -> None:
    #           section tokens: 4 | 3 | 10 | 2 ; target 8
    toks = [(i, i + 1) for i in range(19)]
    bounds = [0, 4, 7, 17]
    assert section_windows(bounds, 19, toks, 8) == [(0, 7), (7, 17), (17, 19)]


def test_section_units_cover_the_document() -> None:
    text = " ".join(f"s{i}" + " w" * 6 for i in range(10))
    offs = fake_offsets(text)
    heads = [text.index(f"s{i} ") for i in range(1, 10)]
    units = label_docs([doc_with_sections(text, heads)], arm(unit={"kind": "section",
                       "target_tokens": 16}, max_len=64, head_max_len=16), POLICY, fake_offsets,
                       "f")  # fmt: skip
    assert [u.kind for u in units] == ["section"] * len(units) and len(units) > 1
    assert units[0].start == offs[0][0] and units[-1].end == offs[-1][1]
    assert all(a.end <= b.start for a, b in pairwise(units))
    assert sum(u.tokens for u in units) == len(offs)
    assert all(u.tokens <= 16 for u in units)
    assert all(u.id == f"d:section:64:{i}" for i, u in enumerate(units))


def test_doc_unit_and_truncation() -> None:
    text = " ".join(["abcdefghi"] * 20)
    [u] = label_docs([doc(text, [])], arm(unit={"kind": "doc"}, max_len=64, head_max_len=16),
                     POLICY, fake_offsets, "f")  # fmt: skip
    assert (u.kind, u.start, u.end, u.tokens) == ("doc", 0, len(text), len(fake_offsets(text)))
    assert u.truncated  # 60 tokens > budget 48; flagged, not dropped


def test_docs_without_section_offsets_are_one_section() -> None:
    [u] = label_docs([doc("one two three", [])], arm(unit={"kind": "section", "target_tokens": 50}),
                     POLICY, fake_offsets, "f")  # fmt: skip
    assert u.tokens == len(fake_offsets("one two three"))


@settings(max_examples=300)
@given(st.lists(st.integers(1, 30), min_size=1, max_size=12), st.integers(5, 60))
def test_section_windows_partition_tokens(sizes: list[int], target: int) -> None:
    n = sum(sizes)
    toks = [(i, i + 1) for i in range(n)]
    bounds = [sum(sizes[:k]) for k in range(len(sizes))]
    wins = section_windows(bounds, n, toks, target)
    assert wins[0][0] == 0 and wins[-1][1] == n
    assert all(a[1] == b[0] for a, b in pairwise(wins))
    starts = set(bounds)
    for a, b in wins:
        assert a in starts and (b in starts or b == n)  # windows are whole sections
        assert b - a <= target or ((b in starts or b == n) and not any(a < x < b for x in starts))


@pytest.mark.model
def test_fixture_units_match_hand_gold() -> None:
    from bench import tokenize

    tok = tokenize.load("english", ROOT / "models.lock.json")
    docs = read_docs(ROOT / "fixtures" / "mini" / "docs.jsonl")
    # FIXTURE_UNITS was hand-derived with coded ids counting as PII; pin that policy here so the
    # hand table (and the golden metric arithmetic built on it) stays valid
    units = label_docs(docs, ARMS.arms["A"], FIXTURE_POLICY, tok, tok.name)
    got = {u.id: (u.gold, u.split_span) for u in units}
    assert got == FIXTURE_UNITS
    # the live policy (D-001: no) differs only where coded ids were a unit's only PII
    live = {u.id: u.gold for u in label_docs(docs, ARMS.arms["A"], POLICY, tok, tok.name)}
    changed = {k: (g.pii_present, g.subject_role, g.category) for k, g in live.items()
               if g != FIXTURE_UNITS[k][0]}  # fmt: skip
    assert changed == {
        "fx04:chunk:512:0": ("B", "none", "coded"),  # CRF with subject ids only
        "fx05:chunk:512:0": ("A", "staff", "coded"),  # staff email mentioning a subject id
    }
    assert {u.id: (u.start, u.end, u.tokens) for u in units} == FIXTURE_UNIT_OFFSETS
    assert all(not u.truncated and u.tokens <= 256 for u in units)
    # units record exactly which tokenizer revision counted them (audit A10)
    rev = tokenize.load("english", ROOT / "models.lock.json").name
    assert rev.startswith("english@") and len(rev) == len("english@") + 40
    assert {u.tokenizer for u in units} == {rev}
