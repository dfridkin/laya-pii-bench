"""Build `fixtures/mini/docs.jsonl` from hand-labeled sources in `fixtures/mini/src/*.yaml`."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from bench.domain import Document
from bench.markup import resolve


def load_source(path: Path) -> Document:
    raw: dict[str, Any] = yaml.safe_load(path.read_text(encoding="utf-8"))
    text, spans, negatives = resolve(raw.pop("text"))
    return Document.model_validate(
        raw | {"text": text, "spans": [s.model_dump() for s in spans], "negatives": negatives}
    )


def build(src_dir: Path) -> list[Document]:
    return [load_source(p) for p in sorted(src_dir.glob("*.yaml"))]


def dumps(docs: list[Document]) -> str:
    # defaults (e.g. Span.value = None, added after the fixture was locked) are omitted so the
    # locked docs.jsonl stays byte-identical
    return "".join(d.model_dump_json(exclude_defaults=True) + "\n" for d in docs)


def write(src_dir: Path, out: Path) -> int:
    docs = build(src_dir)
    out.write_text(dumps(docs), encoding="utf-8")
    return len(docs)
