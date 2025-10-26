import pathlib
import subprocess

from ._version import __version__ as __base_version__

# The goal is to be able to keep track of the local modifications (in a working
# copy of a git repo) while developing. The user will only see the __version__
# variable defined in the _version.py file, while you will be able to log,
# access and recognize all the subsequent changes of the code. This will make it
# easier to find and correct bugs


def _git_suffix() -> str:
    """
    This will return something along the lines of ``+gf0f18e6.dirty``, which is
    a string (hash) used by git to identify different commits
    """

    # pylint: disable=broad-except

    kwargs = dict(cwd=pathlib.Path(__file__).parent, stderr=subprocess.DEVNULL)

    # Note:
    # - cwd=pathlib.Path(__file__).parent
    #   defines the working directory as the one with this file
    # - stderr=subprocess.DEVNULL)
    #   silences Git errors

    try:
        # git rev-parse --short HEAD
        # returns the short SHA of the current HEAD in bits. The command is
        # run through the check_output function of the subprocess module,
        # then the sequence of bits is converted in the corresponding string
        # (UTF-8 convention) by the .decode() instruction. .strip() removes
        # newlines and spaces.

        args = ["git", "rev-parse", "--short", "HEAD"]
        sha = subprocess.check_output(args, **kwargs).decode().strip()  # type: ignore
        suffix = f"+g{sha}"

        # If we have uncommitted changes, we want to append a `.dirty`
        # to the version suffix.

        # git diff --quiet returns 0 if there are no differences between
        # the working tree and the HEAD (i.e., the repository is "clean"), or 1
        # if there are uncommitted changes.

        args = ["git", "diff", "--quiet"]
        if subprocess.call(args, stdout=subprocess.DEVNULL, **kwargs) != 0:  # type: ignore
            suffix = f"{suffix}.dirty"
        return suffix
    except Exception:
        return ""


__version__ = f"{__base_version__}{_git_suffix()}"
