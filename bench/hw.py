"""Hardware fingerprint written as `hw.json` and attached to every run (invariant 9)."""

from __future__ import annotations

import json
import os
import platform
import subprocess
import sys
from datetime import UTC, datetime
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

from bench.domain import Device, HwInfo


def pick_device() -> tuple[Device, str]:
    """Device order cuda -> mps -> cpu (docs/specs/laya-runtime.md)."""
    import torch

    if torch.cuda.is_available():
        return "cuda", torch.cuda.get_device_name(0)
    if torch.backends.mps.is_available():
        return "mps", "Apple MPS"
    return "cpu", _cpu_name()


def _sysctl(key: str) -> str | None:
    try:
        out = subprocess.run(["sysctl", "-n", key], capture_output=True, text=True, check=True)
    except (OSError, subprocess.CalledProcessError):
        return None
    return out.stdout.strip() or None


def _cpu_name() -> str:
    if sys.platform == "darwin":
        name = _sysctl("machdep.cpu.brand_string")
        if name:
            return name
    if sys.platform.startswith("linux"):
        try:
            for line in Path("/proc/cpuinfo").read_text().splitlines():
                if line.startswith("model name"):
                    return line.split(":", 1)[1].strip()
        except OSError:
            pass
    return platform.processor() or platform.machine()


def _ram_gb() -> float:
    if sys.platform == "darwin":
        mem = _sysctl("hw.memsize")
        if mem:
            return round(int(mem) / 2**30, 1)
    pages = os.sysconf("SC_PHYS_PAGES")
    page_size = os.sysconf("SC_PAGE_SIZE")
    return round(pages * page_size / 2**30, 1)


def _pkg_version(name: str) -> str:
    try:
        return version(name)
    except PackageNotFoundError:
        return "not-installed"


def checkpoint_revisions(models_lock: Path) -> dict[str, str]:
    """Checkpoint name -> revision, from `models.lock.json` written by download_models.py."""
    if not models_lock.exists():
        return {}
    raw: dict[str, dict[str, str]] = json.loads(models_lock.read_text())
    return {name: entry["revision"] for name, entry in raw.items()}


def collect(models_lock: Path) -> HwInfo:
    device, device_name = pick_device()
    return HwInfo(
        os=f"{platform.system()} {platform.release()}",
        arch=platform.machine(),
        cpu=_cpu_name(),
        ram_gb=_ram_gb(),
        python=platform.python_version(),
        torch=_pkg_version("torch"),
        laya=_pkg_version("laya"),
        device=device,
        device_name=device_name,
        checkpoints=checkpoint_revisions(models_lock),
        created_at=datetime.now(UTC).isoformat(timespec="seconds"),
    )


def write(out: Path, models_lock: Path) -> HwInfo:
    info = collect(models_lock)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(info.model_dump_json(indent=2) + "\n")
    return info
