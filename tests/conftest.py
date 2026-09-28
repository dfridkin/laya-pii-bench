import os
from collections.abc import Iterator

import pytest


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    if os.environ.get("LAYA_SKIP_MODEL", "0") != "1":
        return
    skip = pytest.mark.skip(reason="LAYA_SKIP_MODEL=1")
    for item in items:
        if "model" in item.keywords:
            item.add_marker(skip)


@pytest.fixture(autouse=True, scope="session")
def _tmp_project_repo() -> Iterator[None]:
    """Calib committed by tests lives in a tmp repo (tests/gitutil.py); the most recent one is the
    project repo for `bench.freeze`. In-process only; the CLI has no such override."""
    from bench import freeze
    from tests import gitutil

    real = freeze.project_root
    freeze.project_root = lambda: gitutil.REPOS[-1] if gitutil.REPOS else real()
    yield
    freeze.project_root = real
