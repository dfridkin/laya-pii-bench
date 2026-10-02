"""Score stage: metrics, routing, slices and bootstrap CIs (docs/specs/metrics.md).

Reads decisions, units, documents and frozen calib params. Refuses calib params whose content hash
doesn't match (invariant 3). Routing is applied here, never in the runner (invariant 4):

- p(pii) >= t_high, or predicted role is patient/both (policy.routing.patient_role_forces_redact)
  -> REDACT
- else p(pii) < t_low -> FORWARD
- else -> ESCALATE

"Recall" is pii_present recall at t_low: positives with calibrated p(pii) >= t_low.
"""

from __future__ import annotations

import hashlib
from collections import Counter, defaultdict
from collections.abc import Callable, Iterable, Mapping, Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

import numpy as np
from scipy.stats import beta  # pyright: ignore[reportMissingTypeStubs]

from bench.calibrate import PII_QUESTION, apply_temperature, calib_key, gold_answer
from bench.config import Policy
from bench.domain import (
    CalibParams,
    CalibrationMetrics,
    ConfusionMatrix,
    CurvePoint,
    Decision,
    Document,
    FailureCase,
    GoldAnswers,
    Headline,
    HwInfo,
    Interval,
    LatencyStats,
    MultiLabelMetrics,
    PiiCategory,
    QuestionMetrics,
    ReliabilityBin,
    Route,
    RoutedDecision,
    RoutingMetrics,
    RunContext,
    Scores,
    SliceRow,
    SpeedMetrics,
    SplitScores,
    Unit,
)
from bench.label import member_spans
from bench.validate import KNOWN_TAGS

ECE_BINS = 15
SMALL_SLICE = 30
# document tags that describe a perturbation (the rest of validate.KNOWN_TAGS are content tags)
PERTURBATION_TAGS = tuple(sorted(KNOWN_TAGS - {"hard_negative", "pre_redacted"}))


class ScoreError(ValueError):
    pass


# --- metric primitives (golden-tested) ---------------------------------------------------------


def accuracy(gold: Sequence[str], pred: Sequence[str]) -> float:
    return sum(g == p for g, p in zip(gold, pred, strict=True)) / len(gold)


def confusion(gold: Sequence[str], pred: Sequence[str], labels: Sequence[str]) -> ConfusionMatrix:
    idx = {lab: i for i, lab in enumerate(labels)}
    counts = [[0] * len(labels) for _ in labels]
    for g, p in zip(gold, pred, strict=True):
        counts[idx[g]][idx[p]] += 1
    return ConfusionMatrix(labels=list(labels), counts=counts)


def _f1(tp: int, fp: int, fn: int) -> float:
    return 0.0 if tp == 0 else 2 * tp / (2 * tp + fp + fn)


def per_class_f1(gold: Sequence[str], pred: Sequence[str]) -> dict[str, float]:
    """F1 for every label present in gold or predictions (the set macro-F1 averages over)."""
    out: dict[str, float] = {}
    for lab in sorted(set(gold) | set(pred)):
        tp = sum(g == lab and p == lab for g, p in zip(gold, pred, strict=True))
        fp = sum(g != lab and p == lab for g, p in zip(gold, pred, strict=True))
        fn = sum(g == lab and p != lab for g, p in zip(gold, pred, strict=True))
        out[lab] = _f1(tp, fp, fn)
    return out


def macro_f1(gold: Sequence[str], pred: Sequence[str]) -> float:
    f1 = per_class_f1(gold, pred)
    return sum(f1.values()) / len(f1)


def majority(gold: Sequence[str]) -> tuple[str, float]:
    """Most frequent gold class (ties: alphabetical) and the accuracy of always predicting it."""
    counts = Counter(gold)
    top = min(counts, key=lambda k: (-counts[k], k))
    return top, counts[top] / len(gold)


def reliability(
    conf: Sequence[float], correct: Sequence[bool], bins: int = ECE_BINS
) -> list[ReliabilityBin]:
    """Equal-width bins: bin i holds conf in [i/bins, (i+1)/bins); conf 1.0 goes in the last."""
    members: list[list[int]] = [[] for _ in range(bins)]
    for i, c in enumerate(conf):
        members[min(int(c * bins), bins - 1)].append(i)
    out: list[ReliabilityBin] = []
    for b, idx in enumerate(members):
        out.append(
            ReliabilityBin(
                lo=b / bins,
                hi=(b + 1) / bins,
                n=len(idx),
                mean_confidence=sum(conf[i] for i in idx) / len(idx) if idx else None,
                accuracy=sum(correct[i] for i in idx) / len(idx) if idx else None,
            )
        )
    return out


