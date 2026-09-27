"""4g: corpus planning exactness, validators on a generated sample, determinism."""

from collections import Counter
from pathlib import Path

import pytest

from bench.config import load_gen_spec, load_policy
from bench.domain import LengthBucket
from bench.generate import corpus
from bench.generate import world as W
from bench.generate.render import template_vocabulary

ROOT = Path(__file__).resolve().parents[2]
SPEC = load_gen_spec(ROOT / "config" / "gen_spec.yaml")
POLICY = load_policy(ROOT / "config" / "policy.yaml")


def words(text: str) -> int:
    return len(text.split())


@pytest.fixture(scope="module")
def slots() -> list[corpus.Slot]:
    return corpus.plan(SPEC, W.build(SPEC, frozenset(template_vocabulary())))


def test_plan_realizes_exact_counts(slots: list[corpus.Slot]) -> None:
    assert Counter(s.doc_type for s in slots) == SPEC.doc_types
    assert Counter(s.lang for s in slots) == SPEC.lang_counts
    assert Counter(s.bucket for s in slots) == SPEC.bucket_counts
    assert sum(s.hard_negative for s in slots) == SPEC.hard_negative_count
    assert sum(s.depth is not None for s in slots) == SPEC.pii_depth_docs
    n = len(slots)
    p = SPEC.perturbations
    post = Counter(x.split(":")[0] for s in slots for x in s.post)
    assert post == {"line_wrap": round(n * p.line_wrap), "table": round(n * p.table),
                    "ocr_noise": round(n * p.ocr_noise)}  # fmt: skip
    assert sum(s.headers_footers for s in slots) == round(n * p.headers_footers)


def test_plan_respects_doc_plan(slots: list[corpus.Slot]) -> None:
    for s in slots:
        entry = SPEC.doc_plan[s.doc_type]
        assert s.bucket in entry.buckets and s.lang in entry.langs
        assert (s.site is None) == (entry.level == "sponsor")
        if s.lang != "en":
            assert s.site is not None and s.site.lang == s.lang and s.bucket is LengthBucket.SHORT
        if s.depth:
            assert (
                s.mode == "normal"
                and s.lang == "en"
                and s.bucket in (LengthBucket.LONG, LengthBucket.XL)
            )
        if s.mode == "normal" and entry.pii.any:
            assert s.enabled
        assert all(getattr(entry.pii, c.value) > 0 for c in s.enabled)
    clean = sum(s.mode != "normal" for s in slots)
    assert clean == sum(round(n * SPEC.doc_plan[t].clean_rate) for t, n in SPEC.doc_types.items())


def test_irb_holdout_and_staff_only_types_carry_no_patient_data(slots: list[corpus.Slot]) -> None:
    for s in slots:
        if s.doc_type.value in ("irb_letter", "delegation_log"):
            assert {c.value for c in s.enabled} <= {"staff_pii"}


def test_sample_generates_cleanly_and_deterministically() -> None:
    sample = list(range(0, 600, 37))  # 17 docs across types and buckets
    a = corpus.generate(SPEC, POLICY, words, only=sample)
    assert a.problems == {}
    b = corpus.generate(SPEC, POLICY, words, only=sample)
    assert [d.model_dump_json() for d in a.docs] == [d.model_dump_json() for d in b.docs]


@pytest.fixture(scope="module")
def sample_docs() -> list:  # type: ignore[type-arg]
    from bench.domain import DocType

    slots_ = corpus.plan(SPEC, W.build(SPEC, frozenset(template_vocabulary())))
    wanted = [s.idx for s in slots_ if s.doc_type in (DocType.SAE, DocType.ICF, DocType.SITE_EMAIL)
              or s.lang != "en"][:80]  # fmt: skip
    return corpus.generate(SPEC, POLICY, words, only=wanted).docs


def test_sae_forms_report_real_adverse_events(sample_docs: list) -> None:  # type: ignore[type-arg]
    """Audit J2: no invented AEs; the reported onset is one of the subject's world AE onsets."""
    from bench.generate.variants import date_forms

    world = W.build(SPEC, frozenset(template_vocabulary()))
    subjects = {s.subject_id: s for site in world.sites() for s in site.subjects}
    for d in (
        x for x in sample_docs if x.doc_type.value == "sae_cioms" and x.gen_meta["mode"] == "normal"
    ):
        sub = subjects[d.world_refs.subjects[0]]
        assert sub.aes
        ae_dates = {
            f for ae in sub.aes for x in (ae.onset, ae.resolved) if x for f in date_forms(x)
        }
        event_dates = [s.value for s in d.spans if s.value_kind == "event_date"]
        # every event date on the form is one of this subject's real AE dates (partial redaction
        # may remove the onset, so no positional assumption)
        assert all(v in ae_dates for v in event_dates), (d.id, event_dates)


def test_non_english_docs_are_native_only(sample_docs: list) -> None:  # type: ignore[type-arg]
    """Audit J6: no English filler sections or English AE terms in de/es/pl docs."""
    from bench.generate import filler
    from bench.generate.world import AE_TERMS

    titles = {t for topic in filler.TOPICS for t in filler._GRAMMAR[topic]["titles"]}  # pyright: ignore[reportPrivateUsage]
    for d in (x for x in sample_docs if x.lang != "en"):
        assert not any(t in d.text for t in titles), d.id
        assert not any(f" {term} " in d.text or f"({term}," in d.text for term in AE_TERMS
                       if term not in ("neutropenia",)), d.id  # fmt: skip


