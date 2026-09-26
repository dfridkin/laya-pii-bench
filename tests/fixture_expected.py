"""Hand-derived gold for the fixture's arm-A chunk units (256 tokens, overlap 32, max_len 512).

Derived by reading fixtures/mini/src/*.yaml against docs/specs/gold-labels.md with
config/policy.yaml (coded_id_is_pii: true, D-001 provisional). fx06 is the only doc longer than
256 English tokens, so it is the only doc with two chunks; its address straddles the boundary.
"""

from bench.domain import GoldAnswers, PiiCategory

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
