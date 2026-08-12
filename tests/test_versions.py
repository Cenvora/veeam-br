import importlib

import pytest

from veeam_br.versions import VERSION_TO_PACKAGE

SCHEMA_DIR = "openapi_schemas"


@pytest.mark.parametrize("version,package", sorted(VERSION_TO_PACKAGE.items()))
def test_package_is_importable(version, package):
    importlib.import_module(package)


@pytest.mark.parametrize("version,package", sorted(VERSION_TO_PACKAGE.items()))
def test_package_name_matches_version(version, package):
    """1.3-rev2 → veeam_br.v1_3_rev2"""
    expected = "veeam_br.v" + version.replace(".", "_").replace("-", "_")
    assert package == expected


@pytest.mark.parametrize("version,package", sorted(VERSION_TO_PACKAGE.items()))
def test_schemas_are_present(version, package, repo_root):
    """Every mapped version keeps both its raw and fixed schema on disk."""
    for suffix in ("", "_fixed"):
        path = repo_root / SCHEMA_DIR / f"vbr_rest_{version}{suffix}.json"
        assert path.is_file(), f"missing {path.name}"


def test_rev2_is_supported():
    assert "1.3-rev2" in VERSION_TO_PACKAGE
