"""Split stage (D-005 amended, D-016, D-018; invariant 2): leak-free, class-complete splits.

Groups: every site-level document belongs to its site group (`study/site`); every sponsor-level
document is its own group; every holdout-type document (IRB letters) goes to holdout regardless of
site. Groups are assigned to train/calib/test by a seeded search that
  1. stratifies site groups by locale (every split gets each language that has >= 3 sites),
  2. gives sponsor groups exact ratio counts,
  3. ranks candidates by missing gold classes (every arm x question set x question x class must
     appear in train, calib and test: M5 gate 2), then by document-share error.
Split reads the label stage's units to measure class coverage, so it runs after `bench label`; the
label stage itself never depends on the split.
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from collections.abc import Mapping, Sequence
from dataclasses import dataclass

import numpy as np

from bench.calibrate import gold_answer
from bench.config import SplitConfig
from bench.domain import (
    ArmLabelStats,
    ChoiceQuestion,
    Document,
    LabelManifest,
    QuestionSet,
    Split,
    Splits,
    Unit,
)
from bench.generate import variants as V
from bench.generate.seeds import rng
from bench.generate.world import World

MAIN_SPLITS: tuple[Split, ...] = ("train", "calib", "test")
ALL_SPLITS: tuple[Split, ...] = ("train", "calib", "test", "holdout")
SPONSOR_SITE = "SPONSOR"


class SplitError(RuntimeError):
    pass


def group_key(doc: Document, cfg: SplitConfig) -> str:
    if doc.doc_type == cfg.holdout_doc_type:
        return "holdout"
    if doc.world_refs.site == SPONSOR_SITE:
        return f"sponsor:{doc.id}"
    return f"{doc.world_refs.study}/{doc.world_refs.site}"  # D-016


def site_locales(docs: Sequence[Document], cfg: SplitConfig) -> dict[str, str]:
    """Locale of each site group: the non-English language its documents use, else English."""
    langs: dict[str, set[str]] = defaultdict(set)
    for d in docs:
        k = group_key(d, cfg)
        if "/" in k:
            langs[k].add(d.lang)
    out: dict[str, str] = {}
    for k, ls in langs.items():
        other = sorted(ls - {"en"})
        if len(other) > 1:
            raise SplitError(f"site {k} has documents in several non-English languages: {other}")
        out[k] = other[0] if other else "en"
    return out


def class_keys(qsets: Mapping[str, QuestionSet]) -> list[tuple[str, str, str]]:
    """(qs, question, class) for every choice option of every question set."""
    out: list[tuple[str, str, str]] = []
    for qs_id in sorted(qsets):
        for q, spec in qsets[qs_id].questions.items():
            if isinstance(spec, ChoiceQuestion):
                out += [(qs_id, q, c) for c in spec.criteria]
    return out


@dataclass
class _Matrix:
    groups: list[str]
    keys: list[tuple[str, str, str, str]]  # (arm, qs, question, class)
    counts: np.ndarray  # groups x keys: units per group with that gold class
    docs: np.ndarray  # docs per group


def _matrix(
    groups: list[str],
    doc_group: Mapping[str, str],
    units_by_arm: Mapping[str, Sequence[Unit]],
    qkeys: Sequence[tuple[str, str, str]],
) -> _Matrix:
    keys = [(arm, qs, q, c) for arm in sorted(units_by_arm) for qs, q, c in qkeys]
    kidx = {k: i for i, k in enumerate(keys)}
    gidx = {g: i for i, g in enumerate(groups)}
    counts = np.zeros((len(groups), len(keys)), dtype=np.int64)
    by_q: dict[tuple[str, str], list[str]] = defaultdict(list)
    for qs, q, _ in qkeys:
        by_q[(qs, q)].append(q)
    for arm, units in units_by_arm.items():
        for u in units:
            g = gidx[doc_group[u.doc_id]]
            for qs, q in by_q:
                k = kidx.get((arm, qs, q, gold_answer(u.gold, q)))
                if k is not None:
                    counts[g, k] += 1
    docs = np.zeros(len(groups), dtype=np.int64)
    for gname in doc_group.values():
        docs[gidx[gname]] += 1
    return _Matrix(groups, keys, counts, docs)


def assign(
    docs: Sequence[Document],
    units_by_arm: Mapping[str, Sequence[Unit]],
    qsets: Mapping[str, QuestionSet],
    cfg: SplitConfig,
) -> tuple[dict[str, Split], dict[str, float]]:
    """Group -> split for the best candidate, and a summary of its score."""
    doc_group = {d.id: group_key(d, cfg) for d in docs}
    groups = sorted(set(doc_group.values()) - {"holdout"})
    locales = site_locales(docs, cfg)
    sites_by_locale: dict[str, list[str]] = defaultdict(list)
    for g in groups:
        if "/" in g:
            sites_by_locale[locales[g]].append(g)
    sponsors = [g for g in groups if g.startswith("sponsor:")]
    main_doc_group = {k: v for k, v in doc_group.items() if v != "holdout"}
    main_units = {
        a: [u for u in us if doc_group[u.doc_id] != "holdout"] for a, us in units_by_arm.items()
    }
    m = _matrix(groups, main_doc_group, main_units, class_keys(qsets))
    weights = [cfg.ratios["train"], cfg.ratios["calib"], cfg.ratios["test"]]
    ratios = np.array(weights)
    total_docs = m.docs.sum()
    gpos = {g: i for i, g in enumerate(groups)}
    # only keys that exist somewhere can be required
    present = m.counts.sum(axis=0) > 0

    best: tuple[tuple[int, int, float], np.ndarray] | None = None
    for it in range(cfg.search_iterations):
        r = rng(cfg.seed, "split", it)
        onehot = np.zeros((3, len(groups)), dtype=np.int64)
        for loc in sorted(sites_by_locale):
            sites = sorted(sites_by_locale[loc])
            r.shuffle(sites)
            for j, g in enumerate(sites):
                s = j if len(sites) >= 3 and j < 3 else r.choices(range(3), weights=weights)[0]
                onehot[s, gpos[g]] = 1
        order = sorted(sponsors)
        r.shuffle(order)
        cuts = np.floor(np.cumsum(ratios) * len(order) + 0.5).astype(int)
        for j, g in enumerate(order):
            onehot[int(np.searchsorted(cuts, j, side="right")), gpos[g]] = 1
        cover = onehot @ m.counts  # 3 x keys
        missing = int(((cover == 0) & present).sum())
        missing_calib = int(((cover[1] == 0) & present).sum())
        shares = (onehot @ m.docs) / total_docs
        dev = float(np.abs(shares - ratios).max())
        score = (missing, missing_calib, dev)
        if best is None or score < best[0]:
            best = (score, onehot)
    assert best is not None
    (missing, missing_calib, dev), onehot = best
    out: dict[str, Split] = {
        g: MAIN_SPLITS[int(onehot[:, i].argmax())] for i, g in enumerate(groups)
    }
    out["holdout"] = "holdout"
    return out, {"missing": missing, "missing_calib": missing_calib, "max_share_error": dev}


def build(
    docs: Sequence[Document],
    units_by_arm: Mapping[str, Sequence[Unit]],
    qsets: Mapping[str, QuestionSet],
    cfg: SplitConfig,
    docs_sha256: str,
    config_sha256: str,
) -> tuple[Splits, dict[str, float]]:
    groups, summary = assign(docs, units_by_arm, qsets, cfg)
    doc_split: dict[str, Split] = {
        d.id: groups[group_key(d, cfg)] for d in sorted(docs, key=lambda d: d.id)
    }
    counts = Counter(doc_split.values())
    splits = Splits(
        seed=cfg.seed, docs_sha256=docs_sha256, config_sha256=config_sha256,
        doc_split=doc_split, groups=dict(sorted(groups.items())),
        counts={s: counts.get(s, 0) for s in ALL_SPLITS},
    )  # fmt: skip
    return splits, summary


def leakage(splits: Splits, docs: Sequence[Document]) -> list[str]:
    """Gate 1: no site, subject or staff person in more than one of train/calib/test; holdout has no
    subjects. Staff persons belong to exactly one site (D-018), so site disjointness implies staff
    disjointness; `staff_leakage` checks it against the world directly."""
    problems: list[str] = []
    seen: dict[str, dict[str, set[Split]]] = {"site": defaultdict(set), "subject": defaultdict(set)}
    for d in docs:
        s = splits.doc_split[d.id]
        if s == "holdout":
            if d.world_refs.subjects:
                problems.append(f"holdout doc {d.id} references subjects")
            continue
        if d.world_refs.site != SPONSOR_SITE:
            seen["site"][f"{d.world_refs.study}/{d.world_refs.site}"].add(s)
        for sub in d.world_refs.subjects:
            seen["subject"][f"{d.world_refs.study}/{sub}"].add(s)
    for kind, m in seen.items():
        for key, ss in sorted(m.items()):
            if len(ss) > 1:
                problems.append(f"{kind} {key} in {sorted(ss)}")
    return problems


def staff_sites(world: World) -> dict[str, str]:
    """Every staff value that names exactly one person (name surfaces, email, phone) -> that
    person's site key (`study/site`). Ownership is per person over every person in the world,
    lone given names included: "Martin" as one person's surname and another's first name names
    no one in particular and is left out (M8 scale-up false positive)."""
    owners: dict[str, set[str]] = defaultdict(set)
    staff_site: dict[str, str] = {}
    for site in world.sites():
        people = [(p, True) for p in site.staff.values()] + [
            (s.person, False) for s in site.subjects
        ]
        for p, is_staff in people:
            if is_staff:
                staff_site[p.id] = site.key
            for v in [*(V.name(p, x) for x in V.NAME_SURFACES), p.email, p.phone]:
                if v:
                    owners[v].add(p.id)
    return {
        v: staff_site[next(iter(ids))]
        for v, ids in owners.items()
        if len(ids) == 1 and next(iter(ids)) in staff_site
    }


def staff_leakage(
    splits: Splits, docs: Sequence[Document], staff_site: Mapping[str, str]
) -> list[str]:
    """Staff spans (by exact value -> the world person's site) never cross train/calib/test.
    `staff_site` maps a staff value (email/phone/full name form) to its site key."""
    where: dict[str, set[Split]] = defaultdict(set)
    for d in docs:
        s = splits.doc_split[d.id]
        if s == "holdout":
            continue
        for sp in d.spans:
            if sp.value and sp.value in staff_site:
                where[staff_site[sp.value]].add(s)
    return [f"staff of {k} in {sorted(v)}" for k, v in sorted(where.items()) if len(v) > 1]


def manifest(
    units_by_arm: Mapping[str, Sequence[Unit]],
    splits: Splits,
    qsets: Mapping[str, QuestionSet],
    docs_sha256: str,
    policy_sha256: str,
    splits_sha256: str,
    units_sha256: Mapping[str, str],
) -> LabelManifest:
    """Gates 2 and 4: unit counts per arm and split, gold class counts per question."""
    qkeys = class_keys(qsets)
    arms: dict[str, ArmLabelStats] = {}
    missing: list[str] = []
    holdout_missing: list[str] = []
    for arm in sorted(units_by_arm):
        units = units_by_arm[arm]
        by_split: Counter[Split] = Counter()
        trunc: Counter[Split] = Counter()
        span: Counter[Split] = Counter()
        classes: dict[str, dict[str, dict[Split, dict[str, int]]]] = defaultdict(
            lambda: defaultdict(lambda: {s: {} for s in ALL_SPLITS})
        )
        for u in units:
            s = splits.doc_split[u.doc_id]
            by_split[s] += 1
            trunc[s] += u.truncated
            span[s] += u.split_span
        for qs, q, c in qkeys:
            for s in ALL_SPLITS:
                classes[qs][q][s][c] = 0
        for u in units:
            s = splits.doc_split[u.doc_id]
            for qs, q in {(qs, q) for qs, q, _ in qkeys}:
                c = gold_answer(u.gold, q)
                if c in classes[qs][q][s]:
                    classes[qs][q][s][c] += 1
        for qs, q, c in qkeys:
            for s in ALL_SPLITS:
                if classes[qs][q][s][c] == 0:
                    (holdout_missing if s == "holdout" else missing).append(
                        f"{arm}/{qs}/{q}/{s}: {c}"
                    )
        kind = units[0].kind if units else "chunk"
        arms[arm] = ArmLabelStats(
            arm=arm, kind=kind, tokenizer=units[0].tokenizer if units else "",
            units_sha256=units_sha256.get(arm, ""), n_units=len(units),
            by_split={s: by_split.get(s, 0) for s in ALL_SPLITS},
            truncated={s: trunc.get(s, 0) for s in ALL_SPLITS},
            split_span={s: span.get(s, 0) for s in ALL_SPLITS},
            classes=json.loads(json.dumps(classes)),
        )  # fmt: skip
    return LabelManifest(
        docs_sha256=docs_sha256, policy_sha256=policy_sha256, splits_sha256=splits_sha256,
        arms=arms, missing=missing, holdout_missing=holdout_missing,
    )  # fmt: skip


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()
