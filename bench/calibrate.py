"""Calibrate stage: temperatures and routing thresholds, fit on calib only (invariant 3).

Temperatures are fit per (question, option count) by minimizing NLL. Decisions store laya's
probabilities (already rounded to 4 dp), so scaling acts on log-probabilities: p_k ∝ p_k^(1/T),
which equals logit scaling up to a per-row constant. Zero probabilities are clipped to EPS first.

Thresholds act on the calibrated p(pii_present = A):
- t_low: the largest threshold keeping recall >= recall_target, i.e. positives with p < t_low
  number at most floor((1 - target) * n_pos).
- t_high: the smallest observed p whose "p >= t" set has precision >= precision_target;
  None if none does (no p-based redaction). Never below t_low.

A temperature whose fit is degenerate falls back to T = 1 and is recorded in
`temperature_fallbacks`: calib accuracy 1.0 (NLL keeps falling as T -> 0, collapsing
probabilities to exactly 0/1) or 0.0, or an optimum on a bound of T_BOUNDS.
"""

from __future__ import annotations

import hashlib
import json
import math
from collections.abc import Callable, Iterable, Mapping, Sequence
from pathlib import Path
from typing import Any, Literal

import numpy as np
from scipy.optimize import minimize_scalar  # pyright: ignore[reportUnknownVariableType]

from bench.config import Policy
from bench.domain import CalibParams, Decision, GoldAnswers, PiiCategory, Unit

_minimize_scalar: Callable[..., Any] = minimize_scalar  # pyright: ignore[reportUnknownVariableType]

EPS = 1e-6
T_BOUNDS = (0.05, 20.0)
PII_QUESTION = "pii_present"


class CalibError(ValueError):
    pass


class CalibHashError(CalibError):
    pass


def gold_answer(gold: GoldAnswers, question: str) -> str:
    """Gold option key for a question id (qs_v1 fields, or qs_v2 `has_<category>`)."""
    if question in ("pii_present", "subject_role", "category", "doc_kind"):
        return str(getattr(gold, question))
    if question.startswith("has_"):
        return "A" if gold.categories_multi[PiiCategory(question.removeprefix("has_"))] else "B"
    raise CalibError(f"no gold for question {question!r}")


def apply_temperature(probs: Mapping[str, float], t: float) -> dict[str, float]:
    keys = list(probs)
    logp = np.log(np.clip(np.array([probs[k] for k in keys], dtype=float), EPS, None)) / t
    z = np.exp(logp - logp.max())
    # fsum is exactly rounded, hence order-independent: equal inputs give bit-identical outputs
    # whatever their position, so permuted rows tie exactly in AUROC and ECE binning.
    total = math.fsum(float(v) for v in z)
    return {k: float(v) / total for k, v in zip(keys, z, strict=True)}


def _nll(rows: np.ndarray, gold_idx: np.ndarray, t: float) -> float:
    logp = np.log(np.clip(rows, EPS, None)) / t
    logp -= logp.max(axis=1, keepdims=True)
    logz = np.log(np.exp(logp).sum(axis=1))
    return float(-(logp[np.arange(len(gold_idx)), gold_idx] - logz).mean())


def fit_temperature(rows: Sequence[Sequence[float]], gold_idx: Sequence[int]) -> float:
    if not rows:
        raise CalibError("no rows to fit a temperature on")
    r, g = np.array(rows, dtype=float), np.array(gold_idx, dtype=int)

    def objective(logt: float) -> float:
        return _nll(r, g, math.exp(logt))

    res = _minimize_scalar(
        objective,
        bounds=(math.log(T_BOUNDS[0]), math.log(T_BOUNDS[1])),
        method="bounded",
        options={"xatol": 1e-10},
    )
    return math.exp(float(res.x))


CURVE_TARGETS = (0.90, 0.95, 0.98, 0.99, 0.995)  # D-007 amended: the headline is this curve


def fit_t_low(p_positive: Sequence[float], recall_target: float) -> float:
    if not p_positive:
        raise CalibError("no positive units: cannot fit t_low")
    allowed_misses = math.floor((1 - recall_target) * len(p_positive) + 1e-9)
    return sorted(p_positive)[allowed_misses]


def fit_t_high(
    p: Sequence[float], positive: Sequence[bool], target: float, t_low: float
) -> float | None:
    for t in sorted(set(p)):
        sel = [y for q, y in zip(p, positive, strict=True) if q >= t]
        if sel and sum(sel) / len(sel) >= target:
            return max(t, t_low)
    return None