def ece(conf: Sequence[float], correct: Sequence[bool], bins: int = ECE_BINS) -> float:
    n = len(conf)
    return sum(
        b.n / n * abs(b.accuracy - b.mean_confidence)
        for b in reliability(conf, correct, bins)
        if b.n and b.accuracy is not None and b.mean_confidence is not None
    )


def brier(probs: Sequence[Mapping[str, float]], gold: Sequence[str]) -> float:
    """Multi-class Brier: mean over units of sum_k (p_k - y_k)^2."""
    total = 0.0
    for p, g in zip(probs, gold, strict=True):
        total += sum((v - (1.0 if k == g else 0.0)) ** 2 for k, v in p.items())
    return total / len(gold)


def auroc(scores: Sequence[float], labels: Sequence[bool]) -> float | None:
    """P(score of a positive > score of a negative), ties count 1/2. None with one class."""
    pos = [s for s, y in zip(scores, labels, strict=True) if y]
    neg = [s for s, y in zip(scores, labels, strict=True) if not y]
    if not pos or not neg:
        return None
    wins = sum((p > n) + 0.5 * (p == n) for p in pos for n in neg)
    return wins / (len(pos) * len(neg))


def recall_at(p: Sequence[float], positive: Sequence[bool], t_low: float) -> float | None:
    pos = [q for q, y in zip(p, positive, strict=True) if y]
    return sum(q >= t_low for q in pos) / len(pos) if pos else None


def exact_recall_hi(hits: int, n: int) -> float | None:
    """Clopper-Pearson two-sided 95% upper bound for hits/n (1 when there are no misses)."""
    if n == 0:
        return None
    if hits == n:
        return 1.0
    return float(beta.ppf(0.975, hits + 1, n - hits))  # pyright: ignore[reportUnknownMemberType, reportUnknownArgumentType]


def positive_kind(gold: GoldAnswers) -> str:
    c = gold.categories_multi
    if c[PiiCategory.PHI_DIRECT]:
        return "direct"
    if c[PiiCategory.STAFF_PII]:
        return "staff"
    return "quasi_only"


def exact_recall_lo(hits: int, n: int) -> float | None:
    """Clopper-Pearson two-sided 95% lower bound for hits/n (0 when hits == 0)."""
    if n == 0:
        return None
    if hits == 0:
        return 0.0
    return float(beta.ppf(0.025, hits, n - hits + 1))  # pyright: ignore[reportUnknownMemberType, reportUnknownArgumentType]


def route_unit(
    p_pii: float, role: str | None, t_low: float, t_high: float | None, patient_forces: bool
) -> tuple[Route, list[str]]:
    triggers: list[str] = []
    if t_high is not None and p_pii >= t_high:
        triggers.append("p_at_or_above_t_high")
    if patient_forces and role in ("patient", "both"):
        triggers.append(f"role_{role}")
    if triggers:
        return Route.REDACT, triggers
    if p_pii < t_low:
        return Route.FORWARD, ["p_below_t_low"]
    return Route.ESCALATE, ["p_in_escalate_band"]


def latency_stats(ms: Sequence[float]) -> LatencyStats | None:
    if not ms:
        return None
    a = np.array(ms, dtype=float)
    return LatencyStats(
        n=len(ms),
        p50_ms=float(np.percentile(a, 50)),
        p95_ms=float(np.percentile(a, 95)),
        p99_ms=float(np.percentile(a, 99)),
        mean_ms=float(a.mean()),
        units_per_sec=float(len(ms) / (a.sum() / 1000.0)),
    )


# --- scored rows -------------------------------------------------------------------------------


@dataclass(frozen=True)
class Row:
    unit: Unit
    doc: Document
    decision: Decision
    raw: dict[str, dict[str, float]]
    cal: dict[str, dict[str, float]]
    route: Route
    triggers: list[str]

    @property
    def p_pii(self) -> float:
        return self.cal[PII_QUESTION]["A"]

    @property
    def positive(self) -> bool:
        return self.unit.gold.pii_present == "A"

    @property
    def false_forward(self) -> bool:
        return self.positive and self.route is Route.FORWARD


def _argmax(p: Mapping[str, float]) -> str:
    return max(p, key=lambda k: p[k])  # first key wins ties, as laya's argmax does


