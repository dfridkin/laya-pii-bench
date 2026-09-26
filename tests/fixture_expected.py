"""Hand-derived gold for the fixture's arm-A chunk units (256 tokens, overlap 32, max_len 512).

Derived by reading fixtures/mini/src/*.yaml against docs/specs/gold-labels.md with
config/policy.yaml (coded_id_is_pii: true, D-001 provisional). fx06 is the only doc longer than
256 English tokens, so it is the only doc with two chunks; its address straddles the boundary.
"""

from bench.domain import GoldAnswers, PiiCategory, Unit

D, Q, C, S = (
    PiiCategory.PHI_DIRECT,
    PiiCategory.PHI_QUASI,
    PiiCategory.CODED_ID,
    PiiCategory.STAFF_PII,
)


def g(pii: str, role: str, cat: str, kind: str, *present: PiiCategory) -> GoldAnswers:
    return GoldAnswers.model_validate(
        {
            "pii_present": pii,
            "subject_role": role,
            "category": cat,
            "doc_kind": kind,
            "categories_multi": {c: c in present for c in PiiCategory},
        }
    )


# unit_id -> (gold, split_span)
FIXTURE_UNITS: dict[str, tuple[GoldAnswers, bool]] = {
    "fx01:chunk:512:0": (g("A", "both", "direct", "narrative", D, Q, C, S), False),
    "fx02:chunk:512:0": (g("B", "none", "none", "protocol_text"), False),
    "fx03:chunk:512:0": (g("A", "staff", "staff", "form_table", S), False),
    "fx04:chunk:512:0": (g("A", "patient", "coded", "form_table", C), False),
    "fx05:chunk:512:0": (g("A", "both", "coded", "correspondence", C, S), False),
    "fx06:chunk:512:0": (g("A", "both", "direct", "narrative", D, S), True),
    "fx06:chunk:512:1": (g("A", "patient", "direct", "narrative", D), False),
    "fx07:chunk:512:0": (g("B", "none", "none", "protocol_text"), False),
    "fx08:chunk:512:0": (g("A", "patient", "direct", "form_table", D, Q, C), False),
    "fx09:chunk:512:0": (g("B", "none", "none", "form_table"), False),
    "fx10:chunk:512:0": (g("A", "both", "direct", "narrative", D, Q, C, S), False),
}

# unit_id -> (start, end, tokens): char offsets and English token count from the label stage,
# pinned here so metric tests run without the tokenizer (checked by test_fixture_units_match).
FIXTURE_UNIT_OFFSETS: dict[str, tuple[int, int, int]] = {
    "fx01:chunk:512:0": (0, 664, 190),
    "fx02:chunk:512:0": (0, 915, 191),
    "fx03:chunk:512:0": (0, 591, 190),
    "fx04:chunk:512:0": (0, 403, 113),
    "fx05:chunk:512:0": (0, 588, 186),
    "fx06:chunk:512:0": (0, 1310, 255),
    "fx06:chunk:512:1": (1142, 1759, 129),
    "fx07:chunk:512:0": (0, 648, 171),
    "fx08:chunk:512:0": (0, 364, 126),
    "fx09:chunk:512:0": (0, 524, 168),
    "fx10:chunk:512:0": (0, 564, 197),
}


def fixture_units() -> list[Unit]:
    out: list[Unit] = []
    for uid, (gold, split_span) in FIXTURE_UNITS.items():
        start, end, tokens = FIXTURE_UNIT_OFFSETS[uid]
        out.append(
            Unit(
                id=uid,
                doc_id=uid.split(":")[0],
                kind="chunk",
                start=start,
                end=end,
                tokens=tokens,
                tokenizer="english",
                truncated=False,
                split_span=split_span,
                gold=gold,
            )
        )
    return out
