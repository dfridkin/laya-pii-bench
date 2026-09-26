import os

import pytest


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    if os.environ.get("LAYA_SKIP_MODEL", "0") != "1":
        return
    skip = pytest.mark.skip(reason="LAYA_SKIP_MODEL=1")
    for item in items:
        if "model" in item.keywords:
            item.add_marker(skip)
