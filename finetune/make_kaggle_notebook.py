"""Write finetune/kaggle_m8.ipynb: train arm C and run every M8 accuracy run on Kaggle 2x T4 (D-022).

Usage: python finetune/make_kaggle_notebook.py
"""

from __future__ import annotations

import json
from pathlib import Path

LAYA = "0.3.20"  # the version the M2 runs used (hw.json); training and inference stay on it
RUNS_GPU0 = [("A", "qs_v1"), ("A", "qs_v2"), ("B1", "qs_v1"), ("B1", "qs_v2"), ("B2", "qs_v1"),
             ("B2", "qs_v2")]  # fmt: skip
RUNS_GPU1 = [("B3", "qs_v1"), ("B3", "qs_v2"), ("B4", "qs_v1"), ("B4", "qs_v2"), ("C", "qs_v1"),
             ("C", "qs_v2")]  # fmt: skip

CELLS: list[tuple[str, str]] = [
    ("markdown", f"""# laya-pii-bench M8 on Kaggle (D-022)

Trains **arm C** (Laya English, fine-tuned on train-split units only) and runs every M8 **accuracy**
run: arms A, B1-B4 and C, question sets qs_v1 and qs_v2, on the calib, test and holdout splits.
Latency headlines stay on the Apple M2; timings here are recorded and labeled as T4 hardware.

**Before running** (right sidebar, *Session options*):
1. *Accelerator*: **GPU T4 x2**. *Internet*: **On** (to download the Laya weights).
2. *Add input*: your private dataset holding `laya-pii-bundle.zip` (made by
   `scripts/kaggle_bundle.sh`).
3. Run all cells. About 1.5-2 h. The result is **`/kaggle/working/m8_outputs.zip`**: download it
   from the Output panel. Nothing is pushed to the Hugging Face Hub.

All data is synthetic (fictional sponsor, sites and people)."""),
    ("code", """import subprocess, torch
print(subprocess.run(["nvidia-smi"], capture_output=True, text=True).stdout)
n = torch.cuda.device_count()
print("GPUs:", [torch.cuda.get_device_name(i) for i in range(n)])
assert n >= 2, "Select Accelerator: GPU T4 x2 in Session options"
"""),
    ("code", """# Unpack the bundle (Kaggle may have extracted the zip already)
import glob, os, shutil, zipfile
REPO = "/kaggle/working/laya-PII"
zips = glob.glob("/kaggle/input/**/laya-pii-bundle.zip", recursive=True)
roots = [os.path.dirname(p) for p in glob.glob("/kaggle/input/**/pyproject.toml", recursive=True)]
shutil.rmtree(REPO, ignore_errors=True)
if zips:
    zipfile.ZipFile(zips[0]).extractall(REPO)
elif roots:
    shutil.copytree(roots[0], REPO)
else:
    raise SystemExit("laya-pii-bundle not found under /kaggle/input: add the dataset as input")
os.chdir(REPO)
print(sorted(os.listdir(REPO)))
"""),
    ("code", f"""# Install the benchmark (and the same laya version as the M2 runs)
!pip install -q -e /kaggle/working/laya-PII "laya=={LAYA}"
import laya, transformers, torch
print("laya", laya.__version__, "| transformers", transformers.__version__, "| torch", torch.__version__)
assert laya.__version__ == "{LAYA}"
"""),
    ("code", """%%bash
set -e
cd /kaggle/working/laya-PII
export USE_TF=0
python scripts/download_models.py          # the revision pinned in models.lock.json
bench finetune-verify                     # M8 gate 1: every record is train-split
bench hw --out hw.json
cat hw.json
"""),
    ("code", """%%bash
set -e
cd /kaggle/working/laya-PII
export USE_TF=0 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
MD=$(python -c "from bench.models import pinned; print(pinned('english').snapshot)")
python finetune/prepare.py "$MD" finetune/data /kaggle/working/train_items.pt
torchrun --standalone --nproc_per_node=2 finetune/train_ddp.py "$MD" \\
  /kaggle/working/train_items.pt finetune/data/manifest.json finetune/output/laya-pii-c 3
cat finetune/output/laya-pii-c/training_meta.json
"""),
    ("code", """%%bash
set -e
cd /kaggle/working/laya-PII
export USE_TF=0
bench pin-checkpoint --path finetune/output/laya-pii-c   # M8 gate 3: weights hash in the lock
bench label --arm C                                       # C's units, with C's own tokenizer
"""),
    ("code", f"""# All accuracy runs: two queues, one per GPU (batch-1, warmups excluded, hw recorded)
import os, subprocess, time
os.chdir("/kaggle/working/laya-PII")
os.makedirs("/kaggle/working/logs", exist_ok=True)
queues = {{"0": {RUNS_GPU0!r}, "1": {RUNS_GPU1!r}}}
def script(runs):
    return " && ".join(
        f"bench run --arm {{a}} --qs {{q}} --release-every 25 > /kaggle/working/logs/{{a}}_{{q}}.log 2>&1"
        for a, q in runs)
procs = {{g: subprocess.Popen(script(r), shell=True,
                             env={{**os.environ, "CUDA_VISIBLE_DEVICES": g, "USE_TF": "0"}})
         for g, r in queues.items()}}
t0 = time.time()
while any(p.poll() is None for p in procs.values()):
    time.sleep(60)
    started = len(os.popen("ls runs/*/*/meta.json 2>/dev/null").read().split())
    print(f"{{(time.time() - t0) / 60:.0f}} min: {{started}} runs started", flush=True)
print({{g: p.returncode for g, p in procs.items()}})
assert all(p.returncode == 0 for p in procs.values()), "a run failed: see /kaggle/working/logs"
"""),
    ("code", """%%bash
set -e
cd /kaggle/working/laya-PII
for d in runs/*/*/; do
  n=$(grep -c '"warmup": *false\\|"warmup":false' "$d/decisions.jsonl" || true)
  echo "$d $n decisions"
done
sha256sum finetune/output/laya-pii-c/model.safetensors
cd /kaggle/working
rm -f m8_outputs.zip
(cd laya-PII && zip -q -r ../m8_outputs.zip runs data/units/C.jsonl hw.json models.lock.json \\
   finetune/output/laya-pii-c -x 'finetune/output/laya-pii-c/checkpoint_latest/*')
zip -q -r m8_outputs.zip logs
ls -lh m8_outputs.zip
"""),
]


def main() -> None:
    nb = {
        "cells": [
            {"cell_type": t, "metadata": {}, "source": src.splitlines(keepends=True),
             **({"outputs": [], "execution_count": None} if t == "code" else {})}
            for t, src in CELLS
        ],  # fmt: skip
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python"},
            "kaggle": {"accelerator": "nvidiaTeslaT4", "isInternetEnabled": True},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    out = Path(__file__).with_name("kaggle_m8.ipynb")
    out.write_text(json.dumps(nb, indent=1) + "\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
