import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from bench.markup import MarkupError, resolve

plain = st.text(alphabet=st.characters(blacklist_characters="⟦⟧|"), max_size=30)
value = plain.filter(lambda s: len(s) > 0)


@settings(max_examples=500)
@given(st.lists(st.tuples(plain, st.booleans(), value), max_size=8), plain)
def test_offsets_point_at_values(parts: list[tuple[str, bool, str]], tail: str) -> None:
    raw = (
        "".join(
            lit + (f"⟦s|{v}|phi_direct|patient|person_name|x⟧" if is_span else f"⟦n|{v}|lot_no⟧")
            for lit, is_span, v in parts
        )
        + tail
    )
    text, spans, negs = resolve(raw)
    want_spans = [v for _, is_span, v in parts if is_span]
    want_negs = [v for _, is_span, v in parts if not is_span]
    assert [text[s.start : s.end] for s in spans] == want_spans
    assert [text[n.start : n.end] for n in negs] == want_negs
    assert text == "".join(lit + v for lit, _, v in parts) + tail


def test_repeated_values_get_distinct_offsets() -> None:
    m = "⟦s|Maria|phi_direct|patient|person_name|first⟧"
    raw = f"Maria and Mariana: {m} met {m}."
    text, spans, _ = resolve(raw)
    assert text == "Maria and Mariana: Maria met Maria."
    assert [(s.start, s.end) for s in spans] == [(19, 24), (29, 34)]


def test_fields_recorded() -> None:
    _, spans, negs = resolve(
        "⟦s|1001-0023|coded_id|patient|subject_id|plain⟧ ⟦n|NCT09990421|nct_id⟧"
    )
    assert spans[0].category == "coded_id" and spans[0].value_kind == "subject_id"
    assert negs[0].kind == "nct_id"


@pytest.mark.parametrize(
    "raw",
    [
        "⟦s|x|phi_direct|patient⟧",  # missing fields
        "⟦n||lot_no⟧",  # empty value
        "⟦n|x|lot_no|extra⟧",
        "open ⟦s|x",  # unbalanced
        "stray ⟧",
    ],
)
def test_malformed_markup(raw: str) -> None:
    with pytest.raises(MarkupError):
        resolve(raw)


def test_bad_enum_in_marker() -> None:
    with pytest.raises(ValueError):
        resolve("⟦s|x|phi|patient|k|s⟧")
