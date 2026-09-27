"""4c: every doc type x site x mode renders cleanly through V1 + V2."""

from pathlib import Path

import pytest

from bench.config import load_gen_spec, load_policy
from bench.domain import DocType, Document, PiiCategory, SubjectRole
from bench.generate import checks
from bench.generate import world as W
from bench.generate.documents import SUBJECT_TYPES, VIEWS, ViewRequest, build
from bench.generate.render import template_names, template_vocabulary
from bench.generate.seeds import rng

ROOT = Path(__file__).resolve().parents[2]
SPEC = load_gen_spec(ROOT / "config" / "gen_spec.yaml")
POLICY = load_policy(ROOT / "config" / "policy.yaml")
SITE_TYPES = [t for t in DocType if SPEC.doc_plan[t].level == "site"]


@pytest.fixture(scope="module")
def world() -> W.World:
    return W.build(SPEC, frozenset(template_vocabulary()))


@pytest.fixture(scope="module")
def scanner(world: W.World) -> checks.Scanner:
    return checks.Scanner(world)


def make(world: W.World, t: DocType, site: W.Site, mode: str, enabled: frozenset[PiiCategory],
         k: int) -> Document:  # fmt: skip
    lang = site.lang if site.lang in SPEC.doc_plan[t].langs else "en"
    r = rng(7, "tpl", t.value, site.key, mode, k)
    sub = r.choice(site.subjects) if t in SUBJECT_TYPES else None
    req = ViewRequest(t, lang, world.study_of(site), site, sub, mode, enabled, r)  # type: ignore[arg-type]
    return build(f"{t.value}-{k}", req)


def test_every_type_has_a_view_and_templates() -> None:
    assert set(VIEWS) == set(DocType)
    names = set(template_names())
    for t in DocType:
        for lang in SPEC.doc_plan[t].langs:
            assert f"{t.value}/{lang}.j2" in names, (t, lang)


@pytest.mark.parametrize("t", SITE_TYPES, ids=lambda t: t.value)
def test_site_types_pass_v1_v2(t: DocType, world: W.World, scanner: checks.Scanner) -> None:
    profile = SPEC.doc_plan[t].pii
    cats = [c for c in PiiCategory if getattr(profile, c.value) > 0]
    for k, site in enumerate(world.sites()):
        r = rng(7, "subset", t.value, k)
        subset = frozenset(c for c in cats if r.random() < 0.6) or frozenset(cats[:1])
        for mode, enabled in (("normal", frozenset(cats)), ("normal", subset),
                              ("clean", frozenset()), ("redacted", frozenset())):  # fmt: skip
            doc = make(world, t, site, mode, enabled, k)
            problems = checks.check(doc, POLICY, scanner)
            assert problems == [], (t, site.key, mode, problems[:3], doc.text[:400])
            assert {s.category for s in doc.spans} <= enabled
            if mode != "normal":
                assert doc.spans == []
            if t is DocType.IRB:  # holdout: no subjects (D-005)
                assert doc.world_refs.subjects == []
                assert all(s.role is not SubjectRole.PATIENT for s in doc.spans)
            if t is DocType.DELEGATION:
                assert {s.category for s in doc.spans} <= {PiiCategory.STAFF_PII}


def test_full_profile_yields_every_enabled_category(world: W.World) -> None:
    site = world.sites()[0]
    missing: dict[DocType, frozenset[PiiCategory]] = {}
    for t in SITE_TYPES:
        profile = SPEC.doc_plan[t].pii
        cats = frozenset(c for c in PiiCategory if getattr(profile, c.value) > 0)
        seen: set[PiiCategory] = set()
        for k in range(8):
            seen |= {s.category for s in make(world, t, site, "normal", cats, 100 + k).spans}
        missing.update({t: cats - seen} if seen != cats else {})
    assert missing == {}


def test_sponsor_role_and_cra_labels(world: W.World) -> None:
    site = world.sites()[0]
    roles = set()
    for k in range(30):
        doc = make(world, DocType.SITE_EMAIL, site, "normal", frozenset(PiiCategory), k)
        roles |= {(s.category, s.role) for s in doc.spans if s.category is PiiCategory.STAFF_PII}
    assert (PiiCategory.STAFF_PII, SubjectRole.SPONSOR) in roles  # D-017
    assert (PiiCategory.STAFF_PII, SubjectRole.STAFF) in roles
