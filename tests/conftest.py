import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = REPO_ROOT / "openapi_schemas"


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return REPO_ROOT


@pytest.fixture(scope="session")
def rev2_schema() -> dict:
    """The fixed OpenAPI schema the 1.3-rev2 SDK was generated from."""
    path = SCHEMA_DIR / "vbr_rest_1.3-rev2_fixed.json"
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)
