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
    Decision,
    Document,
    FailureCase,
    Headline,
    HwInfo,
    Interval,
    LatencyStats,
    MultiLabelMetrics,
    QuestionMetrics,
    ReliabilityBin,
    Route,
    RoutingMetrics,
    RunContext,
    Scores,
    SliceRow,
    SpeedMetrics,
    SplitScores,
    Unit,
)
from bench.label import member_spans

ECE_BINS = 15
SMALL_SLICE = 30
PERTURBATION_TAGS = ("table", "ocr_noise", "line_wrap", "headers_footers", "email_quoting")


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
    )


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
        ("truncated", "yes" if r.unit.truncated or r.decision.truncated_questions else "no"),
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


def highlight(r: Row) -> str:
    """Unit text as a markdown blockquote, gold spans (clipped to the unit) in bold."""
    u, text = r.unit, r.doc.text
    parts: list[str] = []
    pos = u.start
    for s in sorted(member_spans(r.doc.spans, u.start, u.end), key=lambda s: s.start):
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
            text_markdown=highlight(r),
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
    )


def speed(
    decisions: Sequence[Decision], units: Mapping[str, Unit], hw: HwInfo | None
) -> SpeedMetrics:
    live = [d for d in decisions if not d.warmup]
    b1 = [d for d in live if d.mode == "batch1"]
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
        batched=latency_stats([d.latency_ms for d in live if d.mode == "batched"]),
        per_doc_ms=latency_stats(list(per_doc.values())),
        warmup_excluded=len(decisions) - len(live),
    )


def caveats(splits: Mapping[str, SplitScores], calib: CalibParams) -> list[str]:
    out: list[str] = []
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
        small = [f"{r.dimension}={r.value} (n={r.n_units})" for r in s.slices if r.small_sample]
        if small:
            out.append(f"{name}: slices with n < {SMALL_SLICE}: " + ", ".join(small))
    return out


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
        calib_fit_on=calib.fit_on,
        calib_temperature_fallbacks=dict(calib.temperature_fallbacks),
        hw=hw,
        laya_version=hw.laya if hw else "unknown",
        checkpoints=sorted({d.checkpoint for d in live}),
        checkpoint_revs=sorted({d.checkpoint_rev for d in live}),
        created_at=datetime.now(UTC).isoformat(timespec="seconds"),
    )
    return Scores(
        context=context,
        splits=splits,
        speed=speed(decisions, unit_map, hw),
        caveats=caveats(splits, calib),
    )
