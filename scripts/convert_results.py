"""
Converts results from the old ideas repo kind to the new format.
"""


import hashlib
import json
from pathlib import Path
import subprocess
import sys


sys.path.insert(0, str(Path(__file__).parent))


from lib import _result


def get_tag_for_hash(cpython_repo, hash):
    result = subprocess.check_output(
        ["git", "name-rev", "--tags", hash], cwd=cpython_repo, encoding="utf-8"
    ).strip()
    _, tag = result.split()
    _, tag = tag.split("/")
    if tag.endswith("^0"):
        return tag[:-2]
    tag, _ = tag.split("~")
    return tag + "+"


def convert_files(ideas_repo, cpython_repo, results_dir):
    for filename in ideas_repo.glob("cpython-*.json"):
        if filename.stem.endswith("pyston"):
            continue

        with open(filename) as fd:
            pyperf_contents = json.load(fd)

        with open(str(filename).replace("pyperformance", "pyston")) as fd:
            pyston_contents = json.load(fd)

        pyperf_contents["benchmarks"].extend(pyston_contents["benchmarks"])

        pyperf_contents["benchmarks"].sort(key=lambda x: x["metadata"]["name"])

        contents = pyperf_contents

        system = "linux"
        machine = "amd64"
        fork = "python"
        ref = "main"
        version = get_tag_for_hash(cpython_repo, contents["metadata"]["commit_id"])[1:]
        cpython_hash = contents["metadata"]["commit_id"][:7]
        benchmark_hash = hashlib.sha256()
        benchmark_hash.update(
            contents["metadata"]["performance_version"].encode("ascii")
        )
        benchmark_hash = benchmark_hash.hexdigest()[:6]
        contents["metadata"]["benchmark_hash"] = benchmark_hash
        contents["metadata"]["publish"] = True

        result = _result.Result(
            system,
            machine,
            fork,
            ref,
            version,
            cpython_hash,
            commit_datetime=contents["metadata"]["commit_date"],
        )

        result.filename.parent.mkdir(exist_ok=True)
        with open(result.filename, "w") as fd:
            json.dump(contents, fd, indent=2)


if __name__ == "__main__":
    ideas_repo = Path(sys.argv[-2])
    cpython_repo = Path(sys.argv[-1])
    results_dir = Path(__file__).parents[1] / "results"

    convert_files(ideas_repo, cpython_repo, results_dir)
