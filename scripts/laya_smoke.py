"""M0 smoke: preload the English checkpoint, time one two-option choice question.

Runs the question CALLS times, drops the first WARMUP calls, prints the answer, its probabilities,
and p50/p95 latency of `predict` alone (docs/specs/laya-runtime.md, timing protocol).
Loads the snapshot pinned in models.lock.json so the revision is exact.
"""

from __future__ import annotations

import json
import os
import statistics
import time
from pathlib import Path

os.environ.setdefault("USE_TF", "0")

import laya

CALLS = 20
WARMUP = 5
MAX_LEN = 512
HEAD_MAX_LEN = 192

# Fictional world only (D-010): Faker-style name, synthetic site and subject number.
STATE = (
    "Subject 1001-0023 (Marta Kowalczyk, DOB 14-Mar-1961) was seen at Site 1001 on Day 15. "
    "Mild headache reported after FTX-2417 dosing; resolved without treatment."
)
QUESTIONS = {
    "pii_present": {
        "type": "choice",
        "instructions": (
            "Does this text contain personal identifiers of a real individual (patient or site "
            "staff), such as names, contact details, record numbers, birth dates, or study "
            "subject numbers?"
        ),
        "criteria": {
            "A": "yes, it contains at least one personal identifier",
            "B": "no, it contains no personal identifiers",
        },
    }
}


def main() -> None:
    lock = json.loads(Path("models.lock.json").read_text())
    ckpt = lock["english"]
    t0 = time.perf_counter()
    agent = laya.load(ckpt["path"])
    load_s = time.perf_counter() - t0

    times_ms: list[float] = []
    res = None
    for _ in range(CALLS):
        start = time.perf_counter_ns()
        res = agent.predict(STATE, QUESTIONS, max_len=MAX_LEN, head_max_len=HEAD_MAX_LEN)
        times_ms.append((time.perf_counter_ns() - start) / 1e6)
    assert res is not None

    measured = sorted(times_ms[WARMUP:])
    p50 = statistics.median(measured)
    p95 = measured[min(len(measured) - 1, round(0.95 * (len(measured) - 1)))]
    ans = res["answers"]["pii_present"]
    total = sum(ans["probabilities"].values())

    print(f"checkpoint: {ckpt['repo']}@{ckpt['revision']} (english)")
    print(f"device: {agent.device.type}  load_s: {load_s:.1f}")
    print(f"answer: {ans['choice']}  probabilities: {ans['probabilities']}  sum: {total:.4f}")
    print(f"confidence: {ans['confidence']}  answer_confidence: {ans['answer_confidence']}")
    print(f"calls: {CALLS}  dropped: {WARMUP}  measured: {len(measured)}")
    print(f"p50_ms: {p50:.1f}  p95_ms: {p95:.1f}")
    if abs(total - 1.0) > 1e-3:
        raise SystemExit(f"probabilities sum to {total}, expected 1 +/- 1e-3")


if __name__ == "__main__":
    main()
