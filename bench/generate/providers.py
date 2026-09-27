"""Identifier providers (fictional formats; D-010, invariant 10).

Registry identifiers use ranges that are not issued: NCT numbers start `NCT99`, EudraCT numbers use
the year 2031. Phone numbers use the 555 exchange in every locale.
"""

from __future__ import annotations

import random

MRN_FORMATS = ("mrn8", "hosp_dash", "m_prefix", "digits9")


def protocol_no(compound: str, n: int) -> str:
    return f"{compound}-{n:03d}"


def compound_code(prefix: str, rng: random.Random) -> str:
    return f"{prefix}-{rng.randint(1000, 9999)}"


def nct_id(rng: random.Random) -> str:
    return f"NCT99{rng.randint(0, 999999):06d}"


def eudract_no(rng: random.Random) -> str:
    return f"2031-{rng.randint(0, 999999):06d}-{rng.randint(10, 99)}"


def site_no(study_idx: int, site_idx: int) -> str:
    return f"{study_idx + 1}{site_idx + 1:03d}"  # unique within a study (D-016)


def subject_id(site: str, n: int) -> str:
    return f"{site}-{n:04d}"


def rand_no(rng: random.Random) -> str:
    return f"R-{rng.randint(10000, 99999)}"


def mrn(fmt: str, rng: random.Random) -> str:
    match fmt:
        case "mrn8":
            return f"{rng.randint(0, 99999999):08d}"
        case "hosp_dash":
            return f"H-{rng.randint(1000, 9999)}-{rng.randint(1000, 9999)}"
        case "m_prefix":
            return f"M{rng.randint(100000, 999999)}"
        case _:
            return f"{rng.randint(100000000, 999999999)}"


def lot_no(rng: random.Random) -> str:
    return f"LT-{rng.randint(230000, 269999)}-{rng.choice('ABCDEFGH')}"


def kit_no(rng: random.Random) -> str:
    return f"K-{rng.randint(0, 999999):06d}"


def phone(lang: str, rng: random.Random) -> str:
    tail = f"{rng.randint(0, 9999):04d}"
    return {
        "en": f"(555) 01{rng.randint(0, 9)}-{tail}",
        "de": f"+49 555 01{rng.randint(0, 9)} {tail}",
        "es": f"+34 555 01{rng.randint(0, 9)} {tail}",
        "pl": f"+48 555 01{rng.randint(0, 9)} {tail}",
    }[lang]
