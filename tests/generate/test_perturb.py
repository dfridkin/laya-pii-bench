"""4f: perturbations and span remap (gate 4: remap hypothesis test >= 500 examples)."""

import random
from pathlib import Path

import pytest
from hypothesis import assume, given, settings
from hypothesis import strategies as st

from bench.config import load_gen_spec, load_policy
from bench.domain import DocType, Document, LengthBucket, PiiCategory
from bench.generate import checks, perturb
from bench.generate import world as W
from bench.generate.assemble import DocSpec, assemble
from bench.generate.documents import SUBJECT_TYPES
from bench.generate.perturb import Edit, RemapError
from bench.generate.render import template_vocabulary

ROOT = Path(__file__).resolve().parents[2]
SPEC = load_gen_spec(ROOT / "config" / "gen_spec.yaml")
POLICY = load_policy(ROOT / "config" / "policy.yaml")


def doc_with(text: str, spans: list[tuple[int, int]]) -> Document:
    return Document.model_validate({
        "id": "d", "doc_type": "crf_page", "lang": "en", "text": text,
        "spans": [{"start": a, "end": b, "category": "phi_direct", "role": "patient",
                   "value_kind": "k", "surface": "s", "value": text[a:b]} for a, b in spans],
        "negatives": [],
        "tags": [], "length_bucket": "short", "pii_depth": None,
        "world_refs": {"study": "s", "site": "1", "subjects": []}, "gen_meta": {"sections": [0]},
    })  # fmt: skip


# --- remap property ------------------------------------------------------------------------------


@st.composite
def case(draw: st.DrawFn) -> tuple[str, list[tuple[int, int]], list[Edit]]:
    text = draw(st.text(alphabet="abcdefg XYZ\n", min_size=5, max_size=80))
    n = len(text)
    cuts = sorted(draw(st.lists(st.integers(0, n), min_size=0, max_size=8, unique=True)))
    spans = [(a, b) for a, b in zip(cuts[::2], cuts[1::2], strict=False) if b > a]
    edits: list[Edit] = []
    for _ in range(draw(st.integers(0, 6))):
        pos = draw(st.integers(0, n))
        length = draw(st.integers(0, min(3, n - pos)))
        new = draw(st.text(alphabet="qr \n", max_size=3))
        e = Edit(pos, length, new)
        if any(perturb.straddles(e, a, b) for a, b in spans):
            continue
        if any(not (e.pos + e.length <= f.pos or f.pos + f.length <= e.pos) or e.pos == f.pos
               for f in edits):  # fmt: skip
            continue
        edits.append(e)
    return text, spans, edits


def apply_inside(text: str, a: int, b: int, edits: list[Edit]) -> str:
    """Expected new value: the span's own text with only the edits wholly inside it applied
    (insertions strictly inside; insertions at its edges belong outside)."""
    out, last = [], a
    for e in sorted(edits, key=lambda e: e.pos):
        inside = a <= e.pos and e.pos + e.length <= b and (e.length > 0 or a < e.pos < b)
        if inside:
            out += [text[last : e.pos], e.new]
            last = e.pos + e.length
    out.append(text[last:b])
    return "".join(out)


@settings(max_examples=700)
@given(case())
def test_remap_keeps_every_value(c: tuple[str, list[tuple[int, int]], list[Edit]]) -> None:
    text, spans, edits = c
    assume(spans)
    doc = doc_with(text, spans)
    new = perturb.apply(doc, edits)
    for (a, b), s in zip(spans, new.spans, strict=True):
        assert s.value == new.text[s.start : s.end] == apply_inside(text, a, b, edits)
    assert new.gen_meta["sections"] == [perturb.shift(0, sorted(edits, key=lambda e: e.pos))]


def test_straddling_edit_is_refused() -> None:
    doc = doc_with("Anna Nowak was seen", [(0, 10)])
    with pytest.raises(RemapError, match="straddles"):
        perturb.apply(doc, [Edit(8, 4, "")])
    with pytest.raises(RemapError, match="overlapping"):
        perturb.apply(doc, [Edit(12, 2, ""), Edit(13, 2, "")])


# --- perturbations on real generated docs --------------------------------------------------------


@pytest.fixture(scope="module")
def world() -> W.World:
    return W.build(SPEC, frozenset(template_vocabulary()))


@pytest.fixture(scope="module")
def scanner(world: W.World) -> checks.Scanner:
    return checks.Scanner(world)


