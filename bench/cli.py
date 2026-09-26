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


@app.command()
def label(
    docs: Annotated[Path, typer.Option(help="Documents JSONL.")] = Path("data/docs.jsonl"),
    policy: Annotated[Path, typer.Option(help="Label policy.")] = Path("config/policy.yaml"),
    arms: Annotated[Path, typer.Option(help="Arms config.")] = Path("config/arms.yaml"),
    arm: Annotated[list[str] | None, typer.Option(help="Arm(s) to label.")] = None,
    out: Annotated[Path, typer.Option(help="Directory for {arm}.jsonl.")] = Path("data/units"),
) -> None:
    """Segment documents into units and derive gold answers (chunk units only until M5)."""
    from bench import tokenize
    from bench.config import load_arms, load_policy
    from bench.label import label_docs, read_docs, write_units

    cfg, pol, documents = load_arms(arms), load_policy(policy), read_docs(docs)
    for name in arm or [n for n, a in cfg.arms.items() if a.enabled]:
        spec = cfg.arms[name]
        tok = tokenize.load(spec.checkpoint)
        units = label_docs(documents, spec, pol, tok, tok.name)
        write_units(units, out / f"{name}.jsonl")
        n_trunc = sum(u.truncated for u in units)
        typer.echo(f"{name}: {len(units)} units ({n_trunc} truncated) -> {out / name}.jsonl")


@app.command()
def calibrate(
    decisions: Annotated[Path, typer.Option(help="Decisions JSONL for one arm x qs.")],
    units: Annotated[Path, typer.Option(help="Units JSONL (gold answers).")],
    out: Annotated[Path, typer.Option(help="Calib params JSON to write.")],
    policy: Annotated[Path, typer.Option(help="Label policy.")] = Path("config/policy.yaml"),
    debug_fit_all: Annotated[
        bool, typer.Option(help="Fixture only: fit on every unit (no calib split). Labeled.")
    ] = False,
) -> None:
    """Fit temperatures and routing thresholds on the calib split; write hashed params."""
    from bench import calibrate as cal
    from bench.config import load_policy
    from bench.label import read_units
    from bench.score import read_decisions

    if not debug_fit_all:
        typer.echo("calib split selection arrives with `bench split` (M5); use --debug-fit-all")
        raise typer.Exit(2)
    unit_map = {u.id: u for u in read_units(units)}
    params = cal.fit(read_decisions(decisions), unit_map, load_policy(policy), "fixture_debug")
    cal.write(params, out)
    typer.echo(
        f"{params.arm}/{params.qs}: t_low={params.t_low:.4f} t_high={params.t_high:.4f} "
        f"fit_on={params.fit_on} hash={params.content_hash[:12]} -> {out}"
    )


@app.command()
def score(
    decisions: Annotated[Path, typer.Option(help="Decisions JSONL for one arm x qs.")],
    units: Annotated[Path, typer.Option(help="Units JSONL (gold answers).")],
    calib: Annotated[Path, typer.Option(help="Frozen calib params JSON (hash-checked).")],
    out: Annotated[Path, typer.Option(help="Scores JSON to write.")],
    docs: Annotated[Path, typer.Option(help="Documents JSONL.")] = Path("data/docs.jsonl"),
    policy: Annotated[Path, typer.Option(help="Label policy.")] = Path("config/policy.yaml"),
    hw: Annotated[Path, typer.Option(help="Hardware fingerprint.")] = Path("hw.json"),
    allow_debug_calib: Annotated[
        bool, typer.Option(help="Accept fit_on=fixture_debug calib (fixture runs only).")
    ] = False,
) -> None:
    """Score decisions against gold with frozen calib params. Refuses a calib hash mismatch."""
    from bench import calibrate as cal
    from bench import score as sc
    from bench.config import load_policy
    from bench.domain import HwInfo
    from bench.label import read_docs, read_units

    try:
        params = cal.load_verified(calib, allow_debug=allow_debug_calib)
    except cal.CalibError as e:
        typer.echo(f"error: {e}", err=True)
        raise typer.Exit(2) from e
    documents = read_docs(docs)
    split_docs = {"fixture": {d.id for d in documents}}  # bench split (M5) adds calib/test/holdout
    hw_info = HwInfo.model_validate_json(hw.read_text()) if hw.exists() else None
    hashes = {k: sc.sha256_file(p) for k, p in (("docs", docs), ("units", units),
                                                ("decisions", decisions))}  # fmt: skip
    scores = sc.score(sc.read_decisions(decisions), read_units(units), documents, params,
                      load_policy(policy), split_docs, hw_info, hashes)  # fmt: skip
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(scores.model_dump_json(indent=2) + "\n", encoding="utf-8")
    for name, sp in scores.splits.items():
        h = sp.headline
        rec = "n/a" if h.recall is None else f"{h.recall.point:.4f}"
        typer.echo(f"{name}: recall@t_low={rec} forward_rate={h.forward_rate.point:.4f} "
                   f"false_forwards={h.false_forwards} -> {out}")  # fmt: skip


@app.command()
def report(
    scores: Annotated[list[Path] | None, typer.Option(help="Scores JSON files.")] = None,
    scores_dir: Annotated[Path, typer.Option(help="Used when --scores is not given.")] = Path(
        "scores"
    ),
    out: Annotated[Path, typer.Option(help="Report markdown.")] = Path("reports/report.md"),
    hud: Annotated[Path | None, typer.Option(help="HUD replay export (M7).")] = None,
) -> None:
    """Render the markdown report from scores."""
    from bench import report as rep

    paths = scores or sorted(scores_dir.glob("*.json"))
    rep.write(rep.read_scores(paths), out)
    typer.echo(f"wrote {out} from {len(paths)} scores file(s)")
    if hud is not None:
        typer.echo(f"note: HUD replay export arrives in M7; {hud} not written", err=True)


if __name__ == "__main__":
    app()