def build_rows(
    decisions: Iterable[Decision],
    units: Mapping[str, Unit],
    docs: Mapping[str, Document],
    calib: CalibParams,
    policy: Policy,
) -> list[Row]:
    rows: list[Row] = []
    seen: set[str] = set()
    for d in decisions:
        if d.warmup:
            continue
        if (d.arm, d.qs) != (calib.arm, calib.qs):
            raise ScoreError(f"decision {d.arm}/{d.qs} vs calib {calib.arm}/{calib.qs}")
        if d.unit_id in seen:
            raise ScoreError(f"duplicate decision for unit {d.unit_id}")
        if d.unit_id not in units:
            raise ScoreError(f"decision for unknown unit {d.unit_id}")
        seen.add(d.unit_id)
        unit = units[d.unit_id]
        raw = {a.question: dict(a.probs) for a in d.answers}
        if PII_QUESTION not in raw:
            raise ScoreError(f"{d.unit_id}: no {PII_QUESTION} answer")
        cal: dict[str, dict[str, float]] = {}
        for q, p in raw.items():
            key = calib_key(q, len(p))
            if key not in calib.temperatures:
                raise ScoreError(f"no temperature for {key}")
            cal[q] = apply_temperature(p, calib.temperatures[key])
        role = _argmax(cal["subject_role"]) if "subject_role" in cal else None
        route, triggers = route_unit(
            cal[PII_QUESTION]["A"],
            role,
            calib.t_low,
            calib.t_high,
            policy.routing.patient_role_forces_redact,
        )
        rows.append(Row(unit, docs[unit.doc_id], d, raw, cal, route, triggers))
    return rows


# --- sections ----------------------------------------------------------------------------------


def bootstrap_values(
    rows: Sequence[Row],
    stat: Callable[[Sequence[Row]], float | None],
    resamples: int,
    seed: int,
) -> list[float]:
    """The statistic on `resamples` document-level resamples (units of a doc move together);
    resamples where the statistic is undefined (e.g. no positives) are dropped."""
    by_doc: dict[str, list[Row]] = defaultdict(list)
    for r in rows:
        by_doc[r.doc.id].append(r)
    doc_ids = sorted(by_doc)
    rng = np.random.default_rng(seed)
    values: list[float] = []
    for _ in range(resamples):
        pick = rng.integers(0, len(doc_ids), size=len(doc_ids))
        sample = [r for i in pick for r in by_doc[doc_ids[int(i)]]]
        v = stat(sample)
        if v is not None:
            values.append(v)
    return values


def bootstrap(
    rows: Sequence[Row],
    stat: Callable[[Sequence[Row]], float | None],
    resamples: int,
    seed: int,
) -> Interval | None:
    point = stat(rows)
    if point is None:
        return None
    if len({r.doc.id for r in rows}) < 2:  # one document: resampling can't vary anything
        return Interval(point=point, lo=None, hi=None, n_resamples=0)
    values = bootstrap_values(rows, stat, resamples, seed)
    if len(values) < 2:
        return Interval(point=point, lo=None, hi=None, n_resamples=len(values))
    lo, hi = np.percentile(np.array(values), [2.5, 97.5])
    return Interval(point=point, lo=float(lo), hi=float(hi), n_resamples=len(values))


def _recall(rows: Sequence[Row], t_low: float) -> float | None:
    return recall_at([r.p_pii for r in rows], [r.positive for r in rows], t_low)


def _forward_rate(rows: Sequence[Row]) -> float:
    return sum(r.route is Route.FORWARD for r in rows) / len(rows)


def headline(rows: Sequence[Row], calib: CalibParams, policy: Policy) -> Headline:
    b = policy.bootstrap
    above = [r for r in rows if r.p_pii >= calib.t_low]
    n_pos = sum(r.positive for r in rows)
    hits = sum(r.positive and r.p_pii >= calib.t_low for r in rows)
    false_fwd = sum(r.false_forward for r in rows)
    fwd = bootstrap(rows, _forward_rate, b.resamples, b.seed)
    assert fwd is not None
    return Headline(
        t_low=calib.t_low,
        t_high=calib.t_high,
        n_units=len(rows),
        n_docs=len({r.doc.id for r in rows}),
        n_positive=n_pos,
        recall=bootstrap(rows, lambda rs: _recall(rs, calib.t_low), b.resamples, b.seed),
        recall_exact_lo=exact_recall_lo(hits, n_pos),
        route_recall=1 - false_fwd / n_pos if n_pos else None,
        forward_rate=fwd,
        false_forwards=false_fwd,
        precision=sum(r.positive for r in above) / len(above) if above else None,
        recall_target=calib.recall_target,
        recall_exact_hi=exact_recall_hi(hits, n_pos),
        specificity=(sum(not r.positive and r.route is Route.FORWARD for r in rows)
                     / max(1, len(rows) - n_pos)) if len(rows) > n_pos else None,
        auroc_pii=auroc([r.p_pii for r in rows], [r.positive for r in rows]),
        auroc_by_kind={
            k: auroc([r.p_pii for r in rows if not r.positive or positive_kind(r.unit.gold) == k],
                     [r.positive for r in rows
                      if not r.positive or positive_kind(r.unit.gold) == k])
            for k in ("direct", "staff", "quasi_only")
        },
        truncated_forwarded=sum(_truncated(r) and r.route is Route.FORWARD for r in rows),
    )  # fmt: skip