def words(text: str) -> int:
    return len(text.split())


def gen(world: W.World, t: DocType, bucket: LengthBucket, k: int, **kw: object) -> Document:
    plan = SPEC.doc_plan[t]
    site = world.sites()[k % len(world.sites())]
    cats = frozenset(c for c in PiiCategory if getattr(plan.pii, c.value) > 0)
    sponsor = plan.level == "sponsor"
    subject = site.subjects[k % 15] if t in SUBJECT_TYPES else None
    ds = DocSpec(
        doc_id=f"p-{t.value}-{k}", doc_type=t, lang="en", bucket=bucket,
        study=world.study_of(site), site=None if sponsor else site, subject=subject,
        mode="clean" if sponsor else "normal", enabled=cats, **kw,  # type: ignore[arg-type]
    )  # fmt: skip
    return assemble(ds, SPEC, words)


@pytest.mark.parametrize("t", list(DocType), ids=lambda t: t.value)
def test_line_wrap_and_ocr_keep_labels(t: DocType, world: W.World, scanner: checks.Scanner) -> None:
    for k in range(3):
        doc = gen(world, t, SPEC.doc_plan[t].buckets[-1], k)
        wrapped = perturb.apply(doc, perturb.line_wrap(doc, 72), "line_wrap")
        assert all(len(line) <= 72 or " " not in line.strip() or "|" in line
                   for line in wrapped.text.split("\n"))  # fmt: skip
        assert checks.v1(wrapped, POLICY) == []
        noisy = perturb.apply(
            wrapped, perturb.ocr_noise(wrapped, random.Random(k), 0.02), "ocr_noise"
        )
        assert checks.v1(noisy, POLICY) == []
        assert len(noisy.spans) == len(doc.spans) and len(noisy.negatives) == len(doc.negatives)
        assert {"line_wrap", "ocr_noise"} <= set(noisy.tags)


@pytest.mark.parametrize("style", ["tab", "fixed"])
def test_table_restyle(style: str, world: W.World, scanner: checks.Scanner) -> None:
    for t in (DocType.CRF, DocType.DEVIATION, DocType.CONMED, DocType.LAB, DocType.DELEGATION):
        doc = gen(world, t, LengthBucket.MEDIUM, 2)
        styled = perturb.apply(doc, perturb.table_style(doc, style), "table")
        assert " | " not in styled.text and "table" in styled.tags
        assert checks.check(styled, POLICY, scanner) == []


def test_headers_footers_and_email_quoting(world: W.World, scanner: checks.Scanner) -> None:
    doc = gen(world, DocType.MONITORING, LengthBucket.LONG, 4, headers_footers=True)
    assert "headers_footers" in doc.tags
    pages = doc.text.count("| Confidential")
    assert pages >= 2 and sum(n.kind == "protocol_no" for n in doc.negatives) >= pages
    assert checks.check(doc, POLICY, scanner) == []
    mail = gen(world, DocType.SITE_EMAIL, LengthBucket.SHORT, 1)
    assert "email_quoting" in mail.tags and "\n> " in mail.text


class _Draws:
    """Stands in for random.Random: random() returns 0 (edit) at the listed text positions."""

    def __init__(self, hits: set[int]) -> None:
        self.hits, self.i = hits, -1

    def random(self) -> float:
        self.i += 1
        return 0.0 if self.i in self.hits else 1.0


def test_ocr_never_fabricates_a_name_from_several_drops() -> None:
    from bench.domain import Document, LengthBucket, WorldRefs

    text = "Samples are shipped cold. Tablets ship warm."
    doc = Document(id="x", doc_type="protocol_section", lang="en", text=text, spans=[],
                   negatives=[], tags=[], length_bucket=LengthBucket.SHORT, pii_depth=None,
                   world_refs=WorldRefs(study="S", site="SPONSOR", subjects=[]),
                   gen_meta={})  # fmt: skip
    m, p, b = text.index("m"), text.index("p"), text.index("b")  # Sa[m][p]les, Ta[b]lets
    edits = perturb.ocr_noise(doc, _Draws({m, p, b}), 0.01, frozenset({"sales"}))  # type: ignore[arg-type]
    assert [e.pos for e in edits] == [b]  # "Sales" would be a name: both of its drops are gone
    all_edits = perturb.ocr_noise(doc, _Draws({m, p, b}), 0.01)  # type: ignore[arg-type]
    assert sorted(e.pos for e in all_edits) == [m, p, b]
