"""Surface-form variants (docs/specs/generator.md). Pure functions of (entity, surface key).

Every variant of every value can be enumerated (`*_forms`), which is what V2 scans for.
"""

from __future__ import annotations

from datetime import date

from bench.generate.world import Person

MONTHS_EN = ("January", "February", "March", "April", "May", "June", "July", "August",
             "September", "October", "November", "December")  # fmt: skip
MON3 = tuple(m[:3] for m in MONTHS_EN)
MONTHS_DE = ("Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September",
             "Oktober", "November", "Dezember")  # fmt: skip
MONTHS_ES = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
             "septiembre", "octubre", "noviembre", "diciembre")  # fmt: skip
MONTHS_PL = ("stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca", "lipca", "sierpnia",
             "września", "października", "listopada", "grudnia")  # fmt: skip

NAME_SURFACES = ("first_last", "last_first_upper", "last_first", "initial_last", "title_last",
                 "title_first_last", "first", "last")  # fmt: skip
INITIALS_SURFACES = ("plain", "dotted", "dashed", "middle_x")
SUBJECT_ID_SURFACES = ("plain", "prefixed", "hash")
DATE_SURFACES: dict[str, tuple[str, ...]] = {
    "en": ("dd_mon_yyyy", "us_slash", "iso", "ddmonyyyy", "long_en"),
    "de": ("de_dotted", "iso", "long_de"),
    "es": ("eu_slash", "iso", "long_es"),
    "pl": ("de_dotted", "iso", "long_pl"),
}


def name(p: Person, surface: str) -> str:
    match surface:
        case "first_last":
            return f"{p.given} {p.family}"
        case "last_first_upper":
            return f"{p.family.upper()}, {p.given}"
        case "last_first":
            return f"{p.family}, {p.given}"
        case "initial_last":
            return f"{p.given[0]}. {p.family}"
        case "title_last":
            return f"{p.title} {p.family}"
        case "title_first_last":
            return f"{p.title} {p.given} {p.family}"
        case "first":
            return p.given
        case "last":
            return p.family
        case _:
            raise ValueError(surface)


def initials(p: Person, surface: str) -> str:
    g, f = p.given[0].upper(), p.family[0].upper()
    match surface:
        case "plain":
            return f"{g}{f}"
        case "dotted":
            return f"{g}.{f}."
        case "dashed":
            return f"{g}-{f}"
        case "middle_x":
            return f"{g}X{f}"
        case _:
            raise ValueError(surface)


def subject_id(sid: str, surface: str) -> str:
    match surface:
        case "plain":
            return sid
        case "prefixed":
            return f"Subj {sid}"
        case "hash":
            return "#" + sid.replace("-", "")
        case _:
            raise ValueError(surface)


def fmt_date(d: date, surface: str) -> str:
    match surface:
        case "dd_mon_yyyy":
            return f"{d.day:02d}-{MON3[d.month - 1]}-{d.year}"
        case "us_slash":
            return f"{d.month:02d}/{d.day:02d}/{d.year}"
        case "iso":
            return d.isoformat()
        case "ddmonyyyy":
            return f"{d.day:02d}{MON3[d.month - 1].upper()}{d.year}"
        case "long_en":
            return f"{MONTHS_EN[d.month - 1]} {d.day}, {d.year}"
        case "de_dotted":
            return f"{d.day:02d}.{d.month:02d}.{d.year}"
        case "eu_slash":
            return f"{d.day:02d}/{d.month:02d}/{d.year}"
        case "long_de":
            return f"{d.day}. {MONTHS_DE[d.month - 1]} {d.year}"
        case "long_es":
            return f"{d.day} de {MONTHS_ES[d.month - 1]} de {d.year}"
        case "long_pl":
            return f"{d.day} {MONTHS_PL[d.month - 1]} {d.year}"
        case _:
            raise ValueError(surface)


def name_forms(p: Person) -> list[str]:
    """Distinctive name forms V2 scans for. A lone given name is excluded: it is labeled where
    templates use it (greetings), but as a bare word it collides with ordinary text."""
    return sorted({name(p, s) for s in NAME_SURFACES if s != "first"})


def initials_forms(p: Person) -> list[str]:
    # bare two-letter initials ("MG") are too short to scan without false alarms; dotted/dashed
    # forms are distinctive enough
    return sorted({initials(p, s) for s in ("dotted", "dashed", "middle_x")})


def subject_id_forms(sid: str) -> list[str]:
    return sorted({subject_id(sid, s) for s in SUBJECT_ID_SURFACES})


def date_forms(d: date) -> list[str]:
    return sorted({fmt_date(d, s) for ss in DATE_SURFACES.values() for s in ss})
