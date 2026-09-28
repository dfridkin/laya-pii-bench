"""Default artifact locations, namespaced by dataset so fixture runs never mix with real ones.

The main dataset (`data/docs.jsonl`) uses the paths in CLAUDE.md (`data/units/`, `runs/{arm}/{qs}`).
Any other docs file is a named dataset (its directory name, e.g. `fixtures/mini` -> `mini`) with
its own `data/{name}/units/` and `runs/{name}/{arm}/{qs}`.
"""

from __future__ import annotations

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MAIN_DOCS = PROJECT_ROOT / "data" / "docs.jsonl"  # anchored: the cwd never changes what "main" is
GENERATED_DOC_ID = re.compile(r"d\d{4,}")  # ids `bench gen` writes (generate/corpus.py)


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
