"""Export the domain model as one JSON Schema (`schema/domain.json`) for the HUD's TS types.

One combined schema, so shared types (Span, GoldAnswers, ...) are declared once in TypeScript.
Field-level titles are dropped: json-schema-to-typescript turns each into a named alias.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

from pydantic.json_schema import models_json_schema

from bench.domain import EXPORTED

SCHEMA_FILE = "domain.json"


def _drop_property_titles(node: Any) -> Any:
    if isinstance(node, list):
        return [_drop_property_titles(v) for v in cast(list[Any], node)]
    if not isinstance(node, dict):
        return node
    out: dict[str, Any] = {}
    for key, value in cast(dict[str, Any], node).items():
        if key == "properties":
            props = cast(dict[str, dict[str, Any]], value)
            out[key] = {
                name: {k: _drop_property_titles(v) for k, v in prop.items() if k != "title"}
                for name, prop in props.items()
            }
        else:
            out[key] = _drop_property_titles(value)
    return out


def build() -> dict[str, Any]:
    _, top = models_json_schema([(m, "validation") for m in EXPORTED], title="Domain")
    return {
        "title": "Domain",
        "description": "laya-pii-bench domain model (bench/domain.py). Generated; do not edit.",
        "type": "object",
        "additionalProperties": False,
        "$defs": _drop_property_titles(top["$defs"]),
    }


def export(out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / SCHEMA_FILE
    path.write_text(json.dumps(build(), indent=2, sort_keys=True, ensure_ascii=False) + "\n")
    return path