def question_metrics(rows: Sequence[Row], q: str) -> QuestionMetrics:
    labels = list(rows[0].raw[q])
    gold = [gold_answer(r.unit.gold, q) for r in rows]
    pred = [_argmax(r.raw[q]) for r in rows]  # temperature scaling never changes the argmax
    maj, maj_acc = majority(gold)
    return QuestionMetrics(
        n=len(rows),
        accuracy=accuracy(gold, pred),
        macro_f1=macro_f1(gold, pred),
        per_class_f1=per_class_f1(gold, pred),
        confusion=confusion(gold, pred, labels),
        majority_class=maj,
        majority_baseline_accuracy=maj_acc,
    )


def multilabel(rows: Sequence[Row], questions: Sequence[str]) -> MultiLabelMetrics | None:
    qs = [q for q in questions if q.startswith("has_")]
    if not qs:
        return None
    per: dict[str, float] = {}
    tp = fp = fn = 0
    for q in qs:
        g = [gold_answer(r.unit.gold, q) == "A" for r in rows]
        p = [_argmax(r.raw[q]) == "A" for r in rows]
        t = sum(a and b for a, b in zip(g, p, strict=True))
        f_p = sum(b and not a for a, b in zip(g, p, strict=True))
        f_n = sum(a and not b for a, b in zip(g, p, strict=True))
        per[q] = _f1(t, f_p, f_n)
        tp, fp, fn = tp + t, fp + f_p, fn + f_n
    return MultiLabelMetrics(
        questions=qs,
        micro_f1=_f1(tp, fp, fn),
        macro_f1=sum(per.values()) / len(per),
        per_label_f1=per,
    )


def calibration_metrics(rows: Sequence[Row], q: str) -> CalibrationMetrics:
    gold = [gold_answer(r.unit.gold, q) for r in rows]
    out: dict[str, tuple[float, float, float | None, list[ReliabilityBin]]] = {}
    for name, probs in (("raw", [r.raw[q] for r in rows]), ("cal", [r.cal[q] for r in rows])):
        conf = [max(p.values()) for p in probs]
        correct = [_argmax(p) == g for p, g in zip(probs, gold, strict=True)]
        out[name] = (
            ece(conf, correct),
            brier(probs, gold),
            auroc(conf, correct),
            reliability(conf, correct),
        )
    return CalibrationMetrics(
        n=len(rows),
        ece_raw=out["raw"][0],
        ece_calibrated=out["cal"][0],
        brier_raw=out["raw"][1],
        brier_calibrated=out["cal"][1],
        auroc_raw=out["raw"][2],
        auroc_calibrated=out["cal"][2],
        reliability_raw=out["raw"][3],
        reliability_calibrated=out["cal"][3],
    )


def routing(rows: Sequence[Row]) -> RoutingMetrics:
    by_gold: dict[str, dict[Route, int]] = {g: dict.fromkeys(Route, 0) for g in ("A", "B")}
    counts = dict.fromkeys(Route, 0)
    triggers: Counter[str] = Counter()
    for r in rows:
        counts[r.route] += 1
        by_gold[r.unit.gold.pii_present][r.route] += 1
        triggers.update(r.triggers)
    return RoutingMetrics(
        counts=counts, by_gold_pii=by_gold, triggers=dict(sorted(triggers.items()))
    )


def _truncated(r: Row) -> bool:
    """The runner's per-question measurement when present (laya's real room is larger than the
    label stage's max_len - head_max_len budget); the label flag only for decisions without it."""
    if r.decision.state_tokens is not None:
        return bool(r.decision.truncated_questions)
    return r.unit.truncated


def _slice_keys(r: Row) -> list[tuple[str, str]]:
    d = r.doc
    perturb = [t for t in PERTURBATION_TAGS if t in d.tags] or ["none"]
    return [
        ("doc_type", str(d.doc_type)),
        ("length_bucket", str(d.length_bucket)),
        ("pii_depth", str(d.pii_depth) if d.pii_depth else "none"),
        ("hard_negative", "yes" if "hard_negative" in d.tags else "no"),
        ("pre_redacted", "yes" if "pre_redacted" in d.tags else "no"),
        ("split_span", "yes" if r.unit.split_span else "no"),
        ("truncated", "yes" if _truncated(r) else "no"),
        ("lang", d.lang),
        *(("perturbation", t) for t in perturb),
    ]


