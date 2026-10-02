"""Lexical baselines for arm C (M8 results review B1): what plain n-gram features learn from the
same training units.

`run` fits a TF-IDF + logistic regression on arm C's own training units (finetune/data: texts and
their pii_present labels; train split only) and writes p(pii_present = A) for every
calib/test/holdout unit of the unit arm as an ordinary run directory (runs/{arm}/qs_v1), so the
baseline is calibrated on calib, frozen and scored exactly like a model arm. Deterministic: fixed
vectoriser settings and a deterministic solver.
"""

from __future__ import annotations

import hashlib
import json
import time
from collections.abc import Mapping
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Literal

from bench.domain import Answer, Decision, HwInfo, RunMeta

Kind = Literal["word", "char"]
ARM = {"word": "LW", "char": "LC"}  # baseline arm names (not model arms; no arms.yaml entry)
QUESTION = "pii_present"


def _vectorizer(kind: Kind) -> Any:
    from sklearn.feature_extraction.text import TfidfVectorizer

    if kind == "word":
        return TfidfVectorizer(ngram_range=(1, 2), min_df=1, sublinear_tf=True)
    return TfidfVectorizer(analyzer="char", ngram_range=(2, 5), min_df=1, sublinear_tf=True)


def training_set(data_dir: Path) -> tuple[list[str], list[int], str]:
    """C's training units (texts.jsonl) with their pii_present label (records.jsonl)."""
    texts = {
        r["unit_id"]: r["text"]
        for r in map(json.loads, (data_dir / "texts.jsonl").read_text().splitlines())
    }
    labels: dict[str, int] = {}
    for line in (data_dir / "records.jsonl").read_text().splitlines():
        r = json.loads(line)
        if r["question"] == QUESTION:
            labels[r["unit_id"]] = int(r["label"] == "A")
    ids = sorted(labels)
    return (
        [texts[i] for i in ids],
        [labels[i] for i in ids],
        hashlib.sha256((data_dir / "manifest.json").read_bytes()).hexdigest(),
    )


def run(
    kind: Kind, data_dir: Path, unit_texts: Mapping[str, str], out_dir: Path, hw: HwInfo,
    config_hashes: Mapping[str, str],
) -> RunMeta:  # fmt: skip
    from sklearn.linear_model import LogisticRegression

    x, y, manifest_sha = training_set(data_dir)
    vec = _vectorizer(kind)
    clf: Any = LogisticRegression(max_iter=2000, C=1.0, solver="lbfgs")
    started = datetime.now(UTC).isoformat(timespec="seconds")
    clf.fit(vec.fit_transform(x), y)
    ids = list(unit_texts)
    t0 = time.perf_counter_ns()
    proba: list[float] = [
        float(p) for p in clf.predict_proba(vec.transform([unit_texts[i] for i in ids]))[:, 1]
    ]
    per_unit_ms = (time.perf_counter_ns() - t0) / 1e6 / max(1, len(ids))
    arm, rev = ARM[kind], f"{kind}-tfidf-lr@{manifest_sha[:12]}"
    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "decisions.jsonl").open("w", encoding="utf-8") as f:
        for i, (uid, p) in enumerate(zip(ids, proba, strict=True)):
            pa = round(p, 6)
            probs = {"A": pa, "B": round(1 - pa, 6)}
            choice = "A" if pa >= 0.5 else "B"
            d = Decision(
                unit_id=uid, arm=arm, qs="qs_v1", checkpoint=f"baseline-{kind}",
                checkpoint_rev=rev, max_len=0,
                answers=[Answer(question=QUESTION, choice=choice, probs=probs,
                                confidence=max(probs.values()),
                                answer_confidence=max(probs.values()))],
                latency_ms=per_unit_ms, t_offset_ms=i * per_unit_ms, batch_size=1,
                mode="batch1", device="cpu",
            )  # fmt: skip
            f.write(d.model_dump_json() + "\n")
    meta = RunMeta(
        arm=arm, qs="qs_v1", dataset="main", hw=hw, device="cpu",
        checkpoint=f"baseline-{kind}", checkpoint_rev=rev,
        config_hashes={**config_hashes, "finetune_manifest": manifest_sha},
        batch_size=1, warmup_calls=0, sessions=1, started_at=started,
        finished_at=datetime.now(UTC).isoformat(timespec="seconds"),
    )  # fmt: skip
    (out_dir / "meta.json").write_text(meta.model_dump_json(indent=2) + "\n", encoding="utf-8")
    return meta
