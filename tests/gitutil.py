"""Tests that score through the CLI need a committed calib (D-019): a throwaway repo per tmp dir.

`bench.freeze` only accepts calib committed in the project repository; the autouse fixture in
conftest.py points `freeze.project_root` at the repo created here (tests only, in-process)."""

import subprocess
from pathlib import Path

_ID = ["-c", "user.name=test", "-c", "user.email=test@example.invalid", "-c",
       "commit.gpgsign=false"]  # fmt: skip
REPOS: list[Path] = []  # repos created by the current test; the last one is the "project"


def git(cwd: Path, *args: str) -> str:
    return subprocess.run(["git", *_ID, *args], cwd=cwd, capture_output=True, text=True,
                          check=True).stdout.strip()  # fmt: skip


def init_repo(root: Path) -> Path:
    if not (root / ".git").exists():
        git(root, "init", "-q")
    REPOS.append(root)
    return root


def commit_file(path: Path) -> str:
    """Commit `path` in a repo rooted at its parent (created if missing); returns the commit sha."""
    root = init_repo(path.parent)
    git(root, "add", "--", path.name)
    git(root, "commit", "-q", "--allow-empty", "-m", f"freeze {path.name}")
    return git(root, "rev-parse", "HEAD")