def slices(rows: Sequence[Row], t_low: float) -> list[SliceRow]:
    groups: dict[tuple[str, str], list[Row]] = defaultdict(list)
    for r in rows:
        for key in _slice_keys(r):
            groups[key].append(r)
    out: list[SliceRow] = []
    for (dim, val), rs in sorted(groups.items()):
        gold = [r.unit.gold.pii_present for r in rs]
        pred = [_argmax(r.raw[PII_QUESTION]) for r in rs]
        out.append(
            SliceRow(
                dimension=dim,
                value=val,
                n_units=len(rs),
                n_docs=len({r.doc.id for r in rs}),
                n_positive=sum(r.positive for r in rs),
                recall=_recall(rs, t_low),
                forward_rate=_forward_rate(rs),
                false_forwards=sum(r.false_forward for r in rs),
                pii_accuracy=accuracy(gold, pred),
                small_sample=len(rs) < SMALL_SLICE,
            )
        )
    return out


def _missed_kinds(r: Row, policy: Policy) -> list[str]:
    spans = member_spans(r.doc.spans, r.unit.start, r.unit.end)
    return sorted({s.value_kind for s in spans if s.category in policy.effective_pii_categories})


def _md_escape(text: str) -> str:
    return "".join("\\" + c if c in "\\`*_[]<>|#" else c for c in text)


def highlight(r: Row, counted: frozenset[PiiCategory] | None = None) -> str:
    """Unit text as a markdown blockquote; gold spans that count toward pii_present (clipped to
    the unit) in bold. Coded ids are not PII under D-001, so they are not bolded."""
    u, text = r.unit, r.doc.text
    parts: list[str] = []
    pos = u.start
    spans = member_spans(r.doc.spans, u.start, u.end)
    if counted is not None:
        spans = [s for s in spans if s.category in counted]
    for s in sorted(spans, key=lambda s: s.start):
        a, b = max(s.start, u.start), min(s.end, u.end)
        parts.append(_md_escape(text[pos:a]))
        parts.append(f"**{_md_escape(text[a:b])}**")
        pos = b
    parts.append(_md_escape(text[pos : u.end]))
    return "\n".join("> " + line for line in "".join(parts).split("\n"))


def failures(rows: Sequence[Row], policy: Policy) -> list[FailureCase]:
    return [
        FailureCase(
            unit_id=r.unit.id,
            doc_id=r.doc.id,
            text_markdown=highlight(r, policy.effective_pii_categories),
            route=r.route,
            triggers=r.triggers,
            gold=r.unit.gold,
            raw_probs=r.raw,
            calibrated_probs=r.cal,
            missed_value_kinds=_missed_kinds(r, policy),
        )
        for r in rows
        if r.false_forward
    ]


def split_scores(
    rows: Sequence[Row], split_units: int, calib: CalibParams, policy: Policy
) -> SplitScores:
    questions = list(rows[0].raw)
    missed: Counter[str] = Counter()
    for r in rows:
        if r.false_forward:
            missed.update(_missed_kinds(r, policy))
    return SplitScores(
        coverage_units=split_units,
        coverage_decided=len(rows),
        headline=headline(rows, calib, policy),
        per_question={q: question_metrics(rows, q) for q in questions},
        multilabel=multilabel(rows, questions),
        calibration={q: calibration_metrics(rows, q) for q in questions},
        routing=routing(rows),
        slices=slices(rows, calib.t_low),
        false_forward_value_kinds=dict(sorted(missed.items())),
        failures=failures(rows, policy),
        curve=curve(rows, calib, policy),
    )


def curve(rows: Sequence[Row], calib: CalibParams, policy: Policy) -> list[CurvePoint]:
    """D-007 amended: each calib-fit t_low of the curve, routed like the headline. Recall is route
    recall (PII units not forwarded / PII units). Each point raises t_high to at least its t_low,
    as `fit_t_high` does for the headline: with a fixed t_high a stricter t_low only moved units
    into the redact band and every point equaled the headline (M8 results review M1)."""
    out: list[CurvePoint] = []
    pos = [r.positive for r in rows]
    n_pos, n_neg = sum(pos), len(rows) - sum(pos)
    for key, t in sorted(calib.t_low_curve.items(), key=lambda kv: float(kv[0])):
        th = None if calib.t_high is None else max(calib.t_high, t)
        routes = [
            route_unit(r.p_pii, _argmax(r.cal["subject_role"]) if "subject_role" in r.cal else None,
                       t, th, policy.routing.patient_role_forces_redact)[0]
            for r in rows
        ]  # fmt: skip
        fwd = [rt is Route.FORWARD for rt in routes]
        hits = sum(y and not f for f, y in zip(fwd, pos, strict=True))
        out.append(CurvePoint(
            target=float(key), t_low=t,
            recall=hits / n_pos if n_pos else None,
            recall_exact_lo=exact_recall_lo(hits, n_pos),
            recall_exact_hi=exact_recall_hi(hits, n_pos),
            forward_rate=sum(fwd) / len(rows),
            negatives_forwarded=(sum(f and not y for f, y in zip(fwd, pos, strict=True)) / n_neg
                                 if n_neg else None),
            false_forwards=sum(f and y for f, y in zip(fwd, pos, strict=True)),
        ))  # fmt: skip
    return out


