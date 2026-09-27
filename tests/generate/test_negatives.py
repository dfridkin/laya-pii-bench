"""4d: hard-negative registry and injector."""

from pathlib import Path

import pytest

from bench.config import load_gen_spec, load_policy
from bench.domain import DocType, PiiCategory
from bench.generate import checks, negatives
from bench.generate import world as W
from bench.generate.documents import SUBJECT_TYPES, ViewRequest, build, subject_date_set
from bench.generate.render import template_vocabulary
from bench.generate.seeds import rng
from bench.generate.variants import date_forms

ROOT = Path(__file__).resolve().parents[2]
SPEC = load_gen_spec(ROOT / "config" / "gen_spec.yaml")
POLICY = load_policy(ROOT / "config" / "policy.yaml")


@pytest.fixture(scope="module")
def world() -> W.World:
    return W.build(SPEC, frozenset(template_vocabulary()))


@pytest.fixture(scope="module")
def scanner(world: W.World) -> checks.Scanner:
    return checks.Scanner(world)


def test_cas_like_never_has_a_valid_check_digit() -> None:
    for k in range(2000):
        cas = negatives.cas_like(rng(1, "cas", k))
        a, b, c = cas.split("-")
        digits = a + b
        valid = sum((i + 1) * int(d) for i, d in enumerate(reversed(digits))) % 10
        assert int(c) != valid


def test_every_sentence_field_is_registered() -> None:
    import re

    for lang, sentences in negatives.SENTENCES.items():
        for s in sentences:
            assert set(re.findall(r"\{(\w+)\}", s)) <= set(negatives.FIELDS), (lang, s)


@pytest.mark.parametrize("t", list(DocType), ids=lambda t: t.value)
def test_injected_docs_pass_and_are_tagged(t: DocType, world: W.World,
                                           scanner: checks.Scanner) -> None:  # fmt: skip
    kinds: set[str] = set()
    for k, site in enumerate(world.sites()[:8]):
        plan = SPEC.doc_plan[t]
        lang = site.lang if site.lang in plan.langs else "en"
        r = rng(9, "neg", t.value, k)
        sub = r.choice(site.subjects) if t in SUBJECT_TYPES else None
        cats = frozenset(c for c in PiiCategory if getattr(plan.pii, c.value) > 0)
        mode = "clean" if plan.level == "sponsor" else "normal"
        req = ViewRequest(t, lang, world.study_of(site), None if plan.level == "sponsor" else site,  # type: ignore[arg-type]
                          sub, mode, cats, r, {"hard_negative": True})  # type: ignore[arg-type]  # fmt: skip
        doc = build(f"n{k}", req)
        assert "hard_negative" in doc.tags
        assert checks.check(doc, POLICY, scanner) == [], doc.text
        kinds |= {n.kind for n in doc.negatives}
        # negative dates share no rendered form with a referenced subject's dates
        refs = [s for s in site.subjects if s.subject_id in doc.world_refs.subjects]
        taken = {f for d in subject_date_set(refs) for f in date_forms(d)}
        assert not any(n.value in taken for n in doc.negatives if n.kind == "non_phi_date")
    assert {"protocol_no", "nct_id", "eudract_no"} & kinds


def test_safe_date_avoids_ambiguous_day_month_order(world: W.World) -> None:
    from datetime import date

    from bench.generate.documents import safe_date

    sub = world.sites()[0].subjects[0]
    real = next(d for d in [sub.enrolled, *sub.visits] if d.day <= 12 and d.day != d.month)
    swapped = date(real.year, real.day, real.month)  # 07/08 read the other way round
    taken = {f for d in subject_date_set([sub]) for f in date_forms(d)}
    assert set(date_forms(swapped)) & taken  # the ambiguity is real
    with pytest.raises(RuntimeError):  # the only candidate is ambiguous: refused
        safe_date(rng(5, "safe"), [sub], lo=swapped, span_days=0)
    for k in range(300):
        assert not set(date_forms(safe_date(rng(5, "safe", k), [sub]))) & taken
