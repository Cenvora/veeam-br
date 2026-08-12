"""Guards that pyproject.toml declares what the code actually imports.

Regression test for https://github.com/Cenvora/veeam-br/issues/3, where the
generated SDK imported attrs and python-dateutil without either being declared.
"""

import ast
import sys

import pytest

tomllib = pytest.importorskip("tomllib", reason="requires Python 3.11+ to parse pyproject.toml")

# Import name -> distribution name, for the third-party packages the generated
# SDK and the hand-written client rely on.
IMPORT_TO_DISTRIBUTION = {
    "attr": "attrs",
    "attrs": "attrs",
    "dateutil": "python-dateutil",
    "httpx": "httpx",
}


@pytest.fixture(scope="module")
def declared_dependencies(repo_root):
    with (repo_root / "pyproject.toml").open("rb") as fh:
        pyproject = tomllib.load(fh)
    return {_distribution_name(spec) for spec in pyproject["project"]["dependencies"]}


@pytest.fixture(scope="module")
def imported_distributions(repo_root):
    """Third-party distributions imported anywhere under veeam_br/."""
    found = set()
    for path in (repo_root / "veeam_br").rglob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                roots = [alias.name.split(".")[0] for alias in node.names]
            elif isinstance(node, ast.ImportFrom):
                # level > 0 is a relative import, always first-party
                roots = [node.module.split(".")[0]] if node.module and not node.level else []
            else:
                continue
            for root in roots:
                if root in IMPORT_TO_DISTRIBUTION:
                    found.add(IMPORT_TO_DISTRIBUTION[root])
    return found


def test_every_import_is_declared(imported_distributions, declared_dependencies):
    undeclared = imported_distributions - declared_dependencies
    assert not undeclared, f"imported but not declared in pyproject.toml: {sorted(undeclared)}"


def test_no_unused_dependencies(imported_distributions, declared_dependencies):
    unused = declared_dependencies - imported_distributions
    assert not unused, f"declared in pyproject.toml but never imported: {sorted(unused)}"


def test_requires_python_matches_generated_syntax(repo_root):
    """The generated SDK uses PEP 604 unions (str | None) in signatures, which
    are evaluated at def time and require 3.10+."""
    with (repo_root / "pyproject.toml").open("rb") as fh:
        requires = tomllib.load(fh)["project"]["requires-python"]
    assert requires == ">=3.10"


def test_running_interpreter_satisfies_requires_python():
    assert sys.version_info >= (3, 10)


def _distribution_name(spec: str) -> str:
    for delimiter in ("<", ">", "=", "!", "~", "[", ";", " "):
        spec = spec.split(delimiter)[0]
    return spec.strip()
