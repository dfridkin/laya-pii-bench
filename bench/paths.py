"""Default artifact locations, namespaced by dataset so fixture runs never mix with real ones.

The main dataset (`data/docs.jsonl`) uses the paths in CLAUDE.md (`data/units/`, `runs/{arm}/{qs}`).
Any other docs file is a named dataset (its directory name, e.g. `fixtures/mini` -> `mini`) with
its own `data/{name}/units/` and `runs/{name}/{arm}/{qs}`.
"""

from __future__ import annotations

from pathlib import Path

MAIN_DOCS = Path("data/docs.jsonl")


def dataset_name(docs: Path) -> str:
    return "main" if docs.resolve() == MAIN_DOCS.resolve() else docs.resolve().parent.name


def units_dir(docs: Path) -> Path:
    name = dataset_name(docs)
    return Path("data/units") if name == "main" else Path("data") / name / "units"


def run_dir(docs: Path, arm: str, qs: str, batch_size: int = 1) -> Path:
    name = dataset_name(docs)
    base = Path("runs") if name == "main" else Path("runs") / name
    leaf = qs if batch_size == 1 else f"{qs}__batch{batch_size}"
    return base / arm / leaf
