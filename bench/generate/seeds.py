"""Deterministic sub-seeds: every stochastic choice draws from an RNG keyed by (seed, *names).

Hashing the key (not sharing one RNG) keeps components independent: adding a template or a
subject does not shift the random stream of anything else (invariant 12).
"""

from __future__ import annotations

import hashlib
import random


def sub_seed(seed: int, *keys: object) -> int:
    h = hashlib.sha256(repr((seed, *keys)).encode()).digest()
    return int.from_bytes(h[:8], "big")


def rng(seed: int, *keys: object) -> random.Random:
    return random.Random(sub_seed(seed, *keys))
