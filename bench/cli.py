"""Single CLI for every pipeline stage. Subcommands are added milestone by milestone."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

app = typer.Typer(no_args_is_help=True, add_completion=False, help="laya-pii-bench pipeline")


@app.callback()
def main() -> None:
    """laya-pii-bench pipeline. Each stage is a subcommand."""


@app.command()
def version() -> None:
    """Print the package version."""
    from bench import __version__

    typer.echo(__version__)


@app.command()
def hw(
    out: Annotated[Path, typer.Option(help="Where to write the fingerprint.")] = Path("hw.json"),
    models_lock: Annotated[
        Path, typer.Option(help="Checkpoint revisions from download_models.py.")
    ] = Path("models.lock.json"),
) -> None:
    """Write the hardware fingerprint (OS, CPU, RAM, torch, device, checkpoint revisions)."""
    from bench import hw as hw_mod

    info = hw_mod.write(out, models_lock)
    typer.echo(f"device={info.device} ({info.device_name}) torch={info.torch} -> {out}")


@app.command()
def validate(
    docs: Annotated[Path, typer.Argument(help="Documents JSONL to validate.")],
    policy: Annotated[Path, typer.Option(help="Label policy.")] = Path("config/policy.yaml"),
) -> None:
    """Validate documents: offsets, overlaps, enums, policy consistency."""
    from bench.config import load_policy
    from bench.validate import validate_file

    report = validate_file(docs, load_policy(policy))
    for r in report.results:
        for err in r.errors:
            typer.echo(f"line {r.line} ({r.doc_id or '?'}): {err}", err=True)
    typer.echo(f"{report.n_valid}/{len(report.results)} valid")
    if not report.ok:
        raise typer.Exit(1)


@app.command()
def schema(
    out: Annotated[Path, typer.Option(help="Directory for the JSON Schema.")] = Path("schema"),
) -> None:
    """Export the domain model as JSON Schema (input to the HUD's generated TS types)."""
    from bench.schema_export import export

    typer.echo(f"wrote {export(out)}")


@app.command("build-fixture")
def build_fixture(
    src: Annotated[Path, typer.Option(help="Hand-labeled sources.")] = Path("fixtures/mini/src"),
    out: Annotated[Path, typer.Option(help="Output JSONL.")] = Path("fixtures/mini/docs.jsonl"),
) -> None:
    """Resolve the hand-labeled fixture sources (inline sentinel markup) into docs JSONL."""
    from bench.fixture import write

    typer.echo(f"wrote {write(src, out)} docs -> {out}")


if __name__ == "__main__":
    app()
