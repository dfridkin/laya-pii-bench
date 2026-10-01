"""M8 gate 1: arm C's training data is built from train-split units only, and `verify` proves it."""

import json
from pathlib import Path

import pytest

from bench import finetune as ft
from bench.config import load_question_set
from bench.domain import FinetuneManifest, Split, Splits
from bench.label import read_docs, write_units
from tests.fixture_expected import fixture_units

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "fixtures" / "mini" / "docs.jsonl"
QSETS = [load_question_set(ROOT / "config" / "questions" / f"{q}.yaml") for q in ("qs_v1", "qs_v2")]


@pytest.fixture
def built(tmp_path: Path) -> tuple[Path, Path, FinetuneManifest]:
    docs = read_docs(DOCS)
    doc_split: dict[str, Split] = {
        d.id: "train" if i % 2 == 0 else "test" for i, d in enumerate(docs)
    }
    splits = tmp_path / "splits.json"
    splits.write_text(Splits(seed=0, docs_sha256="x", config_sha256="x", doc_split=doc_split,
                             groups={}, counts={}).model_dump_json())  # fmt: skip
    units = tmp_path / "A.jsonl"
    write_units(fixture_units(), units)
    out = tmp_path / "ft"
    m = ft.build(units, DOCS, splits, QSETS, "A", out, clean_per_pii=1.0)
    return out, splits, m


def test_only_train_documents_and_every_pii_unit(
    built: tuple[Path, Path, FinetuneManifest],
) -> None:
    out, splits, m = built
    split = Splits.model_validate_json(splits.read_text()).doc_split
    recs = [json.loads(x) for x in (out / "records.jsonl").read_text().splitlines()]
    assert recs and all(split[r["doc_id"]] == "train" for r in recs)
    train_pii = {
        u.id for u in fixture_units() if split[u.doc_id] == "train" and u.gold.pii_present == "A"
    }
    assert train_pii <= {r["unit_id"] for r in recs}  # every train PII unit kept
    assert m.n_units_clean <= max(1, round(m.n_units_pii * 1.0)) + len({r["doc_id"] for r in recs})
    # one-hot targets on the gold option; pii_present asked once although both sets ask it
    for r in recs:
        assert sum(r["target"].values()) == 1.0 and r["target"][r["label"]] == 1.0
    per_unit = [(r["unit_id"], r["question"]) for r in recs]
    assert len(per_unit) == len(set(per_unit)) and m.duplicates_removed == m.n_units
    assert ft.verify(out, splits).records_sha256 == m.records_sha256


def test_sampling_is_deterministic(
    built: tuple[Path, Path, FinetuneManifest], tmp_path: Path
) -> None:
    _, splits, m = built
    again = ft.build(tmp_path / "A.jsonl", DOCS, splits, QSETS, "A", tmp_path / "ft2", 1.0)
    assert again.records_sha256 == m.records_sha256 and again.texts_sha256 == m.texts_sha256


def test_verify_rejects_non_train_documents(built: tuple[Path, Path, FinetuneManifest]) -> None:
    out, splits, m = built
    split = Splits.model_validate_json(splits.read_text()).doc_split
    test_doc = next(d for d, s in split.items() if s == "test")
    bad = m.model_copy(update={"doc_ids": [*m.doc_ids, test_doc]})
    (out / "manifest.json").write_text(bad.model_dump_json())
    with pytest.raises(ft.FinetuneError, match="not train-split"):
        ft.verify(out, splits)


def test_verify_rejects_another_split_or_edited_records(
    built: tuple[Path, Path, FinetuneManifest],
) -> None:
    out, splits, _ = built
    body = (out / "records.jsonl").read_text()
    (out / "records.jsonl").write_text(body + body.splitlines()[0] + "\n")
    with pytest.raises(ft.FinetuneError, match="records_sha256"):
        ft.verify(out, splits)
    (out / "records.jsonl").write_text(body)
    s = Splits.model_validate_json(splits.read_text())
    flipped = {d: ("train" if v == "test" else v) for d, v in s.doc_split.items()}
    splits.write_text(s.model_copy(update={"doc_split": flipped}).model_dump_json())
    with pytest.raises(ft.FinetuneError, match="not the split"):
        ft.verify(out, splits)


def test_local_checkpoint_pin_verifies_the_weights_hash(tmp_path: Path) -> None:
    from typer.testing import CliRunner

    from bench.cli import app
    from bench.models import pinned, weights_sha256

    ck = tmp_path / "finetune" / "output" / "c"
    (ck / "tokenizer").mkdir(parents=True)
    (ck / "rl_agent_config.json").write_text("{}")
    (ck / "tokenizer" / "tokenizer.json").write_text("{}")
    (ck / "model.safetensors").write_bytes(b"weights-v1")
    lock = tmp_path / "models.lock.json"
    lock.write_text('{"english": {"repo": "convaiinnovations/laya", "revision": "r", "path": "x"}}')
    r = CliRunner().invoke(app, ["pin-checkpoint", "--path", str(ck), "--models-lock", str(lock)])
    assert r.exit_code == 0, r.output
    entry = json.loads(lock.read_text())["finetuned_english"]
    assert entry == {"repo": "local", "subfolder": "", "revision": weights_sha256(ck),
                     "path": "finetune/output/c"}  # fmt: skip
    assert "english" in json.loads(lock.read_text())  # other pins kept
    assert pinned("finetuned_english", lock).snapshot == ck.resolve()
    (ck / "model.safetensors").write_bytes(b"weights-v2")  # a different checkpoint, same path
    with pytest.raises(FileNotFoundError, match="the lock pins"):
        pinned("finetuned_english", lock)
