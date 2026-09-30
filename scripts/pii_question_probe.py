"""M6 diagnostic (calib split only): does pii_present carry signal under three wordings?

Usage: uv run python scripts/pii_question_probe.py <arm>
Record: reports/audits/M6_pii_question_probe-20260929.md
"""

import json
import os
import random
import sys
from pathlib import Path

os.environ.setdefault("USE_TF", "0")
from bench.calibrate import gold_answer
from bench.config import load_arms
from bench.label import read_docs, read_units
from bench.laya_client import LayaClient
from bench.score import auroc

ARM = sys.argv[1]
N = 20
YES = "yes, it contains at least one personal identifier"
NO = "no, it contains no personal identifiers"
ORIG = (
    "Does this text contain personal identifiers of a real individual (patient or site staff), "
    "such as names, contact details, medical record numbers, or birth dates?"
)
NOREAL = (
    "Does this text contain personal identifiers of an individual (patient or site staff), "
    "such as names, contact details, medical record numbers, or birth dates?"
)
VARIANTS = {  # name -> (instructions, criteria, key meaning "yes")
    "original": (ORIG, {"A": YES, "B": NO}, "A"),
    "swapped": (ORIG, {"A": NO, "B": YES}, "B"),
    "no_real": (NOREAL, {"A": YES, "B": NO}, "A"),
}

spec = load_arms(Path("config/arms.yaml")).arms[ARM]
split = json.loads(Path("data/splits.json").read_text())["doc_split"]
docs = {d.id: d for d in read_docs(Path("data/docs.jsonl"))}
units = [u for u in read_units(Path(f"data/units/{ARM}.jsonl")) if split[u.doc_id] == "calib"]
rng = random.Random(0)
pos = [u for u in units if gold_answer(u.gold, "pii_present") == "A"]
neg = [u for u in units if gold_answer(u.gold, "pii_present") == "B"]
sample = rng.sample(pos, min(N, len(pos))) + rng.sample(neg, min(N, len(neg)))
texts = [docs[u.doc_id].text[u.start : u.end] for u in sample]
gold = [gold_answer(u.gold, "pii_present") == "A" for u in sample]
for name, (instr, crit, yes_key) in VARIANTS.items():
    q = {"pii_present": {"type": "choice", "instructions": instr, "criteria": crit}}
    c = LayaClient(spec.checkpoint, q, spec.max_len, spec.head_max_len)
    p_yes = []
    for t in texts:
        res, _ = c.predict(t)
        p_yes.append(float(res["answers"]["pii_present"]["probabilities"][yes_key]))
    picks_a = sum((p if yes_key == "A" else 1 - p) > 0.5 for p in p_yes) / len(p_yes)
    print(
        json.dumps(
            {
                "arm": ARM,
                "variant": name,
                "n": len(p_yes),
                "auroc_yes": auroc(p_yes, gold),
                "share_pick_A": round(picks_a, 2),
                "mean_p_yes_gold_yes": round(
                    sum(p for p, g in zip(p_yes, gold, strict=True) if g) / sum(gold), 3
                ),
                "mean_p_yes_gold_no": round(
                    sum(p for p, g in zip(p_yes, gold, strict=True) if not g)
                    / (len(gold) - sum(gold)),
                    3,
                ),
            }
        ),
        flush=True,
    )
    del c
