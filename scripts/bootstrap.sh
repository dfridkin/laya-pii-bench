#!/usr/bin/env bash
# Idempotent bootstrap for laya-pii-bench. Safe to rerun.
set -euo pipefail
cd "$(dirname "$0")/.."
export USE_TF=0

say()  { printf '\033[1;32m==>\033[0m %s\n' "$*"; }
warn() { printf '\033[1;33m!!\033[0m %s\n' "$*"; }
die()  { printf '\033[1;31mxx\033[0m %s\n' "$*"; exit 1; }

say "Checking tools"
command -v uv  >/dev/null || die "uv not found: brew install uv"
command -v git >/dev/null || die "git not found"
if command -v node >/dev/null; then
  NODE_MAJOR=$(node -p 'process.versions.node.split(".")[0]')
  [ "$NODE_MAJOR" -ge 20 ] || warn "Node $NODE_MAJOR found; HUD (M7) expects >= 20 (nvm use 20)"
else
  warn "node not found; needed only for the HUD (M7) and schema->TS (M1)"
fi
command -v jq >/dev/null || warn "jq not found; hooks fall back to python3"
command -v claude >/dev/null || warn "claude CLI not found on PATH"

say "Git"
if [ ! -d .git ]; then
  git init -q -b main
  git add -A
  git commit -q -m "Scaffold: Claude Code control plane" || true
fi

say "Hook scripts executable"
chmod +x .claude/hooks/*.sh scripts/*.sh

say "Python env (uv sync)"
uv sync

say "Downloading Laya checkpoints (English root + multilingual subfolder)"
uv run python scripts/download_models.py

say "Directories"
mkdir -p data runs calib scores reports/audits schema fixtures/mini .locks

if uv run python -c "import bench.cli" 2>/dev/null; then
  say "Hardware fingerprint"
  uv run bench hw --out hw.json || warn "bench hw failed; M0 will fix"
else
  warn "bench package not built yet; hw.json comes in M0"
fi

say "Done. Next: run 'claude' in this folder, then '/milestone M0'."
