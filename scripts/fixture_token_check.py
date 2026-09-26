"""Print English-tokenizer positions of every span in a fixture doc (tuning aid for fx06)."""

from __future__ import annotations

import sys
from pathlib import Path

from tokenizers import Tokenizer

from bench.fixture import load_source
from bench.models import pinned


def main(src: str) -> None:
    doc = load_source(Path(src))
    tok = Tokenizer.from_file(str(pinned("english").snapshot / "tokenizer" / "tokenizer.json"))
    enc = tok.encode(doc.text, add_special_tokens=False)
    print(f"{doc.id}: {len(enc.ids)} tokens")
    for s in doc.spans:
        idx = [i for i, (a, b) in enumerate(enc.offsets) if a < s.end and b > s.start]
        print(f"  tokens {idx[0]:>4}-{idx[-1]:<4} {doc.text[s.start : s.end]!r}")


if __name__ == "__main__":
    main(sys.argv[1])
