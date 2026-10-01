#!/usr/bin/env bash
# M8 (D-022): everything the Kaggle notebook needs, as one zip to upload as a private dataset.
# Code + configs + the 1,600-doc corpus, its units and splits + arm C's training data. No runs,
# no archive, no HUD. Synthetic data only (fictional world, invariant 10).
set -euo pipefail
cd "$(dirname "$0")/.."
uv run bench finetune-verify
out=kaggle/laya-pii-bundle.zip
rm -f "$out"
zip -q -r "$out" pyproject.toml models.lock.json bench config scripts fixtures \
  finetune/prepare.py finetune/train_ddp.py finetune/data \
  data/docs.jsonl data/splits.json data/label_manifest.json data/gen_manifest.json data/units \
  -x '*/__pycache__/*' '*.pyc'
echo "$out: $(du -h "$out" | cut -f1)"
shasum -a 256 "$out"
