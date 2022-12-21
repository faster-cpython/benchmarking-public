# Various git-related utilities


import hashlib
import subprocess
from typing import Iterable, List, Optional


def get_log(
    format: str,
    dirname,
    ref: Optional[str] = None,
    n: int = 1,
    extra: List[str] = [],
) -> str:
    """
    format: The git pretty format string for each log entry
    dirname: Local checkout of the repository
    ref: If provided, the git ref to show
    n: If < 1, show full log, otherwise the number of entries to show
    extra: Extra arguments to pass to `git log`
    """
    if ref is None:
        ref_args = []
    else:
        ref_args = [ref]
    if n < 1:
        n_args = []
    else:
        n_args = ["-n", str(n)]
    return subprocess.check_output(
        ["git", "log", f"--pretty=format:{format}"] + n_args + ref_args + extra,
        encoding="utf-8",
        cwd=dirname,
    ).strip()


def get_git_hash(dirname) -> str:
    return get_log("%h", dirname)


def get_git_commit_date(dirname) -> str:
    return get_log("%cI", dirname)


def get_git_merge_base(dirname) -> str:
    subprocess.check_call(
        ["git", "remote", "add", "upstream", "https://github.com/python/cpython.git"],
        cwd=dirname,
    )
    subprocess.check_call(
        ["git", "fetch", "upstream", "main", "--depth", "50"], cwd=dirname
    )
    return subprocess.check_output(
        ["git", "merge-base", "upstream/main", "HEAD"], cwd=dirname, encoding="utf-8"
    ).strip()


def get_tags(dirname) -> List[str]:
    subprocess.check_call(["git", "fetch", "--tags"], cwd=dirname)
    return subprocess.check_output(
        ["git", "tag"], cwd=dirname, encoding="utf-8"
    ).splitlines()


def generate_combined_hash(dirs: Iterable) -> str:
    hash = hashlib.sha256()
    for dirname in dirs:
        subhash = get_git_hash(dirname)
        hash.update(subhash.encode("ascii"))
    return hash.hexdigest()[:6]