def test_document_dates_follow_the_events(sample_docs: list) -> None:  # type: ignore[type-arg]
    """Audit J3: SAE report after onset; ICF version dated before the signature."""
    from datetime import date, timedelta

    from bench.generate.variants import date_forms

    parse: dict[str, date] = {}
    d0 = date(2024, 6, 1)
    for k in range(900):
        d = d0 + timedelta(days=k)
        for f in date_forms(d):
            parse.setdefault(f, d)  # ambiguous forms keep the first; checked docs avoid them
    checked = 0
    for d in sample_docs:
        if d.gen_meta["mode"] != "normal":
            continue
        doc_dates = [
            parse[n.value] for n in d.negatives if n.kind == "non_phi_date" and n.value in parse
        ]
        ev = [parse[s.value] for s in d.spans if s.value_kind == "event_date" and s.value in parse]
        if d.doc_type.value == "sae_cioms" and doc_dates and ev:
            assert doc_dates[-1] > ev[0], d.id  # report date (last) after onset (first event)
            checked += 1
        if d.doc_type.value == "icf_signature_page" and doc_dates and ev:
            assert doc_dates[0] < ev[0], d.id  # version date before signature date
            checked += 1
    assert checked >= 5


def test_depth_subject_dates_are_avoided_by_document_dates() -> None:
    """Regression (d0371): the depth subject is added after the view picks its document dates;
    those dates must still avoid every rendered form of the depth subject's dates."""
    from bench.generate.checks import subject_dates

    world = W.build(SPEC, frozenset(template_vocabulary()))
    slots_ = corpus.plan(SPEC, world)
    depth = [s.idx for s in slots_ if s.depth is not None]
    result = corpus.generate(SPEC, POLICY, words, only=[371, *depth[:12]])
    assert result.problems == {}
    subjects = {s.subject_id: s for site in world.sites() for s in site.subjects}
    for d in result.docs:
        if d.pii_depth is None:
            continue
        taken = {f for sid in d.world_refs.subjects for f, _ in subject_dates(subjects[sid])}
        assert not any(n.value in taken for n in d.negatives if n.kind == "non_phi_date"), d.id


@pytest.fixture(scope="module")
def world_and_docs() -> tuple:  # type: ignore[type-arg]
    from bench.domain import DocType

    world = W.build(SPEC, frozenset(template_vocabulary()))
    slots_ = corpus.plan(SPEC, world)
    want = [
        *[s.idx for s in slots_ if s.doc_type in (DocType.CRF, DocType.DEVIATION)][:16],
        *[s.idx for s in slots_ if s.partial_redact][:12],
        *[s.idx for s in slots_ if s.lang != "en" and s.headers_footers][:6],
    ]
    return world, corpus.generate(SPEC, POLICY, words, only=sorted(set(want))).docs


def test_logs_use_only_world_facts(world_and_docs: tuple) -> None:  # type: ignore[type-arg]
    """N2: deviation rows are world deviations; N3: CRF rows are distinct (subject, visit)."""
    from bench.generate.variants import date_forms

    world, docs = world_and_docs
    subjects = {s.subject_id: s for site in world.sites() for s in site.subjects}
    for d in docs:
        if d.doc_type.value == "deviation_log":
            refs = [subjects[x] for x in d.world_refs.subjects]
            dev_dates = {f for s in refs for dv in s.deviations for f in date_forms(dv.on)}
            for sp in d.spans:
                if sp.value_kind == "event_date" and "ocr_noise" not in d.tags:
                    assert sp.value in dev_dates, (d.id, sp.value)


def test_crf_rows_are_distinct_subject_visits(world_and_docs: tuple) -> None:  # type: ignore[type-arg]
    """N3: CRF rows are sampled without replacement over (subject, visit)."""
    from bench.domain import DocType, PiiCategory
    from bench.generate.documents import VIEWS, ViewRequest
    from bench.generate.render import DocCtx
    from bench.generate.seeds import rng

    world, _ = world_and_docs
    for k, site in enumerate(world.sites()):
        r = rng(3, "crf", k)
        ctx = DocCtx(lang="en", rng=r, enabled=frozenset(PiiCategory))
        req = ViewRequest(DocType.CRF, "en", world.study_of(site), site, None, "normal",
                          frozenset(PiiCategory), r, {"rows": 60})  # fmt: skip
        _, data, _ = VIEWS[DocType.CRF](req, ctx)
        keys = [(row["sub"].subject_id, row["visit"]) for row in data["rows"]]
        assert len(keys) == len(set(keys)) == 60


def test_partial_redaction_mixes_placeholders_with_pii(world_and_docs: tuple) -> None:  # type: ignore[type-arg]
    """N5: pre-redaction placeholders also occur in PII-bearing documents."""
    _, docs = world_and_docs
    partial = [d for d in docs if d.gen_meta.get("partial_redact") == 1]
    assert partial
    mixed = [d for d in partial if d.spans and any(n.kind == "pre_redacted" for n in d.negatives)]
    assert len(mixed) >= len(partial) // 2
    assert all("pre_redacted" in d.tags for d in mixed)


def test_headers_are_localized(world_and_docs: tuple) -> None:  # type: ignore[type-arg]
    """N6: running header/footer in the document's language."""
    _, docs = world_and_docs
    for d in docs:
        if d.lang != "en" and "headers_footers" in d.tags:
            assert "Confidential" not in d.text and "Page " not in d.text, d.id
