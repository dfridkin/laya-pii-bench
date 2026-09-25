"""Pre-fetch Laya checkpoints into the Hugging Face cache and print their revisions.

Downloads the English checkpoint (repo root) and the multilingual subfolder only.
Safe to rerun; cached files are reused.
"""

from __future__ import annotations

import json
import os

os.environ.setdefault("USE_TF", "0")

from huggingface_hub import HfApi, snapshot_download

REPO = "convaiinnovations/laya"
TARGETS = {
    "english": None,  # repo root files only
    "multilingual": "multilingual/*",
}


def main() -> None:
    api = HfApi()
    info = api.model_info(REPO)
    root_patterns = ["*.json", "*.safetensors", "*.txt", "*.model", "*.py", "*.md"]
    out: dict[str, dict[str, str]] = {}
    for name, sub in TARGETS.items():
        patterns = [sub] if sub else root_patterns
        path = snapshot_download(REPO, allow_patterns=patterns, revision=info.sha)
        out[name] = {"repo": REPO, "subfolder": sub or "", "revision": info.sha or "", "path": path}
        print(f"{name}: {REPO}@{info.sha} -> {path}")
    with open("models.lock.json", "w") as f:
        json.dump(out, f, indent=2)
    print("wrote models.lock.json")


if __name__ == "__main__":
    main()
