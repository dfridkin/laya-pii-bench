"""Real checkpoint (model-marked): adapter, per-question state room, tokenizer agreement."""

from pathlib import Path

import pytest

from bench.config import load_arms, load_question_set
from bench.label import read_docs
from bench.questions import build
from tests.fixture_expected import FIXTURE_UNIT_OFFSETS

ROOT = Path(__file__).resolve().parent.parent
pytestmark = pytest.mark.model


@pytest.fixture(scope="module")
def client():  # type: ignore[no-untyped-def]
    from bench.laya_client import LayaClient

    arm = load_arms(ROOT / "config" / "arms.yaml").arms["A"]
    qs = load_question_set(ROOT / "config" / "questions" / "qs_v1.yaml")
    return LayaClient("english", build(qs, "english"), arm.max_len, arm.head_max_len,
                      ROOT / "models.lock.json")  # fmt: skip


def test_state_room_per_question_is_exact(client) -> None:  # type: ignore[no-untyped-def]
    # laya: [CLS] head [SEP] options [SEP] state [SEP], capped at max_len 512. Pinned values,
    # independently reproduced with laya.common.build_sequence in the M3 gate review.
    assert client._room == {
        "pii_present": 449,
        "subject_role": 458,
        "category": 420,
        "doc_kind": 459,
    }
    assert client.current_device() == client.device


def test_token_counts_match_label_stage(client) -> None:  # type: ignore[no-untyped-def]
    docs = {d.id: d for d in read_docs(ROOT / "fixtures" / "mini" / "docs.jsonl")}
    for uid, (start, end, tokens) in FIXTURE_UNIT_OFFSETS.items():
        n, cut = client.state_tokens(docs[uid.split(":")[0]].text[start:end])
        assert n == tokens, uid
        assert cut == [], uid  # 256-token chunks fit every question's room


def test_long_state_cut_for_every_question(client) -> None:  # type: ignore[no-untyped-def]
    n, cut = client.state_tokens("word " * 600)
    assert n >= 600 and set(cut) == set(client.questions)


def test_predict_adapts(client) -> None:  # type: ignore[no-untyped-def]
    from bench.laya_client import to_answers

    res, ns = client.predict("Subject 1001-0023 was seen on Day 15.")
    answers = to_answers(res, client.questions)
    assert ns > 0 and [a.question for a in answers] == list(client.questions)
    assert all(a.answer_confidence is not None for a in answers)
    batch, ns_b = client.predict_batch(["a", "b"])
    assert len(batch) == 2 and ns_b > 0


def test_multilingual_client_explicit_max_len() -> None:
    """Invariant 8: the multilingual checkpoint loads from its subfolder and always gets an explicit
    max_len; its state room at 1024 is far above the English one."""
    from bench.laya_client import LayaClient, to_answers

    arm = load_arms(ROOT / "config" / "arms.yaml").arms["B1"]
    qs = load_question_set(ROOT / "config" / "questions" / "qs_v1.yaml")
    ml = LayaClient("multilingual", build(qs, "multilingual"), arm.max_len, arm.head_max_len,
                    ROOT / "models.lock.json")  # fmt: skip
    assert ml.max_len == 1024 and all(800 < r < 1024 for r in ml._room.values())
    res, _ = ml.predict("Patientin Marta Kowalczyk, geb. 14.03.1961, Prüfzentrum 2104.")
    assert [a.question for a in to_answers(res, ml.questions)] == list(qs.questions)
