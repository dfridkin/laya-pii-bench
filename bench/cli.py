"""Single CLI for every pipeline stage. Subcommands are added milestone by milestone."""

from __future__ import annotations

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


if __name__ == "__main__":
    app()
