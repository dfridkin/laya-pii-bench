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
)
from tests.fixture_expected import FIXTURE_UNIT_OFFSETS, FIXTURE_UNITS

ROOT = Path(__file__).resolve().parent.parent
POLICY = load_policy(ROOT / "config" / "policy.yaml")
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
    assert windows[1][0] == first_end - 4


def test_hard_cut_without_word_start() -> None:
    text = "x" * 200  # one long word: no clean cut available
    offs = fake_offsets(text)
    windows = chunk_windows(text, offs, 20, 4)
    assert windows[0] == (0, 20)


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
        assert s1 == e0 - overlap and s1 > s0
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
        ([span(0, 4, "coded_id"), span(5, 9, "staff_pii", "staff")], ("A", "both", "coded")),
        ([span(0, 4, "phi_quasi"), span(5, 9, "phi_direct")], ("A", "patient", "direct")),
    ],
)
def test_derive_gold(spans: list[Span], want: tuple[str, str, str]) -> None:
    gold = derive_gold(doc("x" * 20, spans), spans, POLICY)
    assert (gold.pii_present, gold.subject_role, gold.category) == want
    assert gold.doc_kind == "narrative"


def test_coded_id_not_pii_when_policy_says_so() -> None:
    policy = POLICY.model_copy(update={"coded_id_is_pii": False})
    spans = [span(0, 4, "coded_id")]
    gold = derive_gold(doc("x" * 20, spans), spans, policy)
    assert (gold.pii_present, gold.subject_role, gold.category) == ("B", "none", "none")
    assert gold.categories_multi[PiiCategory.CODED_ID] is True  # raw presence, for qs_v2


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


def test_non_chunk_arm_not_yet() -> None:
    with pytest.raises(NotImplementedError):
        label_docs([], ARMS.arms["B4"], POLICY, fake_offsets, "fake")


@pytest.mark.model
def test_fixture_units_match_hand_gold() -> None:
    from bench import tokenize

    tok = tokenize.load("english", ROOT / "models.lock.json")
    docs = read_docs(ROOT / "fixtures" / "mini" / "docs.jsonl")
    units = label_docs(docs, ARMS.arms["A"], POLICY, tok, tok.name)
    got = {u.id: (u.gold, u.split_span) for u in units}
    assert got == FIXTURE_UNITS
    assert {u.id: (u.start, u.end, u.tokens) for u in units} == FIXTURE_UNIT_OFFSETS
    assert all(not u.truncated and u.tokens <= 256 for u in units)
