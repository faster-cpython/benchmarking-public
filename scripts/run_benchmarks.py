import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys


sys.path.insert(0, str(Path(__file__).parent))


from lib import _git
from lib import _result


BENCHMARK_JSON = "benchmark.json"


def run_benchmarks(python, benchmarks):
    if benchmarks.strip() == "":
        benchmarks = "all"

    returncode = subprocess.call(
        [
            "python",
            "-m",
            "pyperformance",
            "run",
            "-o",
            BENCHMARK_JSON,
            "--manifest",
            "benchmarks.manifest",
            "--benchmarks",
            benchmarks,
            "--python",
            python,
        ]
    )

    # pyperformance frequently returns an error if any of the benchmarks failed.
    # We only want to fail if things are worse than that.

    if returncode:
        if not Path(BENCHMARK_JSON).is_file():
            print("No benchmark file created.")
            sys.exit(1)
        with open(BENCHMARK_JSON) as fd:
            contents = json.load(fd)
        if len(contents.get("benchmarks", [])) == 0:
            print("No benchmarks were run.")
            sys.exit(1)


def update_metadata(filename, fork, ref, publish):
    publish = publish.lower() == "true"

    with open(filename) as fd:
        content = json.load(fd)

    metadata = content["metadata"]

    metadata["commit_id"] = _git.get_git_hash("cpython")
    metadata["commit_fork"] = fork
    metadata["commit_branch"] = ref
    metadata["commit_date"] = _git.get_git_commit_date("cpython")
    if fork != "python" and ref != "main":
        metadata["commit_merge_base"] = _git.get_git_merge_base("cpython")
    metadata["benchmark_hash"] = _git.generate_combined_hash(
        ["pyperformance", "pyston-benchmarks"]
    )
    metadata["publish"] = publish

    with open(filename, "w") as fd:
        json.dump(content, fd, indent=2)


def copy_to_directory(filename, python, fork, ref):
    result = _result.Result.from_scratch(python, fork, ref)
    result.filename.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(filename, result.filename)


def main(python, fork, ref, benchmarks, publish):
    run_benchmarks(python, benchmarks)
    update_metadata(BENCHMARK_JSON, fork, ref, publish)
    copy_to_directory(BENCHMARK_JSON, python, fork, ref)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        """
        Run benchmarks in `pyperformance` with the given python executable. Add
        additional metadata to a benchmark results file and then copy it to the
        correct location in the results tree.
        """
    )
    parser.add_argument("python", help="The path to the Python executable")
    parser.add_argument("fork", help="The fork of CPython")
    parser.add_argument("ref", help="The git ref in the fork")
    parser.add_argument("benchmarks", help="The benchmarks to run")
    parser.add_argument("publish", help="Publish results to the public repo")
    args = parser.parse_args()

    main(args.python, args.fork, args.ref, args.benchmarks, args.publish)
