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


def test_room_is_below_naive_budget_and_positive(client) -> None:  # type: ignore[no-untyped-def]
    rooms = client._room
    assert set(rooms) == {"pii_present", "subject_role", "category", "doc_kind"}
    assert all(0 < r <= 512 - 1 for r in rooms.values())


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
