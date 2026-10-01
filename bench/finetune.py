"""Arm C training data (M8, D-012, D-022): train-split units only, both question sets.

`build` takes the train-split units of the unit arm (A: 256-token chunks, the spec C shares):
every PII unit plus a seeded, per-doc-type sample of clean units (CLEAN_PER_PII per PII unit;
93% of units are PII-free and the threshold is refit on calib anyway). Each unit gives one record
per question of the chosen question sets, with a one-hot gold target from the label stage; texts
are stored once per unit in texts.jsonl. A question asked identically by two sets (pii_present)
is kept once per unit. `verify` re-proves, from the files alone, that every record and every
listed document is in the train split (M8 gate 1). Tokenization happens on the training machine
with the checkpoint's own tokenizer (`finetune/train_ddp.py`).
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping, Sequence
from datetime import UTC, datetime
from pathlib import Path

from bench.calibrate import gold_answer
from bench.domain import (
    ChoiceQuestion,
    Document,
    FinetuneManifest,
    FinetuneRecord,
    QuestionSet,
    ScoreQuestion,
    Splits,
    Unit,
)
from bench.generate.seeds import rng

HOLDOUT_SHARE = 0.10  # of train documents, for the checkpoint's own temperature fit
HOLDOUT_SEED = 20260922
CLEAN_PER_PII = 3.0  # clean units kept per PII unit: 93% of train units are PII-free
SAMPLE_SEED = 20260930


class FinetuneError(RuntimeError):
    pass


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def sample_units(
    units: Sequence[Unit], docs: Mapping[str, Document], splits: Splits, clean_per_pii: float
) -> list[Unit]:
    """Every train-split PII unit, plus clean units at `clean_per_pii` per PII unit, drawn per
    document type in proportion to that type's clean units (seeded), in original order."""
    train = [u for u in units if splits.doc_split.get(u.doc_id) == "train"]
    pii = [u for u in train if u.gold.pii_present == "A"]
    clean = [u for u in train if u.gold.pii_present != "A"]
    want = min(len(clean), round(len(pii) * clean_per_pii))
    by_type: dict[str, list[Unit]] = {}
    for u in clean:
        by_type.setdefault(docs[u.doc_id].doc_type.value, []).append(u)
    keep: set[str] = set()
    for t in sorted(by_type):
        group = sorted(by_type[t], key=lambda u: u.id)
        k = max(1, round(want * len(group) / len(clean)))
        r = rng(SAMPLE_SEED, "finetune-clean", t)
        keep |= {u.id for u in r.sample(group, min(k, len(group)))}
    return [u for u in train if u.gold.pii_present == "A" or u.id in keep]


def records(
    units: Sequence[Unit], splits: Splits, qsets: Sequence[QuestionSet]
) -> tuple[list[FinetuneRecord], int]:
    out: list[FinetuneRecord] = []
    seen: set[tuple[str, str, str, str]] = set()
    dupes = 0
    for u in units:
        if splits.doc_split.get(u.doc_id) != "train":
            continue
        for qs in qsets:
            for qid, q in qs.questions.items():
                if not isinstance(q, ChoiceQuestion | ScoreQuestion):
                    raise FinetuneError(f"{qs.id}.{qid}: only choice/score questions train arm C")
                key = (u.id, qid, q.instructions, json.dumps(q.criteria, sort_keys=True))
                if key in seen:
                    dupes += 1
                    continue
                seen.add(key)
                gold = gold_answer(u.gold, qid)
                crit = dict(q.criteria) if isinstance(q, ChoiceQuestion) else list(q.criteria)
                keys = list(q.criteria) if isinstance(q, ChoiceQuestion) else [
                    str(i) for i in range(len(q.criteria))
                ]  # fmt: skip
                if gold not in keys:
                    raise FinetuneError(f"{u.id}: gold {gold!r} is not an option of {qid}")
                out.append(FinetuneRecord(
                    unit_id=u.id, doc_id=u.doc_id, question=qid,
                    qtype="choice" if isinstance(q, ChoiceQuestion) else "score",
                    instructions=q.instructions,
                    criteria=crit, target={k: float(k == gold) for k in keys}, label=gold,
                ))  # fmt: skip
    return out, dupes