LENGTH_BUCKETS = ((0, 1000, "<1k"), (1000, 2000, "1-2k"), (2000, 4000, "2-4k"),
                  (4000, 8200, "4-8k"), (8200, 10**9, ">8k"))  # fmt: skip


def length_bucket(tokens: int | None) -> str:
    t = tokens or 0
    return next(name for lo, hi, name in LENGTH_BUCKETS if lo <= t < hi)


def outliers(ms: Sequence[float], tokens: Sequence[int | None] | None = None) -> int:
    """Calls slower than OUTLIER_X x the median of calls of similar length (M6 review: long units
    are slow by nature, so the median is taken within each length bucket)."""
    if not ms:
        return 0
    keys = [length_bucket(t) for t in tokens] if tokens is not None else ["all"] * len(ms)
    out = 0
    for k in set(keys):
        group = [m for m, g in zip(ms, keys, strict=True) if g == k]
        med = float(np.median(np.array(group, dtype=float)))
        out += sum(m > OUTLIER_X * med for m in group)
    return out


def drift(decisions: Sequence[Decision]) -> float | None:
    """Median ms/token of the last eighth of a run over the first eighth (run order), within the
    run's most common length bucket so that length mix along the run order can't fake a drift."""
    rows = [d for d in decisions if d.state_tokens]
    if not rows:
        return None
    modal = Counter(length_bucket(d.state_tokens) for d in rows).most_common(1)[0][0]
    rows = [d for d in rows if length_bucket(d.state_tokens) == modal]
    k = len(rows) // 8
    if k < 10:
        return None
    rate = [d.latency_ms / max(d.state_tokens or 1, 100) for d in rows]
    first, last = float(np.median(rate[:k])), float(np.median(rate[-k:]))
    return last / first if first else None


def autocast_state(decisions: Sequence[Decision]) -> str:
    seen = {d.autocast for d in decisions}
    if not seen or seen == {None}:
        return "unknown"
    if len(seen - {None}) > 1:
        return "mixed"
    return "on" if True in seen else "off"


def speed(
    decisions: Sequence[Decision],
    units: Mapping[str, Unit],
    hw: HwInfo | None,
    batched: Sequence[Decision] = (),
) -> SpeedMetrics:
    """Batch-1 stats from the arm's batch-1 run; batched stats from its batched run (audit C6),
    which is timing only: its answers never enter a metric."""
    live = [d for d in [*decisions, *batched] if not d.warmup]
    b1 = [d for d in live if d.mode == "batch1"]
    bb = [d for d in live if d.mode == "batched"]
    per_doc: dict[str, float] = defaultdict(float)
    for d in b1:
        per_doc[units[d.unit_id].doc_id] += d.latency_ms
    hardware = (
        f"{hw.cpu}, {hw.ram_gb} GB RAM, device {hw.device} ({hw.device_name}), torch {hw.torch}"
        if hw
        else "unknown hardware (no hw.json)"
    )
    return SpeedMetrics(
        hardware=hardware,
        batch1=latency_stats([d.latency_ms for d in b1]),
        batched=latency_stats([d.latency_ms for d in bb]),
        per_doc_ms=latency_stats(list(per_doc.values())),
        warmup_excluded=len(decisions) + len(batched) - len(live),
        batch1_autocast=autocast_state(b1),
        batch1_outliers=outliers([d.latency_ms for d in b1], [d.state_tokens for d in b1]),
        batch1_by_length={
            name: s
            for _, _, name in LENGTH_BUCKETS
            if (
                s := latency_stats(
                    [d.latency_ms for d in b1 if length_bucket(d.state_tokens) == name]
                )
            )
            is not None
        },
        batch1_drift=drift(b1),
        batched_autocast=autocast_state(bb),
    )


OUTLIER_X = 5.0  # a batch-1 call this many times the median counts as an outlier
OUTLIER_SHARE = 0.005  # above this share of calls, the speed numbers get a caveat
D008_ARM = "A"  # D-008 amended: the review trigger applies to arm A's test recall only
D008_GAP = 0.01  # D-008 amended: point recall minus exact 95% lower bound above this -> review
DRIFT_MAX = 1.25  # batch-1 ms/token end/start above this gets a caveat


def d008_gap(h: Headline) -> float | None:
    if h.recall is None or h.recall_exact_lo is None:
        return None
    return h.recall.point - h.recall_exact_lo


