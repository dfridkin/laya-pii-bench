"""D-013 guard: fixture-only flags never touch the main corpus, whatever the path, cwd or meta say.

Decided by document id alone, never by text the caller supplies: a unit's document is main-corpus if
its id is in the project's `data/docs.jsonl` (anchored to the project root) or has the generator's
id format (`d0000`), so the guard fails closed when the corpus file is missing or moved. The fixture
uses its own ids (`fx01`). `--debug-fit-all`, `--allow-debug-calib` and `--allow-no-meta` are
refused for such units, and `bench run` refuses to run them as a named dataset (which would skip the
split filter).
"""

from __future__ import annotations

import json
from collections.abc import Iterable

from bench import paths


def main_ids() -> set[str]:
    """Document ids of the project's main corpus (empty if it hasn't been generated)."""
    if not paths.MAIN_DOCS.exists():
        return set()
    with paths.MAIN_DOCS.open(encoding="utf-8") as f:
        return {str(json.loads(line)["id"]) for line in f if line.strip()}


def main_doc_ids(doc_ids: Iterable[str]) -> list[str]:
    """The ids among `doc_ids` that belong (or may belong) to the main corpus."""
    known = main_ids()
    return sorted(i for i in set(doc_ids) if i in known or paths.GENERATED_DOC_ID.fullmatch(i))
