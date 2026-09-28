"""Calib freeze (D-019): calib files are committed before any scoring, and `score` checks it.

`require_committed` refuses a calib file that is untracked or differs from HEAD, and returns the
commit that last touched it (sha and ISO commit time), which the scores record. `freeze` commits
calib files with their content hashes in the message (`make freeze-calib`).
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


class FreezeError(RuntimeError):
    pass


def _git(cwd: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, check=False)


def repo_root(path: Path) -> Path:
    r = _git(path.resolve().parent, "rev-parse", "--show-toplevel")
    if r.returncode != 0:
        raise FreezeError(f"{path} is not inside a git repository; calib must be committed (D-019)")
    return Path(r.stdout.strip())


def require_committed(path: Path) -> tuple[str, str]:
    """(commit sha, commit time) of the committed, unmodified calib file; FreezeError otherwise."""
    root = repo_root(path)
    rel = str(path.resolve().relative_to(root))
    if _git(root, "ls-files", "--error-unmatch", rel).returncode != 0:
        raise FreezeError(f"{rel} is not committed; run `make freeze-calib` before scoring (D-019)")
    if _git(root, "diff", "--quiet", "HEAD", "--", rel).returncode != 0:
        raise FreezeError(f"{rel} differs from its committed version; commit or restore it (D-019)")
    log = _git(root, "log", "-n", "1", "--format=%H %cI", "--", rel)
    parts = log.stdout.split()
    if log.returncode != 0 or len(parts) != 2:
        raise FreezeError(f"cannot read the commit of {rel}")
    return parts[0], parts[1]


def freeze(paths: list[Path], extra_message: str = "") -> str | None:
    """Stage and commit calib files, listing each file's content hash in the message.
    Returns the new commit sha, or None when there is nothing to commit."""
    if not paths:
        return None
    root = repo_root(paths[0])
    rels = [str(p.resolve().relative_to(root)) for p in paths]
    _git(root, "add", "--", *rels)
    if _git(root, "diff", "--cached", "--quiet", "--", *rels).returncode == 0:
        return None
    lines: list[str] = []
    for p, rel in zip(paths, rels, strict=True):
        h = str(json.loads(p.read_text())["content_hash"])
        lines.append(f"- {rel}: {h}")
    msg = "calib: freeze " + ", ".join(p.stem for p in paths) + "\n\n" + "\n".join(lines)
    if extra_message:
        msg += "\n\n" + extra_message
    r = _git(root, "commit", "-m", msg, "--", *rels)
    if r.returncode != 0:
        raise FreezeError(f"git commit failed: {r.stderr.strip()}")
    return _git(root, "rev-parse", "HEAD").stdout.strip()
