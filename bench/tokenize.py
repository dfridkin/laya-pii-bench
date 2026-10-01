"""Checkpoint tokenizers, loaded from the snapshot pinned in models.lock.json.

Token counts are raw text tokens without special tokens; truncation compares them to the arm's
state budget (docs/specs/gold-labels.md).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from tokenizers import Tokenizer

from bench.models import MODELS_LOCK, pinned

_SUBDIR = {
    "english": "tokenizer",
    "multilingual": "multilingual/tokenizer",
    "finetuned_english": "tokenizer",
}


class Offsets(Protocol):
    def __call__(self, text: str) -> list[tuple[int, int]]: ...


@dataclass(frozen=True)
class CheckpointTokenizer:
    name: str
    tokenizer: Tokenizer

    def __call__(self, text: str) -> list[tuple[int, int]]:
        return list(self.tokenizer.encode(text, add_special_tokens=False).offsets)


def load(checkpoint: str, models_lock: Path = MODELS_LOCK) -> CheckpointTokenizer:
    """Tokenizer of the locked checkpoint revision; `name` is `{checkpoint}@{revision}` so units
    record exactly which tokenizer counted them."""
    if checkpoint not in _SUBDIR:
        raise ValueError(f"no tokenizer for checkpoint {checkpoint!r}")
    pin = pinned(checkpoint, models_lock)
    path = pin.snapshot / _SUBDIR[checkpoint] / "tokenizer.json"
    return CheckpointTokenizer(f"{checkpoint}@{pin.revision}", Tokenizer.from_file(str(path)))
