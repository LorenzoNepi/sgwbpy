import pathlib
import shutil

import nox

from sgwbpy import __name__ as __package_name__

# Basic environment.
_ROOT_DIR = pathlib.Path(__file__).parent                           # Root directory of the project
_DOCS_DIR = _ROOT_DIR / "docs"                                      # Documentation directory
_SRC_DIR = _ROOT_DIR / "src" / __package_name__                     # Source code directory
_TESTS_DIR = _ROOT_DIR / "tests"                                    # Unit test directory

# Folders containing code that potentially needs linting.
_LINT_DIRS = ("src", "tests")

# Reuse existing virtualenvs by default.
nox.options.reuse_existing_virtualenvs = True

# Session to cleanup pycache and other temporary files --> nox -s cleanup
@nox.session(venv_backend="none")
def cleanup(_session: nox.Session) -> None:
    """Cleanup temporary files.
    """
    # Remove all the __pycache__ folders.
    for folder_path in (_ROOT_DIR, _SRC_DIR, _TESTS_DIR):
        _path1 = folder_path / "__pycache__"
        _path2 = folder_path / ".mypy_cache"
        _path3 = folder_path / ".nox"
        _path4 = folder_path / ".ruff_cache"
        if _path1.exists():
            shutil.rmtree(_path1)
        if _path2.exists():
            shutil.rmtree(_path2)
        if _path3.exists():
            shutil.rmtree(_path3)
        if _path4.exists():
            shutil.rmtree(_path4)
    # Cleanup the docs.
    _path = _DOCS_DIR / "_build"
    if _path.exists():
        shutil.rmtree(_path)

# Session to create the documentation locally --> nox -s docs
@nox.session(venv_backend="none")
def docs(session: nox.Session) -> None:
    """Build the HTML docs.

    Note this is a nox session with no virtual environment, based on the assumption
    that it is not very interesting to build the documentation with different
    versions of Python or the associated environment, since the final thing will
    be created remotely anyway. (This also illustrates the use of the nox.session
    decorator called with arguments.)
    """
    source_dir = _DOCS_DIR
    output_dir = _DOCS_DIR / "_build" / "html"
    session.run("sphinx-build", "-b", "html", source_dir, output_dir, *session.posargs)

# Session to run ruff on the necessary files
@nox.session
def ruff(session: nox.Session) -> None:
    """Run ruff.
    """
    session.install("ruff")
    session.install(".[dev]")
    session.run("ruff", "check", *session.posargs)

# Session to run pylint
@nox.session
def pylint(session: nox.Session) -> None:
    """Run pylint.
    """
    session.install("pylint")
    session.install(".[dev]")
    session.run("pylint", *_LINT_DIRS, *session.posargs)

# Session to run mypy
@nox.session
def mypy(session: nox.Session) -> None:
    """Run mypy.
    """
    session.install("mypy")
    session.install(".[dev]")
    session.run("mypy", *_LINT_DIRS, *session.posargs )

# Session tu tun unit tests
@nox.session
def test(session: nox.Session) -> None:
    """Run the unit tests.
    """
    session.install("pytest")
    session.install(".[dev]")
    session.run("pytest", *session.posargs)
