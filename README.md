# laya-pii-bench

Local PII classification benchmark for the open-weight Laya decision model on synthetic
clinical-trial documents. This repo ships with a Claude Code control plane: Claude Code builds the
pipeline milestone by milestone, and each milestone ends at a verifiable gate.

## Prerequisites

- macOS (Apple Silicon) or Linux; ~6 GB free disk for checkpoints and venv
- [uv](https://docs.astral.sh/uv/) (`brew install uv`)
- Node 20 LTS (via nvm) for the HUD
- git, jq (hooks fall back to python3 if jq is missing)
- Claude Code

## 1. Bootstrap (once)

```bash
cd /Users/admin/Dev/laya-PII
./scripts/bootstrap.sh
```

This checks tools, inits git, runs `uv sync`, downloads both Laya checkpoints, writes `hw.json`,
and makes the hook scripts executable. It is idempotent.

## 2. Start Claude Code

```bash
claude
```

First prompt:

```
/progress
/milestone M0
```

Claude reads `CLAUDE.md`, the milestone scope in `docs/MILESTONES.md`, builds it, runs the gate
checks, asks the `gate-reviewer` subagent for an independent pass, updates `docs/STATUS.md`, and
commits. Then continue with `/milestone M1`, `/milestone M2`, and so on.

Resolve the two open decisions whenever you're ready (both have provisional defaults):

```
/decide D-001 no      # coded subject IDs are NOT PII
/decide D-002 m5-max  # name the machine that produces headline latency
```

## 3. Milestone path

| # | Milestone | You'll have |
|---|---|---|
| M0 | Bootstrap | Laya loads, one timed call |
| M1 | Contracts + fixture | domain model, schemas, 10 hand-labeled docs |
| M2 | Scorer + report | every metric, proven on hand-checked numbers |
| M3 | Runner, arm A | real Laya decisions, resumable, timed |
| M4 | Generator | 600 synthetic docs with exact gold |
| M5 | Label + split | units per arm, site-grouped splits |
| M6 | Zero-shot arms | report v1: A and B1–B4, both question sets |
| M7 | HUD | Doom-demo-style replay of real runs |
| M8 | Fine-tuned arm C | report v2 |

## 4. Running the full pipeline (after M6)

```bash
make pipeline          # gen → label → split → run all arms → calibrate → score → report
make smoke             # 20 docs, arm A only, for quick checks
make hud && open hud/dist/index.html
```

Or inside Claude Code: `/pipeline full`.

## 5. Unattended runs

Long milestones (M4, M6) can run headless:

```bash
claude -p "/milestone M4" --permission-mode acceptEdits
```

Permissions in `.claude/settings.json` pre-allow the uv, make, and git commands the pipeline
needs; pushes and destructive commands are denied.

## Layout

```
CLAUDE.md                 Claude Code's standing instructions
docs/                     plan, milestones, decisions, status, specs
config/                   policy, generator spec, arms, question sets
.claude/                  settings, hooks, skills (slash commands), subagents
bench/                    pipeline package (built by Claude Code)
tests/  fixtures/  scripts/  hud/  finetune/
data/ runs/ calib/ scores/ reports/   generated (gitignored except reports/)
```
