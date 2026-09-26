"""Pre-fetch Laya checkpoints into the Hugging Face cache at the pinned revision.

By default the revision in models.lock.json is kept (reproducible bootstrap). `--update` resolves
the repo's current revision instead and rewrites the lock; that changes tokenizers and weights,
so everything from `label` onward must be rerun. Safe to rerun.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

os.environ.setdefault("USE_TF", "0")

from huggingface_hub import HfApi, snapshot_download

REPO = "convaiinnovations/laya"
LOCK = Path("models.lock.json")
TARGETS = {
    "english": None,  # repo root files only
    "multilingual": "multilingual/*",
}
ROOT_PATTERNS = [
    "*.json",
    "*.safetensors",
    "*.txt",
    "*.model",
    "*.py",
    "*.md",
    "tokenizer/*",
    "encoder/*",
]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--update", action="store_true", help="move the lock to the repo's HEAD")
    args = ap.parse_args()
    lock: dict[str, dict[str, str]] = json.loads(LOCK.read_text()) if LOCK.exists() else {}
    head: str | None = None
    out: dict[str, dict[str, str]] = {}
    for name, sub in TARGETS.items():
        revision = lock.get(name, {}).get("revision")
        if args.update or not revision:
            head = head or HfApi().model_info(REPO).sha or ""
            if revision and revision != head:
                print(f"{name}: updating {revision[:12]} -> {head[:12]} (rerun label onward)")
            revision = head
        patterns = [sub] if sub else ROOT_PATTERNS
        path = snapshot_download(REPO, allow_patterns=patterns, revision=revision)
        out[name] = {"repo": REPO, "subfolder": sub or "", "revision": revision, "path": path}
        print(f"{name}: {REPO}@{revision} -> {path}")
    LOCK.write_text(json.dumps(out, indent=2) + "\n")
    print(f"wrote {LOCK} (path is informational; loading resolves repo + revision)")


if __name__ == "__main__":
    main()
