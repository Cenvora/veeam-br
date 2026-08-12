"""Structural checks on the generated per-version SDK packages.

These guard the contract that veeam_br.client.VeeamClient relies on: every
version package must expose the same client classes, login operation and auth
models, regardless of which schema revision produced it.
"""

import importlib
import re

import pytest

from veeam_br.versions import VERSION_TO_PACKAGE

VERSIONS = sorted(VERSION_TO_PACKAGE.items())

REQUIRED_MEMBERS = [
    ("client", ("Client", "AuthenticatedClient")),
    ("api.login.create_token", ("asyncio", "sync")),
    ("models.token_login_spec", ("TokenLoginSpec",)),
    ("models.e_login_grant_type", ("ELoginGrantType",)),
    ("types", ("UNSET", "Unset", "Response")),
]


@pytest.mark.parametrize("version,package", VERSIONS)
@pytest.mark.parametrize("module,members", REQUIRED_MEMBERS)
def test_required_members_exist(version, package, module, members):
    mod = importlib.import_module(f"{package}.{module}")
    for member in members:
        assert hasattr(mod, member), f"{package}.{module} is missing {member}"


@pytest.mark.parametrize("version,package", VERSIONS)
def test_grant_types_cover_password_and_refresh(version, package):
    """VeeamClient authenticates with PASSWORD and refreshes with REFRESH_TOKEN."""
    ELoginGrantType = importlib.import_module(f"{package}.models.e_login_grant_type").ELoginGrantType
    names = {member.name for member in ELoginGrantType}
    assert {"PASSWORD", "REFRESH_TOKEN"} <= names


@pytest.mark.parametrize("version,package", VERSIONS)
def test_login_operation_accepts_api_version_header(version, package):
    """call() always injects x_api_version, so the operation must accept it."""
    create_token = importlib.import_module(f"{package}.api.login.create_token")
    assert "x_api_version" in create_token.asyncio.__code__.co_varnames


@pytest.mark.parametrize("version,package", VERSIONS)
def test_repositories_namespace_resolves(version, package):
    """The namespace used throughout the README docs."""
    mod = importlib.import_module(f"{package}.api.repositories.get_all_repositories")
    assert callable(mod.asyncio)


def test_rev2_operation_modules_match_schema(rev2_schema):
    """Every tagged operation in the schema has a generated module, except the
    binary-response endpoints openapi-python-client cannot model."""
    package = VERSION_TO_PACKAGE["1.3-rev2"]

    # Responses use content types (efi.iso / zip / x-tar) the generator omits.
    known_omissions = {
        ("backupObjects", "createRecoveryMedia"),
        ("recoveryMedia", "downloadRecoveryMedia"),
        ("agents", "generateProtectionGroupPackages"),
        ("agents", "createDiscoveredComputerRecoveryMedia"),
    }

    missing = []
    for path, methods in rev2_schema["paths"].items():
        for method, operation in methods.items():
            if method not in {"get", "post", "put", "patch", "delete"}:
                continue
            tags = operation.get("tags") or []
            operation_id = operation.get("operationId")
            if not tags or not operation_id:
                continue
            tag = tags[0]
            if (tag, operation_id) in known_omissions:
                continue
            module = f"{package}.api.{_snake(tag)}.{_snake(operation_id)}"
            if not _importable(module):
                missing.append(f"{method.upper()} {path} -> {module}")

    assert not missing, "operations without generated modules:\n" + "\n".join(missing)


def _importable(module: str) -> bool:
    """Try the module name, then the variants openapi-python-client produces for
    identifiers that shadow a builtin (``license`` → ``license_``)."""
    package, tag, operation = module.rsplit(".", 2)
    for candidate in (
        module,
        f"{package}.{tag}_.{operation}",
        f"{package}.{tag}.{operation}_",
        f"{package}.{tag}_.{operation}_",
    ):
        try:
            importlib.import_module(candidate)
            return True
        except ModuleNotFoundError:
            continue
    return False


def _snake(name: str) -> str:
    """Mirror openapi-python-client's identifier casing."""
    name = re.sub(r"[^a-zA-Z0-9]+", "_", name)
    name = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    return re.sub(r"_+", "_", name).strip("_").lower()