def caveats(
    splits: Mapping[str, SplitScores], calib: CalibParams, doc_level: bool = False,
    sp: SpeedMetrics | None = None,
) -> list[str]:  # fmt: skip
    out: list[str] = []
    test = splits.get("test")
    gap = d008_gap(test.headline) if test else None
    if calib.arm == D008_ARM and gap is not None and gap > D008_GAP:
        assert test is not None and test.headline.recall is not None
        out.append(
            f"D-008 review: test recall {test.headline.recall.point:.4f} minus its exact 95% lower "
            f"bound {test.headline.recall_exact_lo:.4f} = {gap:.4f} > {D008_GAP} "
            f"({test.headline.n_positive} positives)."
        )
    if doc_level:
        n = test.headline.n_docs if test else 0
        out.append(
            f"Doc-level arm: underpowered (D-008 amended); {n} test documents, few units each, "
            "so recall intervals are wide."
        )
    if (
        sp is not None
        and sp.batch1 is not None
        and sp.batch1_outliers > OUTLIER_SHARE * sp.batch1.n
    ):
        out.append(
            f"{sp.batch1_outliers} of {sp.batch1.n} batch-1 calls took over {OUTLIER_X:g}x the "
            "median of calls of similar length: treat p95/p99 with care."
        )
    if sp is not None and sp.batch1_drift is not None and sp.batch1_drift > DRIFT_MAX:
        out.append(
            f"Batch-1 latency per token drifted to {sp.batch1_drift:.2f}x its start by the end of "
            "the run at similar unit lengths (e.g. MPS allocator growth; the runner releases it "
            "between calls since 8e004bb): treat batch-1 p50/p95 as upper bounds."
        )
    if sp is not None:
        for mode, state in (("batch-1", sp.batch1_autocast), ("batched", sp.batched_autocast)):
            if state == "mixed":
                out.append(f"laya switched autocast off mid-run ({mode}): speed mixes precisions.")
    if calib.fit_on != "calib":
        out.append(
            f"Calibration fit_on={calib.fit_on}: temperatures and thresholds were fit on the "
            "scored units themselves. Calibrated metrics and routing are in-sample; this is a "
            "pipeline check, not a benchmark result."
        )
    if "holdout" not in splits:
        out.append("No holdout split was scored.")
    for name, s in splits.items():
        if s.coverage_decided < s.coverage_units:
            out.append(f"{name}: {s.coverage_decided}/{s.coverage_units} units have a decision.")
        # review M8 minor: recall rests on positives, forward rate on negatives
        few_pos = [f"{r.dimension}={r.value} ({r.n_positive})" for r in s.slices
                   if 0 < r.n_positive < SMALL_SLICE]  # fmt: skip
        few_neg = [f"{r.dimension}={r.value} ({r.n_units - r.n_positive})" for r in s.slices
                   if r.n_units - r.n_positive < SMALL_SLICE]  # fmt: skip
        if few_pos:
            out.append(f"{name}: slice recall from fewer than {SMALL_SLICE} positives: "
                       + ", ".join(few_pos))  # fmt: skip
        if few_neg:
            out.append(f"{name}: slice forward rate from fewer than {SMALL_SLICE} negatives: "
                       + ", ".join(few_neg))  # fmt: skip
    return out


# --- provenance (invariant 3) -------------------------------------------------------------------


def disjointness_scope(split_docs: Mapping[str, set[str]]) -> set[str]:
    """Scored docs that must not overlap calib's docs: every split except a split named `calib`,
    which may be scored descriptively (in-sample by definition)."""
    return {d for name, ids in split_docs.items() if name != "calib" for d in ids}


def verify_provenance(
    calib: CalibParams,
    units_sha256: str,
    docs_sha256: str,
    run_hashes: Mapping[str, str] | None,
    scored_doc_ids: set[str],
) -> None:
    """Refuse to score gold or calib that doesn't belong to this run.

    - units/docs must be the files the run was produced from (run meta config hashes);
    - calib must have been fit on the same units (same gold);
    - calib docs must be disjoint from scored docs, except for the labeled fixture_debug fit.
    """
    if run_hashes is not None:
        for key, got in (("units", units_sha256), ("docs", docs_sha256)):
            want = run_hashes.get(key)
            if want is None:
                raise ScoreError(f"run meta has no {key} hash; provenance can't be checked")
            if want != got:
                raise ScoreError(
                    f"{key} file differs from the one this run was produced from "
                    f"(run {want[:12]}, given {got[:12]})"
                )
    if calib.units_sha256 != units_sha256:
        raise ScoreError(
            f"calib was fit on different units (calib {calib.units_sha256[:12]}, "
            f"given {units_sha256[:12]})"
        )
    overlap = scored_doc_ids & set(calib.calib_doc_ids)
    if overlap and calib.fit_on != "fixture_debug":
        raise ScoreError(
            f"{len(overlap)} scored documents were used to fit calib, e.g. {sorted(overlap)[0]}"
        )