def build(
    units_path: Path, docs_path: Path, splits_path: Path, qsets: Sequence[QuestionSet],
    unit_arm: str, out_dir: Path, clean_per_pii: float = CLEAN_PER_PII,
) -> FinetuneManifest:  # fmt: skip
    from bench.label import read_docs, read_units

    splits = Splits.model_validate_json(splits_path.read_text(encoding="utf-8"))
    docs = {d.id: d for d in read_docs(docs_path)}
    units = sample_units(read_units(units_path), docs, splits, clean_per_pii)
    recs, dupes = records(units, splits, qsets)
    body = "".join(r.model_dump_json() + "\n" for r in recs)
    texts = "".join(
        json.dumps({"unit_id": u.id, "text": docs[u.doc_id].text[u.start : u.end]},
                   ensure_ascii=False) + "\n"
        for u in units
    )  # fmt: skip
    doc_ids = sorted({r.doc_id for r in recs})
    order = list(doc_ids)
    rng(HOLDOUT_SEED, "finetune-temperature-holdout").shuffle(order)
    holdout = sorted(order[: max(1, round(len(order) * HOLDOUT_SHARE))])
    manifest = FinetuneManifest(
        created_at=datetime.now(UTC).isoformat(timespec="seconds"), unit_arm=unit_arm,
        question_sets=[q.id for q in qsets],
        docs_sha256=hashlib.sha256(docs_path.read_bytes()).hexdigest(),
        units_sha256=hashlib.sha256(units_path.read_bytes()).hexdigest(),
        splits_sha256=hashlib.sha256(splits_path.read_bytes()).hexdigest(),
        records_sha256=_sha(body), texts_sha256=_sha(texts), n_records=len(recs),
        n_units=len(units), n_units_pii=sum(u.gold.pii_present == "A" for u in units),
        n_units_clean=sum(u.gold.pii_present != "A" for u in units), clean_per_pii=clean_per_pii,
        duplicates_removed=dupes, doc_ids=doc_ids, temperature_holdout_doc_ids=holdout,
    )  # fmt: skip
    verify_records(recs, manifest, splits)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "records.jsonl").write_text(body, encoding="utf-8")
    (out_dir / "texts.jsonl").write_text(texts, encoding="utf-8")
    (out_dir / "manifest.json").write_text(
        manifest.model_dump_json(indent=2) + "\n", encoding="utf-8"
    )
    return manifest


def verify_records(
    recs: Sequence[FinetuneRecord], manifest: FinetuneManifest, splits: Splits
) -> None:
    """M8 gate 1: every record and listed document is in the train split; nothing else."""
    bad = sorted({r.doc_id for r in recs if splits.doc_split.get(r.doc_id) != "train"})
    bad += [d for d in manifest.doc_ids if splits.doc_split.get(d) != "train"]
    bad += [d for d in manifest.temperature_holdout_doc_ids if d not in set(manifest.doc_ids)]
    if bad:
        raise FinetuneError(f"{len(bad)} training documents are not train-split, e.g. {bad[0]}")
    if {r.doc_id for r in recs} != set(manifest.doc_ids):
        raise FinetuneError("manifest doc_ids differ from the records' documents")


def verify(out_dir: Path, splits_path: Path) -> FinetuneManifest:
    """Re-prove train-only from the files: records hash, then every document against splits."""
    from bench.domain import FinetuneManifest as M

    manifest = M.model_validate_json((out_dir / "manifest.json").read_text(encoding="utf-8"))
    body = (out_dir / "records.jsonl").read_text(encoding="utf-8")
    if _sha(body) != manifest.records_sha256:
        raise FinetuneError("records.jsonl differs from the manifest's records_sha256")
    texts = (out_dir / "texts.jsonl").read_text(encoding="utf-8")
    if _sha(texts) != manifest.texts_sha256:
        raise FinetuneError("texts.jsonl differs from the manifest's texts_sha256")
    text_units = {json.loads(x)["unit_id"] for x in texts.splitlines() if x.strip()}
    splits_bytes = splits_path.read_bytes()
    if hashlib.sha256(splits_bytes).hexdigest() != manifest.splits_sha256:
        raise FinetuneError(f"{splits_path} is not the split the records were built from")
    splits = Splits.model_validate_json(splits_bytes)
    recs = [FinetuneRecord.model_validate_json(x) for x in body.splitlines() if x.strip()]
    verify_records(recs, manifest, splits)
    if text_units != {r.unit_id for r in recs}:
        raise FinetuneError("texts.jsonl units differ from the records' units")
    return manifest
