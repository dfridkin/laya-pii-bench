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
