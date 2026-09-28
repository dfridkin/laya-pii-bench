"""M5 split stage: leak-free (gate 1), class-complete (gate 2), deterministic, manifest (gate 4)."""

import re
from pathlib import Path

import pytest

from bench import split as sp
from bench.config import load_arms, load_gen_spec, load_policy, load_question_sets, load_split
from bench.domain import Document, Splits, Unit
from bench.generate import corpus
from bench.generate import world as W
from bench.generate.render import template_vocabulary
from bench.label import label_docs

ROOT = Path(__file__).resolve().parent.parent
SPEC = load_gen_spec(ROOT / "config" / "gen_spec.yaml")
POLICY = load_policy(ROOT / "config" / "policy.yaml")
CFG = load_split(ROOT / "config" / "split.yaml").model_copy(update={"search_iterations": 300})
ARMS = load_arms(ROOT / "config" / "arms.yaml")
QSETS = load_question_sets(ROOT / "config" / "questions")


def words(text: str) -> int:
    return len(text) // 4  # close to tokenization, so native non-English docs reach their bucket


def offsets(text: str) -> list[tuple[int, int]]:
    return [(m.start(), m.end()) for m in re.finditer(r"\s*\S+", text)]


@pytest.fixture(scope="module")
def corpus_docs() -> list[Document]:
    # non-English docs fall below the short bucket under a word counter and are skipped; the rest
    # of the corpus is enough to exercise the split
    return corpus.generate(SPEC, POLICY, words).docs


@pytest.fixture(scope="module")
def units(corpus_docs: list[Document]) -> dict[str, list[Unit]]:
    return {a: label_docs(corpus_docs, ARMS.arms[a], POLICY, offsets, "fake")
            for a in ("A", "B2", "B4")}  # fmt: skip


@pytest.fixture(scope="module")
def result(
    corpus_docs: list[Document], units: dict[str, list[Unit]]
) -> tuple[Splits, dict[str, float]]:
    return sp.build(corpus_docs, units, QSETS, CFG, "d", "c")


def test_groups_and_holdout(
    corpus_docs: list[Document], result: tuple[Splits, dict[str, float]]
) -> None:
    splits, _ = result
    for d in corpus_docs:
        s = splits.doc_split[d.id]
        assert (s == "holdout") == (
            d.doc_type == CFG.holdout_doc_type
        )  # all IRB letters, only them
    sponsor = [d for d in corpus_docs if d.world_refs.site == "SPONSOR"]
    assert {splits.doc_split[d.id] for d in sponsor} == {"train", "calib", "test"}


def test_gate1_no_site_subject_or_staff_across_splits(
    corpus_docs: list[Document], result: tuple[Splits, dict[str, float]]
) -> None:
    splits, _ = result
    assert sp.leakage(splits, corpus_docs) == []
    world = W.build(SPEC, frozenset(template_vocabulary()))
    staff_site = sp.staff_sites(world)
    assert len(staff_site) > 100
    assert sp.staff_leakage(splits, corpus_docs, staff_site) == []
    # and every person's site maps to one split (D-018 makes staff disjointness follow)
    site_split = {k: v for k, v in splits.groups.items() if "/" in k}
    assert all("/".join(p.id.split("/")[:2]) in site_split for p in world.persons())


def test_leakage_detects_a_crossing(
    corpus_docs: list[Document], result: tuple[Splits, dict[str, float]]
) -> None:
    splits, _ = result
    site_doc = next(
        d
        for d in corpus_docs
        if d.world_refs.site != "SPONSOR"
        and splits.doc_split[d.id] == "train"
        and d.world_refs.subjects
    )
    moved = splits.model_copy(update={"doc_split": {**splits.doc_split, site_doc.id: "test"}})
    problems = sp.leakage(moved, corpus_docs)
    assert any(p.startswith("site ") for p in problems) and any(
        p.startswith("subject ") for p in problems
    )


def test_locales_are_stratified(
    corpus_docs: list[Document], result: tuple[Splits, dict[str, float]]
) -> None:
    splits, _ = result
    locales = sp.site_locales(corpus_docs, CFG)
    for loc in ("en", "de", "es", "pl"):
        where = {splits.groups[g] for g, lang in locales.items() if lang == loc}
        assert where == {"train", "calib", "test"}, loc


def test_class_coverage_and_manifest(
    units: dict[str, list[Unit]], result: tuple[Splits, dict[str, float]]
) -> None:
    splits, summary = result
    man = sp.manifest(units, splits, QSETS, "d", "p", "s", {"A": "u"})
    assert summary["missing"] == len(man.missing) == 0, man.missing[:10]
    for arm, st in man.arms.items():
        assert sum(st.by_split.values()) == len(units[arm])
        for per_split in st.classes["qs_v1"].values():
            assert set(per_split) == {"train", "calib", "test", "holdout"}
    assert man.arms["B4"].kind == "doc"


def test_split_is_deterministic(corpus_docs: list[Document], units: dict[str, list[Unit]],
                                result: tuple[Splits, dict[str, float]]) -> None:  # fmt: skip
    again, _ = sp.build(corpus_docs, units, QSETS, CFG, "d", "c")
    assert again == result[0]


def test_ratios_close_to_config(result: tuple[Splits, dict[str, float]]) -> None:
    splits, summary = result
    main = {s: n for s, n in splits.counts.items() if s != "holdout"}
    total = sum(main.values())
    for s, n in main.items():
        assert abs(n / total - CFG.ratios[s]) <= CFG.ratio_tolerance, (s, n, total)  # type: ignore[index]
    assert summary["max_share_error"] <= CFG.ratio_tolerance


def test_staff_leakage_detects_a_crossing(
    corpus_docs: list[Document], result: tuple[Splits, dict[str, float]]
) -> None:
    splits, _ = result
    staff_site = sp.staff_sites(W.build(SPEC, frozenset(template_vocabulary())))
    doc = next(
        d
        for d in corpus_docs
        if splits.doc_split[d.id] == "train" and any(s.value in staff_site for s in d.spans)
    )
    moved = splits.model_copy(update={"doc_split": {**splits.doc_split, doc.id: "test"}})
    assert any(p.startswith("staff of ") for p in sp.staff_leakage(moved, corpus_docs, staff_site))
