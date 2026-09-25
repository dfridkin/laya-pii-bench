#!/usr/bin/env bash
# SessionStart (startup/resume/compact/clear): re-inject progress and hard rules.
# Plain stdout is added to Claude's context.
cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0
echo "## laya-pii-bench session context"
if [ -f docs/STATUS.md ]; then
  echo
  echo "### docs/STATUS.md (top)"
  sed -n '1,25p' docs/STATUS.md
fi
if grep -q '| OPEN |' docs/DECISIONS.md 2>/dev/null; then
  echo
  echo "### Open decisions (use provisional defaults only for cheap-to-redo work; ask before gates that depend on them)"
  grep '| OPEN |' docs/DECISIONS.md | cut -d'|' -f2,3,5
fi
echo
echo "### Hard rules"
echo "- Gold spans only from the sentinel renderer. Split by site. Test split sealed until score."
echo "- Runner stores raw probs; routing in score. No noul on English checkpoint. Gate on confidence."
echo "- Never hand-edit data/ runs/ calib/ scores/. Work only inside the active milestone; stop at its gate."
if command -v git >/dev/null 2>&1 && [ -d .git ]; then
  echo
  echo "### Recent commits"
  git log --oneline -5 2>/dev/null
fi
exit 0
