"""4e: length buckets, filler, PII depth."""

from pathlib import Path

import pytest

from bench.config import load_gen_spec, load_policy
from bench.domain import DocType, LengthBucket, PiiCategory, PiiDepth
from bench.generate import checks, filler
from bench.generate import world as W
from bench.generate.assemble import DocSpec, assemble, realized_depth_of
from bench.generate.documents import SUBJECT_TYPES
from bench.generate.render import template_vocabulary

ROOT = Path(__file__).resolve().parents[2]
SPEC = load_gen_spec(ROOT / "config" / "gen_spec.yaml")
POLICY = load_policy(ROOT / "config" / "policy.yaml")


def words(text: str) -> int:  # stand-in token counter for fast tests
    return len(text.split())


@pytest.fixture(scope="module")
def world() -> W.World:
    return W.build(SPEC, frozenset(template_vocabulary()))


@pytest.fixture(scope="module")
def scanner(world: W.World) -> checks.Scanner:
    return checks.Scanner(world)


def spec_for(world: W.World, t: DocType, bucket: LengthBucket, k: int, **kw: object) -> DocSpec:
    plan = SPEC.doc_plan[t]
    site = world.sites()[k % len(world.sites())]
    sponsor = plan.level == "sponsor"
    cats = frozenset(c for c in PiiCategory if getattr(plan.pii, c.value) > 0)
    base: dict[str, object] = dict(
        doc_id=f"{t.value}-{bucket.value}-{k}", doc_type=t, lang="en", bucket=bucket,
        study=world.study_of(site), site=None if sponsor else site,
        subject=site.subjects[k % 15] if t in SUBJECT_TYPES or kw.get("pii_depth") else None,
        mode="clean" if sponsor else "normal", enabled=cats,
    )  # fmt: skip
    return DocSpec(**(base | kw))  # type: ignore[arg-type]


def test_filler_is_clean_and_varied() -> None:
    import random

    r = random.Random(3)
    paras = {filler.paragraph(r, t) for t in filler.TOPICS for _ in range(20)}
    assert len(paras) > 100
    assert not any("{" in p or "}" in p for p in paras)


@pytest.mark.parametrize("t", list(DocType), ids=lambda t: t.value)
def test_every_type_hits_every_allowed_bucket(t: DocType, world: W.World,
                                              scanner: checks.Scanner) -> None:  # fmt: skip
    for k, bucket in enumerate(SPEC.doc_plan[t].buckets):
        doc = assemble(spec_for(world, t, bucket, k), SPEC, words)
        lo, hi = SPEC.length_tokens[bucket]
        assert lo <= words(doc.text) <= hi, (t, bucket, words(doc.text))
        assert doc.length_bucket is bucket
        assert checks.check(doc, POLICY, scanner) == [], (t, bucket)
        assert len(doc.gen_meta["sections"]) >= 1  # type: ignore[arg-type]


@pytest.mark.parametrize("depth", list(PiiDepth), ids=lambda d: d.value)
def test_depth_docs_place_one_pii_block_in_band(depth: PiiDepth, world: W.World,
                                                scanner: checks.Scanner) -> None:  # fmt: skip
    lo_f, hi_f = SPEC.pii_depth_positions[depth]
    for k, t in enumerate((DocType.NARRATIVE, DocType.MONITORING, DocType.SITE_EMAIL)):
        for bucket in (LengthBucket.LONG, LengthBucket.XL):
            doc = assemble(spec_for(world, t, bucket, k, pii_depth=depth), SPEC, words)
            assert doc.pii_depth is depth
            assert lo_f <= realized_depth_of(doc, words) <= hi_f
            span_zone = max(s.end for s in doc.spans) - min(s.start for s in doc.spans)
            assert span_zone < 300  # one compact block, not scattered PII
            assert checks.check(doc, POLICY, scanner) == []


def test_assembly_is_deterministic(world: W.World) -> None:
    ds = spec_for(world, DocType.MONITORING, LengthBucket.LONG, 3, hard_negative=True)
    a, b = assemble(ds, SPEC, words), assemble(ds, SPEC, words)
    assert a == b and "hard_negative" in a.tags


@pytest.mark.model
def test_real_tokenizer_xl_exceeds_8192(world: W.World) -> None:
    from bench import tokenize

    tok = tokenize.load("multilingual", ROOT / "models.lock.json")

    def count(text: str) -> int:
        return len(tok(text))

    doc = assemble(spec_for(world, DocType.PROTOCOL, LengthBucket.XL, 1), SPEC, count)
    assert 8200 <= count(doc.text) <= 11000 and doc.gen_meta["tokens_multilingual"] == count(
        doc.text
    )
    short = assemble(spec_for(world, DocType.ICF, LengthBucket.SHORT, 2), SPEC, count)
    assert 120 <= count(short.text) <= 1000
