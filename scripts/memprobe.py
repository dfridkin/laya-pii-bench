"""Audit C4: can an arm's longest unit run on this machine without leaving the GPU?

One process per arm (so peaks don't mix): preload the arm's checkpoint, run its longest
calib/test/holdout unit through the question set with the most rows `CALLS` times, and report
latency, MPS memory, peak RSS, the device after the calls (laya falls back to CPU on an MPS memory
error) and whether autocast was on. Usage: uv run python scripts/memprobe.py B4 [qs_v2]
"""

from __future__ import annotations

import json
import os
import resource
import sys
import time
from pathlib import Path

os.environ.setdefault("USE_TF", "0")

import torch

from bench.config import load_arms, load_question_set
from bench.domain import Splits
from bench.label import read_docs, read_units
from bench.laya_client import LayaClient
from bench.questions import build

CALLS = 3


def main(arm: str, qs: str) -> None:
    cfg = load_arms(Path("config/arms.yaml"), Path("config/questions"))
    spec = cfg.arms[arm]
    splits = Splits.model_validate_json(Path("data/splits.json").read_text())
    keep = set(cfg.defaults.splits_to_run)
    units = [u for u in read_units(Path(f"data/units/{arm}.jsonl"))
             if splits.doc_split[u.doc_id] in keep]  # fmt: skip
    unit = max(units, key=lambda u: u.tokens)
    docs = {d.id: d for d in read_docs(Path("data/docs.jsonl"))}
    text = docs[unit.doc_id].text[unit.start : unit.end]
    questions = build(load_question_set(Path(f"config/questions/{qs}.yaml")), spec.checkpoint)
    t0 = time.perf_counter()
    client = LayaClient(spec.checkpoint, questions, spec.max_len, spec.head_max_len)
    load_s = time.perf_counter() - t0
    agent = client._agent  # pyright: ignore[reportPrivateUsage]
    out: dict[str, object] = {
        "arm": arm, "qs": qs, "rows": len(questions), "unit": unit.id, "unit_tokens": unit.tokens,
        "truncated": unit.truncated, "max_len": spec.max_len, "load_s": round(load_s, 1),
        "device_start": client.device, "amp_enabled_start": bool(agent.amp_enabled),
    }  # fmt: skip
    times: list[float] = []
    for _ in range(CALLS):
        _, ns = client.predict(text)
        times.append(ns / 1e9)
        print(f"call {len(times)}: {times[-1]:.2f}s on {client.current_device()}", flush=True)
    out |= {
        "call_s": [round(t, 2) for t in times],
        "device_end": client.current_device(),
        "amp_enabled_end": bool(agent.amp_enabled),
        "peak_rss_gb": round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**30, 2),
    }
    if torch.backends.mps.is_available():
        out |= {
            "mps_current_gb": round(torch.mps.current_allocated_memory() / 2**30, 2),
            "mps_driver_gb": round(torch.mps.driver_allocated_memory() / 2**30, 2),
        }
    out["ok"] = out["device_end"] == out["device_start"]
    print(json.dumps(out))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "qs_v2")
