"""Tokenize arm C's training records into laya training items (adapted from laya's Kaggle notebook).

Usage: python finetune/prepare.py <model_dir> <data_dir> <items.pt>

Reads `records.jsonl`, `texts.jsonl` and `manifest.json` written by `bench finetune-data`
(train-split units only, verified by `bench finetune-verify`). Each record becomes one item via
laya's own `build_sequence` at arm C's lengths (max_len 512, head_max_len 192, config/arms.yaml),
with the record's one-hot target. Items carry `holdout` = their document is in the manifest's
temperature hold-out (train documents kept out of gradient steps for the checkpoint's own
temperatures, as the notebook does).
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

os.environ.setdefault("USE_TF", "0")

import torch
from laya.agent import _fix_tokenizer_config  # pyright: ignore[reportMissingTypeStubs]
from laya.common import (  # pyright: ignore[reportMissingTypeStubs]
    QTYPES,
    build_sequence,
    render_options,
)
from transformers import AutoTokenizer

MAX_LEN, HEAD_MAX_LEN = 512, 192  # arm C (config/arms.yaml), = arm A


def main(model_dir: str, data_dir: str, out: str) -> None:
    _fix_tokenizer_config(model_dir)
    tok = AutoTokenizer.from_pretrained(os.path.join(model_dir, "tokenizer"))
    d = Path(data_dir)
    manifest = json.loads((d / "manifest.json").read_text())
    texts = {
        r["unit_id"]: r["text"]
        for r in map(json.loads, (d / "texts.jsonl").read_text().splitlines())
    }
    holdout = set(manifest["temperature_holdout_doc_ids"])
    items, skipped = [], 0
    for line in (d / "records.jsonl").read_text().splitlines():
        r = json.loads(line)
        crit = r["criteria"]
        q = {"t": r["qtype"], "ins": r["instructions"], "crit": crit}
        keys = list(crit) if r["qtype"] == "choice" else [str(i) for i in range(len(crit))]
        seq, markers = build_sequence(tok, texts[r["unit_id"]], q, MAX_LEN, HEAD_MAX_LEN)
        if len(markers) != len(render_options({"t": r["qtype"], "crit": crit})):
            skipped += 1
            continue
        target = [float(r["target"][k]) for k in keys]
        items.append({
            "ids": seq, "markers": markers, "qtype": QTYPES[r["qtype"]], "target": target,
            "label": keys.index(r["label"]), "holdout": r["doc_id"] in holdout,
            "question": r["question"],
        })  # fmt: skip
    torch.save(items, out)
    n_hold = sum(it["holdout"] for it in items)
    print(f"{len(items)} items ({n_hold} temperature hold-out, {skipped} skipped) -> {out}")
    if skipped:
        raise SystemExit(f"{skipped} records did not tokenize to their option markers")


if __name__ == "__main__":
    main(*sys.argv[1:4])
