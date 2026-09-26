from pathlib import Path
from typing import Any, get_args

import pytest
import yaml
from pydantic import ValidationError

from bench import config
from bench.domain import (
    CategoryAnswer,
    ChoiceQuestion,
    DocKindAnswer,
    GoldAnswers,
    PiiCategory,
    RoleAnswer,
)

ROOT = Path(__file__).resolve().parent.parent
CFG = ROOT / "config"


def raw(name: str) -> dict[str, Any]:
    return yaml.safe_load((CFG / name).read_text())


def dump(tmp_path: Path, name: str, data: Any) -> Path:
    p = tmp_path / name
    p.write_text(yaml.safe_dump(data))
    return p


# --- the real config files load -----------------------------------------------------------------


def test_policy_loads() -> None:
    p = config.load_policy(CFG / "policy.yaml")
    assert p.coded_id_is_pii is True  # D-001 provisional
    assert PiiCategory.CODED_ID in p.effective_pii_categories


def test_policy_coded_id_toggle(tmp_path: Path) -> None:
    data = raw("policy.yaml") | {"coded_id_is_pii": False}
    p = config.load_policy(dump(tmp_path, "policy.yaml", data))
    assert PiiCategory.CODED_ID not in p.effective_pii_categories


def test_gen_spec_loads() -> None:
    g = config.load_gen_spec(CFG / "gen_spec.yaml")
    assert g.total_docs == 600  # D-008


def test_arms_load() -> None:
    a = config.load_arms(CFG / "arms.yaml")
    assert a.arms["A"].state_budget == 320
    assert a.arms["B1"].state_budget == 768
    assert a.arms["C"].enabled is False


def test_question_sets_load() -> None:
    qs = config.load_question_sets(CFG / "questions")
    assert set(qs) == {"qs_v1", "qs_v2"}


# --- question sets are answerable from GoldAnswers (contract) -----------------------------------


def choice_keys(qs_id: str, q: str) -> set[str]:
    question = config.load_question_sets(CFG / "questions")[qs_id].questions[q]
    assert isinstance(question, ChoiceQuestion)
    return set(question.criteria)


def test_qs_v1_keys_match_gold_literals() -> None:
    assert choice_keys("qs_v1", "pii_present") == {"A", "B"}
    assert choice_keys("qs_v1", "subject_role") == set(get_args(RoleAnswer))
    assert choice_keys("qs_v1", "category") == set(get_args(CategoryAnswer))
    assert choice_keys("qs_v1", "doc_kind") == set(get_args(DocKindAnswer))
    qs = config.load_question_sets(CFG / "questions")["qs_v1"]
    assert set(qs.questions) <= set(GoldAnswers.model_fields)


def test_qs_v2_one_binary_question_per_category() -> None:
    qs = config.load_question_sets(CFG / "questions")["qs_v2"]
    per_cat = {k.removeprefix("has_") for k in qs.questions if k.startswith("has_")}
    assert per_cat == {c.value for c in PiiCategory}
    for q in qs.questions:
        assert choice_keys("qs_v2", q) == {"A", "B"}


def test_no_noul_in_shipped_question_sets() -> None:
    # Arm A (English) runs every question set, so none may use noul (invariant 5).
    for qs in config.load_question_sets(CFG / "questions").values():
        assert all(q.type != "noul" for q in qs.questions.values())


def test_yaml_booleans_rejected_as_criteria(tmp_path: Path) -> None:
    (tmp_path / "q.yaml").write_text(
        "id: q\nquestions:\n  x:\n    type: choice\n    instructions: i\n"
        "    criteria:\n      A: yes\n      B: no\n"
    )
    with pytest.raises(ValidationError):
        config.load_question_set(tmp_path / "q.yaml")


# --- unknown keys and inconsistencies are errors ------------------------------------------------


@pytest.mark.parametrize(
    ("name", "loader"),
    [
        ("policy.yaml", config.load_policy),
        ("gen_spec.yaml", config.load_gen_spec),
        ("arms.yaml", config.load_arms),
    ],
)
def test_unknown_top_level_key_rejected(tmp_path: Path, name: str, loader: Any) -> None:
    (tmp_path / "questions").mkdir()
    for q in ("qs_v1", "qs_v2"):
        (tmp_path / "questions" / f"{q}.yaml").write_text(
            (CFG / "questions" / f"{q}.yaml").read_text()
        )
    with pytest.raises(ValidationError, match="bogus"):
        loader(dump(tmp_path, name, raw(name) | {"bogus": 1}))


