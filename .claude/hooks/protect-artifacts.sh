#!/usr/bin/env bash
# PreToolUse guard: blocks hand-edits to generated artifacts, sealed splits, and locked fixtures.
# Invariant 11 in CLAUDE.md. Exit 2 = block; stderr is fed back to Claude.
set -u
INPUT=$(cat)

if command -v jq >/dev/null 2>&1; then
  FILE=$(printf '%s' "$INPUT" | jq -r '.tool_input.file_path // .tool_input.notebook_path // empty')
else
  FILE=$(printf '%s' "$INPUT" | python3 -c 'import json,sys; t=json.load(sys.stdin).get("tool_input",{}); print(t.get("file_path") or t.get("notebook_path") or "")')
fi
[ -z "$FILE" ] && exit 0

ROOT="${CLAUDE_PROJECT_DIR:-$(pwd)}"
REL="${FILE#"$ROOT"/}"

case "$REL" in
  data/*|runs/*|calib/*|scores/*|hw.json|models.lock.json)
    echo "Blocked: $REL is a generated artifact (CLAUDE.md invariant 11). Fix the stage that produces it and rerun it instead of editing the output." >&2
    exit 2 ;;
  fixtures/*)
    if [ -e "$ROOT/.locks/fixtures" ]; then
      echo "Blocked: fixtures are locked after the M1 gate (.locks/fixtures). Changing hand-labeled gold needs an owner decision; ask the user and log it in docs/DECISIONS.md." >&2
      exit 2
    fi ;;
  reports/audits/*)
    # Audits are written by subagents; allow creation, block rewriting an existing audit.
    if [ -e "$FILE" ]; then
      echo "Blocked: $REL is a recorded audit. Write a new dated audit file instead of editing this one." >&2
      exit 2
    fi ;;
esac
exit 0