def verify_run_rows(decisions: Sequence[Decision], batch_size: int) -> None:
    """Every row of a run must carry that run's mode, so an old or foreign row (e.g. a batched row
    without `mode`, which defaults to batch1) can't enter the wrong speed statistic."""
    mode = "batch1" if batch_size == 1 else "batched"
    bad = [d.unit_id for d in decisions if d.mode != mode or d.batch_size > batch_size]
    if bad:
        raise ScoreError(
            f"{len(bad)} decisions don't match the run's mode {mode!r} (batch {batch_size}), "
            f"e.g. {bad[0]}"
        )


# --- stage entry -------------------------------------------------------------------------------


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_decisions(path: Path) -> list[Decision]:
    with path.open(encoding="utf-8") as f:
        return [Decision.model_validate_json(line) for line in f if line.strip()]


def score(
    decisions: Sequence[Decision],
    units: Sequence[Unit],
    docs: Sequence[Document],
    calib: CalibParams,
    policy: Policy,
    split_docs: Mapping[str, set[str]],
    hw: HwInfo | None,
    hashes: Mapping[str, str],
    extra_caveats: Sequence[str] = (),
    calib_commit: tuple[str, str] = ("not-verified", ""),
    batched: Sequence[Decision] = (),
    doc_level: bool = False,
) -> Scores:
    unit_map = {u.id: u for u in units}
    doc_map = {d.id: d for d in docs}
    rows = build_rows(decisions, unit_map, doc_map, calib, policy)
    splits: dict[str, SplitScores] = {}
    for name, doc_ids in split_docs.items():
        split_rows = [r for r in rows if r.doc.id in doc_ids]
        if not split_rows:
            raise ScoreError(f"split {name!r} has no decided units")
        n_units = sum(u.doc_id in doc_ids for u in units)
        splits[name] = split_scores(split_rows, n_units, calib, policy)
    live = [d for d in decisions if not d.warmup]
    context = RunContext(
        arm=calib.arm,
        qs=calib.qs,
        splits=list(split_docs),
        docs_sha256=hashes["docs"],
        units_sha256=hashes["units"],
        decisions_sha256=hashes["decisions"],
        calib_hash=calib.content_hash,
        calib_auroc_pii=calib.calib_auroc_pii,
        calib_fit_on=calib.fit_on,
        calib_temperature_fallbacks=dict(calib.temperature_fallbacks),
        calib_commit=calib_commit[0],
        calib_committed_at=calib_commit[1],
        batched_decisions_sha256=hashes.get("batched_decisions"),
        doc_level=doc_level,
        hw=hw,
        laya_version=hw.laya if hw else "unknown",
        checkpoints=sorted({d.checkpoint for d in live}),
        checkpoint_revs=sorted({d.checkpoint_rev for d in live}),
        created_at=datetime.now(UTC).isoformat(timespec="microseconds"),  # D-019
    )
    sp = speed(decisions, unit_map, hw, batched)
    return Scores(
        context=context,
        splits=splits,
        speed=sp,
        caveats=[
            *extra_caveats,
            *(["calib commit not verified (D-019)"] if calib_commit[0] == "not-verified" else []),
            *caveats(splits, calib, doc_level, sp),
        ],
    )


def routed(
    decisions: Sequence[Decision],
    units: Sequence[Unit],
    docs: Sequence[Document],
    calib: CalibParams,
    policy: Policy,
    split_docs: Mapping[str, set[str]],
) -> list[RoutedDecision]:
    """Per-unit routes for the scored splits (the HUD replay, audit C7), in run order."""
    split_of = {d: name for name, ids in split_docs.items() for d in ids}
    rows = build_rows(decisions, {u.id: u for u in units}, {d.id: d for d in docs}, calib, policy)
    return [
        RoutedDecision(decision=r.decision, route=r.route, triggers=r.triggers,
                       calibrated_probs=r.cal, split=split_of[r.doc.id])
        for r in rows
        if r.doc.id in split_of
    ]  # fmt: skip


def with_timing(scores: Scores, rows: Sequence[Decision], hardware: str, sha256: str) -> Scores:
    """Attach a timing-only run's latency (speed only, never accuracy) with its hardware label."""
    live = [d for d in rows if not d.warmup and d.mode == "batch1"]
    sp = scores.speed.model_copy(update={
        "timing": latency_stats([d.latency_ms for d in live]),
        "timing_hardware": hardware,
        "timing_drift": drift(live),
    })  # fmt: skip
    ctx = scores.context.model_copy(update={"timing_decisions_sha256": sha256})
    return scores.model_copy(update={"speed": sp, "context": ctx})
