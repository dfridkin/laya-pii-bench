import re
from collections import Counter
from pathlib import Path

import pytest

from bench.config import load_gen_spec
from bench.domain import SubjectRole
from bench.generate import world as W

ROOT = Path(__file__).resolve().parents[2]
SPEC = load_gen_spec(ROOT / "config" / "gen_spec.yaml")


@pytest.fixture(scope="module")
def world() -> W.World:
    return W.build(SPEC)


def test_deterministic(world: W.World) -> None:
    assert W.build(SPEC).model_dump_json() == world.model_dump_json()


def test_shape(world: W.World) -> None:
    assert len(world.studies) == 3
    sites = world.sites()
    n_sites = SPEC.world.studies * SPEC.world.sites_per_study
    assert len(sites) == n_sites
    assert sum(len(s.subjects) for s in sites) == n_sites * SPEC.world.subjects_per_site
    assert Counter(s.lang for s in sites) == SPEC.world.site_locales


def test_site_keys_unique_and_study_scoped(world: W.World) -> None:
    keys = [s.key for s in world.sites()]
    assert len(set(keys)) == len(keys)
    for st in world.studies:
        nos = [s.site_no for s in st.sites]
        assert len(set(nos)) == len(nos)
        assert all(s.key == f"{st.protocol_no}/{s.site_no}" for s in st.sites)


def test_people_unique_and_single_site(world: W.World) -> None:
    people = world.persons()
    assert len({p.id for p in people}) == len(people)
    assert len({p.family for p in people}) == len(people)  # unique family names (V2)
    for s in world.sites():  # each person's id is scoped to exactly one site (D-018)
        ids = [p.id for p in s.staff.values()] + [x.person.id for x in s.subjects]
        assert all(i.startswith(s.key + "/") for i in ids)
    assert {p.role for p in people} == {SubjectRole.PATIENT, SubjectRole.STAFF, SubjectRole.SPONSOR}


def test_places_never_reuse_person_names(world: W.World) -> None:
    families = {p.family for p in world.persons()}
    assert min(len(f) for f in families) >= 3
    for s in world.sites():
        words = set(re.findall(r"\w+", f"{s.institution} {s.city}"))
        assert not words & families


def test_subject_timelines_consistent(world: W.World) -> None:
    ages = []
    for s in world.sites():
        for sub in s.subjects:
            ages.append(sub.age)
            assert sub.visits == sorted(sub.visits) and sub.visits[0] == sub.enrolled
            assert sub.subject_id.startswith(s.site_no + "-")
            for ae in sub.aes:
                assert ae.onset > sub.enrolled
                assert ae.resolved is None or ae.resolved > ae.onset
            for cm in sub.conmeds:
                assert cm.stop is None or cm.stop > cm.start
    assert min(ages) >= 18 and max(ages) <= 95
    assert any(a > 89 for a in ages)  # the age > 89 quasi-identifier edge case exists


def test_fictional_identifiers(world: W.World) -> None:
    for st in world.studies:
        assert st.nct.startswith("NCT99") and st.eudract.startswith("2031-")
        assert st.compound.startswith("FTX-") and st.protocol_no.startswith(st.compound)
    for p in world.persons():
        assert p.phone is None or "555" in p.phone
        assert p.email is None or p.email.endswith((".example.org", ".example.com"))


def test_no_place_name_echoes_an_atrocity_site() -> None:
    world = W.build(SPEC, frozenset())
    places = {s.city for s in world.sites()} | {s.institution for s in world.sites()}
    assert not any(b in p.lower() for p in places for b in W.BLOCKED_PLACES)
