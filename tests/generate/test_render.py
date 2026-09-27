"""4b: sentinel renderer, V1/V2, narrative + protocol templates."""

from pathlib import Path

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from bench.config import load_gen_spec, load_policy
from bench.domain import DocType, Document, PiiCategory
from bench.generate import checks
from bench.generate import world as W
from bench.generate.documents import ViewRequest, build
from bench.generate.render import RenderError, Slot, resolve, template_vocabulary
from bench.generate.seeds import rng

ROOT = Path(__file__).resolve().parents[2]
SPEC = load_gen_spec(ROOT / "config" / "gen_spec.yaml")
POLICY = load_policy(ROOT / "config" / "policy.yaml")
ALL = frozenset(PiiCategory)


@pytest.fixture(scope="module")
def world() -> W.World:
    return W.build(SPEC, frozenset(template_vocabulary()))


@pytest.fixture(scope="module")
def scanner(world: W.World) -> checks.Scanner:
    return checks.Scanner(world)


# --- resolve (gate 4: >= 500 examples) -----------------------------------------------------------

text = st.text(
    alphabet=st.characters(blacklist_characters="⟦⟧", blacklist_categories=("Cs",)), max_size=25
)
value = text.filter(bool)


@settings(max_examples=600)
@given(st.lists(st.tuples(text, st.sampled_from("snh"), value), max_size=10), text)
def test_resolve_offsets_point_at_values(parts: list[tuple[str, str, str]], tail: str) -> None:
    slots: list[Slot] = []
    negs: list[Slot] = []
    heads: list[str] = []
    raw = ""
    for lit, kind, v in parts:
        if kind == "s":
            slots.append(Slot(v, {"category": "phi_direct", "role": "patient",
                                  "value_kind": "k", "surface": "x"}))  # fmt: skip
            raw += lit + f"⟦s{len(slots) - 1}⟧"
        elif kind == "n":
            negs.append(Slot(v, {"kind": "lot_no"}))
            raw += lit + f"⟦n{len(negs) - 1}⟧"
        else:
            heads.append(v)
            raw += lit + f"⟦h{len(heads) - 1}⟧"
    out = resolve(raw + tail, slots, negs, heads)
    assert out.text == "".join(lit + v for lit, _, v in parts) + tail
    assert [out.text[s.start : s.end] for s in out.spans] == [s.value for s in slots]
    assert [s.value for s in out.spans] == [s.value for s in slots]
    assert [out.text[n.start : n.end] for n in out.negatives] == [n.value for n in negs]
    assert [out.text[p : p + len(h)] for p, h in zip(out.sections, heads, strict=True)] == heads


def test_unresolved_sentinel_is_an_error() -> None:
    with pytest.raises(RenderError):
        resolve("text ⟦s0", [], [], [])


# --- templates through V1 + V2 -------------------------------------------------------------------


def narrative(world: W.World, site: W.Site, sub: W.Subject, mode: str = "normal",
              enabled: frozenset[PiiCategory] = ALL) -> Document:  # fmt: skip
    req = ViewRequest(DocType.NARRATIVE, site.lang, world.study_of(site), site, sub,
                      mode, enabled, rng(1, "t", sub.subject_id, mode))  # type: ignore[arg-type]  # fmt: skip
    return build(f"t-{sub.subject_id}", req)


def test_every_subject_narrative_passes_v1_v2(world: W.World, scanner: checks.Scanner) -> None:
    n = 0
    for site in world.sites():
        for sub in site.subjects:
            doc = narrative(world, site, sub)
            assert checks.check(doc, POLICY, scanner) == [], doc.text
            assert {s.category for s in doc.spans} == set(PiiCategory)
            n += 1
    assert n == 360


def test_languages_render(world: W.World) -> None:
    langs = {s.lang: s for s in world.sites()}
    assert set(langs) == {"en", "de", "es", "pl"}
    de = narrative(world, langs["de"], langs["de"].subjects[0])
    assert "Patientennarrativ" in de.text and de.lang == "de"


def test_clean_and_redacted_modes(world: W.World, scanner: checks.Scanner) -> None:
    site = world.sites()[0]
    sub = site.subjects[0]
    clean = narrative(world, site, sub, "clean")
    assert clean.spans == [] and checks.check(clean, POLICY, scanner) == []
    red = narrative(world, site, sub, "redacted")
    assert red.spans == [] and "pre_redacted" in red.tags
    assert {n.kind for n in red.negatives} >= {"pre_redacted", "protocol_no"}
    assert checks.check(red, POLICY, scanner) == []


def test_category_gating(world: W.World, scanner: checks.Scanner) -> None:
    site = world.sites()[1]
    only_coded = narrative(world, site, site.subjects[2], enabled=frozenset({PiiCategory.CODED_ID}))
    assert {s.category for s in only_coded.spans} == {PiiCategory.CODED_ID}
    assert checks.check(only_coded, POLICY, scanner) == []


def test_protocol_is_person_free(world: W.World, scanner: checks.Scanner) -> None:
    for i, study in enumerate(world.studies):
        for k in range(6):
            req = ViewRequest(DocType.PROTOCOL, "en", study, None, None, "clean", frozenset(),
                              rng(1, "p", i, k))  # fmt: skip
            doc = build(f"p{i}{k}", req)
            assert doc.spans == [] and doc.negatives
            assert doc.world_refs.site == "SPONSOR" and doc.world_refs.subjects == []
            assert checks.check(doc, POLICY, scanner) == []
            assert doc.gen_meta["sections"]


def test_v2_catches_an_unlabeled_name(world: W.World, scanner: checks.Scanner) -> None:
    site = world.sites()[3]
    p = site.staff["coordinator"]
    doc = Document.model_validate({
        "id": "leak", "doc_type": "site_correspondence", "lang": "en",
        "text": f"Please ask {p.given} {p.family} or {p.email} to confirm.",
        "spans": [], "negatives": [], "tags": [], "length_bucket": "short", "pii_depth": None,
        "world_refs": {"study": site.study, "site": site.site_no, "subjects": []}, "gen_meta": {},
    })  # fmt: skip
    problems = scanner.unlabeled(doc)
    assert any("name of" in x for x in problems) and any("contact of" in x for x in problems)


def test_v2_catches_a_referenced_subjects_unlabeled_date(
    world: W.World, scanner: checks.Scanner
) -> None:
    from bench.generate.variants import fmt_date

    site = world.sites()[0]
    sub = site.subjects[0]
    doc = Document.model_validate({
        "id": "leak2", "doc_type": "crf_page", "lang": "en",
        "text": f"Visit on {fmt_date(sub.visits[1], 'iso')} completed.",
        "spans": [], "negatives": [], "tags": [], "length_bucket": "short", "pii_depth": None,
        "world_refs": {"study": site.study, "site": site.site_no, "subjects": [sub.subject_id]},
        "gen_meta": {},
    })  # fmt: skip
    assert any("date of" in x for x in scanner.unlabeled(doc))


def test_v1_catches_value_mismatch(world: W.World) -> None:
    site = world.sites()[0]
    doc = narrative(world, site, site.subjects[0])
    wrong = doc.spans[0].model_copy(update={"value": "nope"})
    bad = doc.model_copy(update={"spans": [wrong, *doc.spans[1:]]})
    assert any(p.startswith("V1") for p in checks.v1(bad, POLICY))


def test_world_names_avoid_template_vocabulary(world: W.World) -> None:
    vocab = template_vocabulary()
    for p in world.persons():
        assert p.given.lower() not in vocab and p.family.lower() not in vocab
