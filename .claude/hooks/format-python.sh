#!/usr/bin/env bash
# PostToolUse: format and autofix Python files Claude just wrote. Silent on success.
set -u
INPUT=$(cat)
if command -v jq >/dev/null 2>&1; then
  FILE=$(printf '%s' "$INPUT" | jq -r '.tool_input.file_path // empty')
else
  FILE=$(printf '%s' "$INPUT" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("file_path") or "")')
fi
case "$FILE" in
  *.py) ;;
  *) exit 0 ;;
esac
[ -f "$FILE" ] || exit 0
cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0
command -v uv >/dev/null 2>&1 || exit 0
uv run --quiet ruff format "$FILE" >/dev/null 2>&1
uv run --quiet ruff check --fix --quiet "$FILE" >/dev/null 2>&1
exit 0
