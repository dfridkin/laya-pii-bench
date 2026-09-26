import json
from pathlib import Path

from typer.testing import CliRunner

from bench.cli import app
from bench.domain import EXPORTED
from bench.schema_export import SCHEMA_FILE, build

ROOT = Path(__file__).resolve().parent.parent


def test_every_exported_model_in_schema() -> None:
    defs = build()["$defs"]
    for model in EXPORTED:
        assert model.__name__ in defs


def test_no_property_titles() -> None:
    doc = build()["$defs"]["Document"]
    assert all("title" not in prop for prop in doc["properties"].values())


def test_committed_schema_is_current(tmp_path: Path) -> None:
    result = CliRunner().invoke(app, ["schema", "--out", str(tmp_path)])
    assert result.exit_code == 0, result.output
    fresh = (tmp_path / SCHEMA_FILE).read_text()
    committed = (ROOT / "schema" / SCHEMA_FILE).read_text()
    assert fresh == committed, "schema/ is stale: run `make schema`"
    assert json.loads(fresh)["title"] == "Domain"


def test_ts_types_exist_for_exported_models() -> None:
    ts = (ROOT / "hud" / "src" / "types.gen.ts").read_text()
    for model in EXPORTED:
        assert f"export interface {model.__name__} " in ts
