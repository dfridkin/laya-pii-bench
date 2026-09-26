"""Print English-tokenizer positions of every span in a fixture doc (tuning aid for fx06)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from tokenizers import Tokenizer

from bench.fixture import load_source


def main(src: str) -> None:
    doc = load_source(Path(src))
    lock = json.loads(Path("models.lock.json").read_text())
    tok = Tokenizer.from_file(lock["english"]["path"] + "/tokenizer/tokenizer.json")
    enc = tok.encode(doc.text, add_special_tokens=False)
    print(f"{doc.id}: {len(enc.ids)} tokens")
    for s in doc.spans:
        idx = [i for i, (a, b) in enumerate(enc.offsets) if a < s.end and b > s.start]
        print(f"  tokens {idx[0]:>4}-{idx[-1]:<4} {doc.text[s.start : s.end]!r}")


if __name__ == "__main__":
    main(sys.argv[1])
