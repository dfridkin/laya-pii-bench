"""Tests that score through the CLI need a committed calib (D-019): a throwaway repo per tmp dir."""

import subprocess
from pathlib import Path

_ID = ["-c", "user.name=test", "-c", "user.email=test@example.invalid", "-c",
       "commit.gpgsign=false"]  # fmt: skip


def git(cwd: Path, *args: str) -> str:
    return subprocess.run(["git", *_ID, *args], cwd=cwd, capture_output=True, text=True,
                          check=True).stdout.strip()  # fmt: skip


def commit_file(path: Path) -> str:
    """Commit `path` in a repo rooted at its parent (created if missing); returns the commit sha."""
    root = path.parent
    if not (root / ".git").exists():
        git(root, "init", "-q")
    git(root, "add", "--", path.name)
    git(root, "commit", "-q", "--allow-empty", "-m", f"freeze {path.name}")
    return git(root, "rev-parse", "HEAD")