def fit_or_fallback(
    rows: Sequence[Sequence[float]], gold_idx: Sequence[int]
) -> tuple[float, str | None]:
    """Temperature for one (question, n_options) key, or (1.0, reason) if the fit is degenerate."""
    correct = sum(int(np.argmax(r)) == g for r, g in zip(rows, gold_idx, strict=True))
    if correct == len(rows):
        return 1.0, "calib accuracy 1.0"
    if correct == 0:
        return 1.0, "calib accuracy 0.0"
    t = fit_temperature(rows, gold_idx)
    # A bounded optimizer on a flat objective stops short of the bound (e.g. T = 0.06), so compare
    # objective values: if a bound is at least as good as the fit, the fit is running into it.
    r, g = np.array(rows, dtype=float), np.array(gold_idx, dtype=int)
    at_t = _nll(r, g, t)
    if any(_nll(r, g, b) <= at_t + 1e-9 for b in T_BOUNDS):
        return 1.0, f"fit hit bound ({t:.4g})"
    return t, None


def calib_key(question: str, n_options: int) -> str:
    return f"{question}:{n_options}"


def content_hash(params: CalibParams) -> str:
    body = params.model_dump(mode="json", exclude={"content_hash"})
    if not body["t_low_curve"]:  # added in M6 (D-007 amended): files fit before it keep their hash
        del body["t_low_curve"]
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def fit(
    decisions: Iterable[Decision],
    units: Mapping[str, Unit],
    policy: Policy,
    fit_on: Literal["calib", "fixture_debug"],
    *,
    input_hashes: Mapping[str, str],
) -> CalibParams:
    """`input_hashes`: sha256 of the decisions and units files ("decisions", "units")."""
    live = [d for d in decisions if not d.warmup]
    if not live:
        raise CalibError("no non-warmup decisions")
    seen: set[str] = set()
    for d in live:
        if d.unit_id in seen:
            raise CalibError(f"duplicate decision for unit {d.unit_id}")
        seen.add(d.unit_id)
    arms, qss = {d.arm for d in live}, {d.qs for d in live}
    if len(arms) != 1 or len(qss) != 1:
        raise CalibError(f"decisions mix arms {arms} or question sets {qss}")
    missing = [d.unit_id for d in live if d.unit_id not in units]
    if missing:
        raise CalibError(f"{len(missing)} decisions have no unit, e.g. {missing[0]}")

    rows: dict[str, list[list[float]]] = {}
    gold_idx: dict[str, list[int]] = {}
    for d in live:
        for a in d.answers:
            keys = list(a.probs)
            k = calib_key(a.question, len(keys))
            rows.setdefault(k, []).append([a.probs[o] for o in keys])
            gold_idx.setdefault(k, []).append(
                keys.index(gold_answer(units[d.unit_id].gold, a.question))
            )
    temps: dict[str, float] = {}
    fallbacks: dict[str, str] = {}
    for k in sorted(rows):
        temps[k], reason = fit_or_fallback(rows[k], gold_idx[k])
        if reason:
            fallbacks[k] = reason

    p_pii: list[float] = []
    positive: list[bool] = []
    for d in live:
        a = next((a for a in d.answers if a.question == PII_QUESTION), None)
        if a is None:
            raise CalibError(f"{d.unit_id}: no {PII_QUESTION} answer")
        p_pii.append(apply_temperature(a.probs, temps[calib_key(PII_QUESTION, len(a.probs))])["A"])
        positive.append(units[d.unit_id].gold.pii_present == "A")
    t_low = fit_t_low(
        [p for p, y in zip(p_pii, positive, strict=True) if y], policy.routing.recall_target
    )
    t_high = fit_t_high(p_pii, positive, policy.routing.precision_target, t_low)
    pos_p = [p for p, y in zip(p_pii, positive, strict=True) if y]
    curve = {f"{t:g}": fit_t_low(pos_p, t)
             for t in sorted({*CURVE_TARGETS, policy.routing.recall_target})}  # fmt: skip

    params = CalibParams(
        arm=arms.pop(),
        qs=qss.pop(),
        temperatures=temps,
        temperature_fallbacks=fallbacks,
        t_low=t_low,
        t_high=t_high,
        recall_target=policy.routing.recall_target,
        precision_target=policy.routing.precision_target,
        t_low_curve=curve,
        fit_on=fit_on,
        decisions_sha256=input_hashes["decisions"],
        units_sha256=input_hashes["units"],
        calib_doc_ids=sorted({units[d.unit_id].doc_id for d in live}),
        content_hash="",
    )
    return params.model_copy(update={"content_hash": content_hash(params)})


def write(params: CalibParams, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(params.model_dump_json(indent=2) + "\n", encoding="utf-8")


def load_verified(path: Path, allow_debug: bool = False) -> CalibParams:
    """Load frozen calib params; refuse a hash mismatch or (unless allowed) a debug fit."""
    params = CalibParams.model_validate_json(path.read_text(encoding="utf-8"))
    if content_hash(params) != params.content_hash:
        raise CalibHashError(f"{path}: content hash mismatch; calib file was modified after fit")
    if params.fit_on != "calib" and not allow_debug:
        raise CalibError(f"{path}: fit_on={params.fit_on!r}; pass --allow-debug-calib to use it")
    return params
