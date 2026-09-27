"""Grammar-generated clean filler (docs/specs/generator.md). No people, places, dates or IDs."""

from __future__ import annotations

import random
import re
from pathlib import Path

import yaml

_GRAMMAR: dict[str, dict[str, list[str]]] = yaml.safe_load(
    (Path(__file__).parent / "data" / "filler_grammar.yaml").read_text(encoding="utf-8")
)["topics"]
_ALT = re.compile(r"\{([^{}]*)\}")
TOPICS = tuple(sorted(_GRAMMAR))


def expand(pattern: str, r: random.Random) -> str:
    return _ALT.sub(lambda m: r.choice(m.group(1).split("|")), pattern)


def paragraph(r: random.Random, topic: str, n: int | None = None) -> str:
    sentences = _GRAMMAR[topic]["sentences"]
    k = n if n is not None else r.randint(3, 6)
    return " ".join(expand(r.choice(sentences), r) for _ in range(k))


def title(r: random.Random, topic: str) -> str:
    return r.choice(_GRAMMAR[topic]["titles"])
