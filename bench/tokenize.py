"""Checkpoint tokenizers, loaded from the snapshot pinned in models.lock.json.

Token counts are raw text tokens without special tokens; truncation compares them to the arm's
state budget (docs/specs/gold-labels.md).
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from tokenizers import Tokenizer

_SUBDIR = {"english": "tokenizer", "multilingual": "multilingual/tokenizer"}


class Offsets(Protocol):
    def __call__(self, text: str) -> list[tuple[int, int]]: ...


@dataclass(frozen=True)
class CheckpointTokenizer:
    name: str
    tokenizer: Tokenizer

    def __call__(self, text: str) -> list[tuple[int, int]]:
        return list(self.tokenizer.encode(text, add_special_tokens=False).offsets)


def load(checkpoint: str, models_lock: Path = Path("models.lock.json")) -> CheckpointTokenizer:
    if checkpoint not in _SUBDIR:
        raise ValueError(f"no tokenizer for checkpoint {checkpoint!r}")
    lock: dict[str, dict[str, str]] = json.loads(models_lock.read_text())
    path = Path(lock[checkpoint]["path"]) / _SUBDIR[checkpoint] / "tokenizer.json"
    return CheckpointTokenizer(checkpoint, Tokenizer.from_file(str(path)))
