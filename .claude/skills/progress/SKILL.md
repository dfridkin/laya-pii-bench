---
name: progress
description: Show where the laya-pii-bench project stands - active milestone, gates passed, open decisions, next action. Use when the user asks for status, progress, or what's next on the benchmark.
---

## Status file

!`cat docs/STATUS.md`

## Open decisions

!`grep '| OPEN |' docs/DECISIONS.md || echo "none"`

## Recent commits

!`git log --oneline -10 2>/dev/null || echo "(no git history yet)"`

Summarize in under 8 lines: active milestone and its state, last gate passed, open decisions that
block the next gate, and the single next action (as a slash command when there is one).
