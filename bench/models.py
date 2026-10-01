"""Pinned checkpoints: models.lock.json holds repo + revision; paths are resolved at load time.

The lock's `path` field is informational (it is machine-specific). Loading goes through the local
Hugging Face cache for the locked revision, so the same lock works on any machine that has run
`make bootstrap`, and a newer upstream revision can never be picked up silently.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

MODELS_LOCK = Path("models.lock.json")


@dataclass(frozen=True)
class Pinned:
    name: str
    repo: str
    revision: str
    snapshot: Path  # local snapshot root for `revision`


REQUIRED = ("rl_agent_config.json", "model.safetensors", "tokenizer/tokenizer.json")
SUBFOLDER = {"english": "", "multilingual": "multilingual"}


LOCAL = "local"  # a checkpoint trained here (arm C): `path` + `revision` = sha256 of its weights


def weights_sha256(directory: Path) -> str:
    import hashlib

    h = hashlib.sha256()
    with (directory / "model.safetensors").open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def _local(name: str, entry: dict[str, str], models_lock: Path) -> Pinned:
    base = Path(entry["path"])
    if not base.is_absolute():
        base = models_lock.resolve().parent / base
    missing = [f for f in REQUIRED if not (base / f).exists()]
    if missing:
        raise FileNotFoundError(f"{name}: {base} is missing {missing}")
    got = weights_sha256(base)
    if got != entry["revision"]:
        raise FileNotFoundError(
            f"{name}: weights in {base} hash to {got[:12]}, the lock pins {entry['revision'][:12]}"
        )
    return Pinned(name, LOCAL, entry["revision"], base)


def pinned(name: str, models_lock: Path = MODELS_LOCK) -> Pinned:
    """Snapshot of the locked revision in the local HF cache (offline, no revision resolution);
    a local checkpoint (arm C) is verified against its pinned weights hash."""
    import huggingface_hub

    entry: dict[str, str] = json.loads(models_lock.read_text())[name]
    if entry["repo"] == LOCAL:
        return _local(name, entry, models_lock)
    try:
        scan: Any = getattr(huggingface_hub, "scan_cache_dir")()  # noqa: B009 (untyped result)
    except Exception as e:
        raise FileNotFoundError(f"no local HF cache ({e}); run `make bootstrap`") from e
    root: Path | None = None
    for repo in scan.repos:
        if repo.repo_id == entry["repo"]:
            for rev in repo.revisions:
                if rev.commit_hash == entry["revision"]:
                    root = Path(rev.snapshot_path)
    base = root / SUBFOLDER.get(name, "") if root is not None else None
    missing = [f for f in REQUIRED if base is None or not (base / f).exists()]
    if missing:
        raise FileNotFoundError(
            f"{name}@{entry['revision'][:12]} is not complete in the local HF cache (missing "
            f"{missing}); run `make bootstrap`"
        )
    assert root is not None
    return Pinned(name, entry["repo"], entry["revision"], root)
