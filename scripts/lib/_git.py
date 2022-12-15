# Various git-related utilities


import hashlib
import subprocess


def get_log(format, dirname, ref=None, n=1, extra=[]):
    if ref is None:
        ref = []
    else:
        ref = [ref]
    if n is None:
        n = []
    else:
        n = ["-n", str(n)]
    return subprocess.check_output(
        ["git", "log", f"--pretty=format:{format}"] + n + ref + extra,
        encoding="utf-8",
        cwd=dirname,
    ).strip()


def get_git_hash(dirname):
    return get_log("%h", dirname)


def get_git_commit_date(dirname):
    return get_log("%cI", dirname)


def get_git_merge_base(dirname):
    subprocess.check_call(
        ["git", "remote", "add", "upstream", "https://github.com/python/cpython.git"],
        cwd=dirname,
    )
    subprocess.check_call(["git", "fetch", "upstream"], cwd=dirname)
    return subprocess.check_output(
        ["git", "merge-base", "upstream/main", "HEAD"], cwd=dirname, encoding="utf-8"
    ).strip()


def get_tags(dirname):
    subprocess.check_call(["git", "fetch", "--tags"], cwd=dirname)
    return subprocess.check_output(
        ["git", "tag"], cwd=dirname, encoding="utf-8"
    ).splitlines()


def generate_combined_hash(dirs):
    hash = hashlib.sha256()
    for dirname in dirs:
        subhash = get_git_hash(dirname)
        hash.update(subhash.encode("ascii"))
    return hash.hexdigest()[:6]
