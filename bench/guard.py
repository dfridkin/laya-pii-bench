"""D-013 guard: fixture-only flags never touch the main corpus, whatever the path or meta say.

The main corpus is recognized by content: a document whose id and text hash match a document of
`data/docs.jsonl`. A copy of the corpus under another name, or decisions without a run meta.json,
are still the main corpus, so `--debug-fit-all`, `--allow-debug-calib` and `--allow-no-meta` are
refused for them, and `bench run` refuses to treat them as a named dataset (which would skip the
split filter).
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Iterable
from pathlib import Path

from bench.domain import Document
from bench.paths import MAIN_DOCS


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def main_index(main_docs: Path = MAIN_DOCS) -> dict[str, str]:
    """Document id -> text sha256 of the main corpus (empty if it hasn't been generated)."""
    if not main_docs.exists():
        return {}
    out: dict[str, str] = {}
    with main_docs.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                d = json.loads(line)
                out[str(d["id"])] = _sha(str(d["text"]))
    return out


def main_docs_in(docs: Iterable[Document], main_docs: Path = MAIN_DOCS) -> list[str]:
    """Ids of `docs` that are main-corpus documents (same id and text)."""
    idx = main_index(main_docs)
    return sorted(d.id for d in docs if idx.get(d.id) == _sha(d.text))
