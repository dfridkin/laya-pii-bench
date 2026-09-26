import json
from pathlib import Path
from typing import Any

import pytest
from typer.testing import CliRunner

from bench.cli import app
from bench.config import Policy, load_policy
from bench.validate import validate_file, validate_lines

ROOT = Path(__file__).resolve().parent.parent
TEXT = "Patient Anna Nowak, MRN 00482913, protocol FTX-4471-012."
#       0       8         18    24       33        43          55


@pytest.fixture(scope="module")
def policy() -> Policy:
    return load_policy(ROOT / "config" / "policy.yaml")


def span(
    start: int, end: int, category: str = "phi_direct", role: str = "patient"
) -> dict[str, Any]:
    return {
        "start": start,
        "end": end,
        "category": category,
        "role": role,
        "value_kind": "x",
        "surface": "y",
    }


def doc(**kw: Any) -> dict[str, Any]:
    base: dict[str, Any] = {
        "id": "d1",
        "doc_type": "csr_patient_narrative",
        "lang": "en",
        "text": TEXT,
        "spans": [span(8, 18), span(24, 32)],
        "negatives": [{"start": 43, "end": 55, "kind": "protocol_no"}],
        "tags": ["hard_negative"],
        "length_bucket": "short",
        "pii_depth": None,
        "world_refs": {"study": "FTX-4471-012", "site": "S1", "subjects": ["1001-0001"]},
        "gen_meta": {},
    }
    return base | kw


def errors(policy: Policy, *docs: dict[str, Any]) -> list[str]:
    report = validate_lines([json.dumps(d) for d in docs], policy)
    return [e for r in report.results for e in r.errors]


def test_valid_doc(policy: Policy) -> None:
    assert TEXT[8:18] == "Anna Nowak" and TEXT[24:32] == "00482913"
    assert TEXT[43:55] == "FTX-4471-012"
    assert errors(policy, doc()) == []


@pytest.mark.parametrize(
    ("patch", "match"),
    [
        ({"spans": [span(8, 99)]}, "beyond text length"),
        ({"negatives": [{"start": 50, "end": 99, "kind": "k"}]}, "beyond text length"),
        ({"spans": [span(7, 18)]}, "whitespace"),
        ({"spans": [span(24, 32), span(8, 18)]}, "not sorted"),
        ({"spans": [span(8, 18), span(13, 19)]}, "overlap"),
        (
            {
                "negatives": [
                    {"start": 43, "end": 50, "kind": "a"},
                    {"start": 46, "end": 55, "kind": "b"},
                ]
            },
            "negatives[0] and negatives[1] overlap",
        ),
        ({"negatives": [{"start": 24, "end": 32, "kind": "lot_no"}]}, "overlaps negatives"),
        ({"spans": [span(8, 18, role="staff")]}, "requires role patient"),
        ({"spans": [span(8, 18, category="coded_id", role="sponsor")]}, "requires role patient"),
        ({"spans": [span(8, 18, category="staff_pii", role="patient")]}, "staff or sponsor"),
        ({"tags": ["hard_negative", "sparkly"]}, "unknown tags"),
        ({"tags": ["hard_negative", "hard_negative"]}, "duplicate tags"),
        ({"tags": []}, "hard_negative"),
        ({"negatives": []}, "hard_negative"),
        ({"pii_depth": "early"}, "pii_depth"),
        ({"lang": "fr"}, "lang"),
        ({"spans": [span(8, 18, category="phi")]}, "category"),
        ({"surprise": True}, "surprise"),
    ],
)
def test_invalid_docs(policy: Policy, patch: dict[str, Any], match: str) -> None:
    errs = errors(policy, doc(**patch))
    assert any(match in e for e in errs), errs


def test_staff_pii_sponsor_ok(policy: Policy) -> None:
    assert errors(policy, doc(spans=[span(8, 18, category="staff_pii", role="sponsor")])) == []


def test_pii_depth_ok_on_long(policy: Policy) -> None:
    assert errors(policy, doc(pii_depth="late", length_bucket="long")) == []


def test_duplicate_ids(policy: Policy) -> None:
    assert any("duplicate id" in e for e in errors(policy, doc(), doc()))


def test_blank_lines_skipped_and_empty_file_not_ok(policy: Policy, tmp_path: Path) -> None:
    p = tmp_path / "docs.jsonl"
    p.write_text("\n\n")
    report = validate_file(p, policy)
    assert report.results == [] and not report.ok


def test_cli_reports_counts(tmp_path: Path) -> None:
    p = tmp_path / "docs.jsonl"
    p.write_text(json.dumps(doc()) + "\n" + json.dumps(doc(id="d2", tags=[])) + "\n")
    policy_path = str(ROOT / "config" / "policy.yaml")
    result = CliRunner().invoke(app, ["validate", str(p), "--policy", policy_path])
    assert result.exit_code == 1
    assert "1/2 valid" in result.stdout
    p.write_text(json.dumps(doc()) + "\n")
    result = CliRunner().invoke(app, ["validate", str(p), "--policy", policy_path])
    assert result.exit_code == 0
    assert "1/1 valid" in result.stdout
