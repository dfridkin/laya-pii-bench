"""Hard-negative registry and injector (docs/specs/generator.md, D-015).

Values that look like PII but aren't: study identifiers, ID look-alikes, non-PHI dates, eponyms,
clinical numerics. The injector renders a paragraph of them through the document's own DocCtx
(`neg()` sentinels), so offsets come from the same resolve pass as everything else. Injected docs
get the `hard_negative` tag; header/footer identifiers elsewhere are labeled but don't set it.
"""

from __future__ import annotations

import random
from collections.abc import Callable
from datetime import date
from pathlib import Path

import yaml

from bench.generate import providers as pv
from bench.generate.render import DocCtx
from bench.generate.world import Study

# eponyms by the context they make sense in (audit J4: "renal function uses the Hodgkin formula"
# would make hard negatives easy to spot)
EPONYM_POOLS: dict[str, tuple[str, ...]] = {
    "tte": ("Kaplan-Meier",),
    "renal": ("Cockcroft-Gault",),
    "rank": ("Wilcoxon", "Mann-Whitney"),
    "exact": ("Fisher",),
    "correction": ("Bonferroni", "Holm"),
    "stratified": ("Mantel-Haenszel",),
    "agreement": ("Bland-Altman",),
    "disease": ("Hodgkin",),
}


def cas_like(r: random.Random) -> str:
    """CAS-format number with a deliberately wrong check digit: can't name a real substance."""
    body = f"{r.randint(1000, 99999)}{r.randint(10, 99)}"
    check = sum((i + 1) * int(d) for i, d in enumerate(reversed(body))) % 10
    return f"{body[:-2]}-{body[-2:]}-{(check + 1 + r.randint(0, 8)) % 10}"


def meddra_like(r: random.Random) -> str:
    return f"10{r.randint(0, 999999):06d}"


def visit_window(r: random.Random) -> str:
    return f"Day {r.choice((8, 15, 29, 57, 85))} ±{r.choice((1, 2, 3))}"


def dose(r: random.Random) -> str:
    return f"{r.choice((25, 50, 100, 150, 200))} mg"


def ref_range(r: random.Random) -> str:
    lo = r.randint(1, 60)
    return f"{lo}-{lo + r.randint(20, 90)}"


def _pick(pool: tuple[str, ...]) -> Callable[[random.Random, Study, date], str]:
    return lambda r, st, d: r.choice(pool)


# sentence templates: {field} -> (value factory, negative kind)
Factory = Callable[[random.Random, Study, date], str]
FIELDS: dict[str, tuple[Factory, str]] = {
    "protocol": (lambda r, st, d: st.protocol_no, "protocol_no"),
    "nct": (lambda r, st, d: st.nct, "nct_id"),
    "eudract": (lambda r, st, d: st.eudract, "eudract_no"),
    "compound": (lambda r, st, d: st.compound, "compound_code"),
    "amendment": (lambda r, st, d: f"A{r.randint(1, 6)}", "amendment_no"),
    "lot": (lambda r, st, d: pv.lot_no(r), "lot_no"),
    "kit": (lambda r, st, d: pv.kit_no(r), "kit_no"),
    "cas": (lambda r, st, d: cas_like(r), "cas_no"),
    "meddra": (lambda r, st, d: meddra_like(r), "meddra_code"),
    "window": (lambda r, st, d: visit_window(r), "visit_window"),
    "dose": (lambda r, st, d: dose(r), "dose"),
    "range": (lambda r, st, d: ref_range(r), "reference_range"),
    **{f"ep_{ctx}": (_pick(pool), "eponym") for ctx, pool in EPONYM_POOLS.items()},
    "date": (lambda r, st, d: "", "non_phi_date"),  # filled by ctx.doc_date
}
SENTENCES: dict[str, list[str]] = yaml.safe_load(
    (Path(__file__).parent / "data" / "hard_negative_sentences.yaml").read_text(encoding="utf-8")
)


def block(ctx: DocCtx, study: Study, free_date: date, n: int = 3) -> str:
    """A paragraph of `n` hard-negative sentences, as raw text with `neg()` sentinels.

    `free_date` must not coincide with any referenced subject's date (see documents.safe_date).
    """
    r = ctx.rng
    sentences = SENTENCES.get(ctx.lang, SENTENCES["en"])
    out: list[str] = []
    for s in r.sample(sentences, min(n, len(sentences))):
        fields: dict[str, str] = {}
        for name, (factory, kind) in FIELDS.items():
            if "{" + name + "}" in s:
                fields[name] = (
                    ctx.doc_date(free_date)
                    if name == "date"
                    else ctx.neg(factory(r, study, free_date), kind)
                )
        out.append(s.format(**fields))
    return " ".join(out)
