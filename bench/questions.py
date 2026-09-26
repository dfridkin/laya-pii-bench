"""Build laya question dicts from a QuestionSet (docs/specs/laya-runtime.md)."""

from __future__ import annotations

from typing import Any

from bench.domain import ChoiceQuestion, NoulQuestion, QuestionSet, ScoreQuestion

ENGLISH_CHECKPOINTS = frozenset({"english", "finetuned_english"})


class QuestionError(ValueError):
    pass


def build(qs: QuestionSet, checkpoint: str) -> dict[str, dict[str, Any]]:
    """Laya `questions` argument. Rejects `noul` on English checkpoints (invariant 5, D-006)."""
    out: dict[str, dict[str, Any]] = {}
    for qid, q in qs.questions.items():
        match q:
            case ChoiceQuestion():
                out[qid] = {
                    "type": "choice",
                    "instructions": q.instructions,
                    "criteria": dict(q.criteria),
                }
            case ScoreQuestion():
                out[qid] = {
                    "type": "score",
                    "instructions": q.instructions,
                    "criteria": list(q.criteria),
                }
            case NoulQuestion():
                if checkpoint in ENGLISH_CHECKPOINTS:
                    raise QuestionError(
                        f"{qs.id}.{qid}: noul questions are not allowed on the {checkpoint} "
                        "checkpoint (invariant 5); use a two-option choice with keys A/B"
                    )
                out[qid] = {"type": "noul", "instructions": q.instructions}
    return out