def test_unknown_nested_key_rejected(tmp_path: Path) -> None:
    data = raw("arms.yaml")
    data["arms"]["A"]["unit"]["stride"] = 8
    with pytest.raises(ValidationError):
        config.load_arms(dump(tmp_path, "arms.yaml", data), qs_dir=CFG / "questions")


def test_unknown_question_key_rejected(tmp_path: Path) -> None:
    data = raw("questions/qs_v1.yaml")
    data["questions"]["pii_present"]["labels"] = {"A": "yes"}
    with pytest.raises(ValidationError):
        config.load_question_set(dump(tmp_path, "qs_v1.yaml", data))


def test_question_set_id_must_match_file(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="does not match"):
        config.load_question_set(dump(tmp_path, "other.yaml", raw("questions/qs_v1.yaml")))


def test_non_mapping_rejected(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="mapping"):
        config.load_policy(dump(tmp_path, "policy.yaml", [1, 2]))


@pytest.mark.parametrize(
    ("patch", "match"),
    [
        ({"pii_categories": ["phi_direct", "coded_id"]}, "coded_id_is_pii"),
        ({"category_precedence": ["phi_direct", "phi_quasi", "coded_id"]}, "precedence"),
        ({"category_answer_map": {"phi_direct": "direct"}}, "category_answer_map"),
        ({"role_map": {"patient": "patient"}}, "role_map"),
        ({"doc_kind_map": {"crf_page": "form_table"}}, "doc_kind_map"),
    ],
)
def test_policy_inconsistencies(tmp_path: Path, patch: dict[str, Any], match: str) -> None:
    with pytest.raises(ValidationError, match=match):
        config.load_policy(dump(tmp_path, "policy.yaml", raw("policy.yaml") | patch))


@pytest.mark.parametrize(
    ("patch", "match"),
    [
        ({"lang_mix": {"en": 0.5, "de": 0.1, "es": 0.1, "pl": 0.1}}, "lang_mix"),
        ({"lang_mix": {"en": 1.1, "de": -0.1, "es": 0.0, "pl": 0.0}}, "negative"),
        ({"locales": {"en": "en_US"}}, "locales"),
        ({"length_mix": {"short": 1.0}}, "LengthBucket"),
        ({"doc_types": {"crf_page": 600}}, "every DocType"),
        (
            {"length_tokens": {"short": [5, 1], "medium": [1, 2], "long": [2, 3], "xl": [3, 4]}},
            "lo < hi",
        ),
        ({"pii_depth_positions": {"early": [0.5, 0.2]}}, "pii_depth_positions"),
    ],
)
def test_gen_spec_inconsistencies(tmp_path: Path, patch: dict[str, Any], match: str) -> None:
    with pytest.raises(ValidationError, match=match):
        config.load_gen_spec(dump(tmp_path, "gen_spec.yaml", raw("gen_spec.yaml") | patch))


def test_gen_spec_negative_count(tmp_path: Path) -> None:
    data = raw("gen_spec.yaml")
    data["doc_types"]["crf_page"] = -1
    with pytest.raises(ValidationError, match=">= 0"):
        config.load_gen_spec(dump(tmp_path, "gen_spec.yaml", data))


@pytest.mark.parametrize(
    ("arm_patch", "match"),
    [
        ({"head_max_len": 512}, "head_max_len"),
        ({"unit": {"kind": "chunk", "size": 32, "overlap": 32}}, "overlap"),
        ({"checkpoint": "gpt"}, "checkpoint"),
    ],
)
def test_arm_inconsistencies(tmp_path: Path, arm_patch: dict[str, Any], match: str) -> None:
    data = raw("arms.yaml")
    data["arms"]["A"] |= arm_patch
    with pytest.raises(ValidationError, match=match):
        config.load_arms(dump(tmp_path, "arms.yaml", data), qs_dir=CFG / "questions")


def test_arms_missing_question_set(tmp_path: Path) -> None:
    data = raw("arms.yaml")
    data["defaults"]["question_sets"] = ["qs_v1", "qs_v9"]
    with pytest.raises(ValueError, match="qs_v9"):
        config.load_arms(dump(tmp_path, "arms.yaml", data), qs_dir=CFG / "questions")
