import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
import textwrap
from typing import Optional, Union


sys.path.insert(0, str(Path(__file__).parent))


from lib import git
from lib.result import Result


BENCHMARK_JSON = Path("benchmark.json")
GITHUB_URL = "https://github.com/faster-cpython/benchmarking"


def run_benchmarks(python: Union[Path, str], benchmarks: str, fast: bool) -> None:
    if benchmarks.strip() == "":
        benchmarks = "all"

    if BENCHMARK_JSON.is_file():
        BENCHMARK_JSON.unlink()

    if fast:
        fast_arg = ["--fast"]
    else:
        fast_arg = []

    subprocess.call(
        [
            sys.executable,
            "-m",
            "pyperformance",
            "run",
        ]
        + fast_arg
        + [
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

    if not Path(BENCHMARK_JSON).is_file():
        print("No benchmark file created.")
        sys.exit(1)
    with open(BENCHMARK_JSON) as fd:
        contents = json.load(fd)
    if len(contents.get("benchmarks", [])) == 0:
        print("No benchmarks were run.")
        sys.exit(1)


def update_metadata(
    filename: Path,
    fork: str,
    ref: str,
    publish: str,
    cpython="cpython",
    run_id: Optional[str] = None,
) -> None:
    publish_bool = publish.lower() == "true"

    with open(filename) as fd:
        content = json.load(fd)

    metadata = content.setdefault("metadata", {})

    metadata["commit_id"] = git.get_git_hash(cpython)
    metadata["commit_fork"] = fork
    metadata["commit_branch"] = ref
    metadata["commit_date"] = git.get_git_commit_date(cpython)
    if fork != "python" and ref != "main":
        merge_base = git.get_git_merge_base(cpython)
        if merge_base is not None:
            metadata["commit_merge_base"] = merge_base
    metadata["benchmark_hash"] = git.generate_combined_hash(
        ["pyperformance", "pyston-benchmarks"]
    )
    metadata["publish"] = publish_bool
    if run_id is not None:
        metadata["github_action_url"] = f"{GITHUB_URL}/actions/runs/{run_id}"

    with open(filename, "w") as fd:
        json.dump(content, fd, indent=2)


def copy_to_directory(filename: Path, python: str, fork: str, ref: str) -> None:
    result = Result.from_scratch(python, fork, ref)
    result.filename.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(filename, result.filename)


def run_summarize_stats(python: str, fork: str, ref: str, publish: str) -> None:
    summarize_stats_path = (
        Path(python).parent / "Tools" / "scripts" / "summarize_stats.py"
    )

    table = subprocess.check_output(
        [python, summarize_stats_path, "--json-output", "pystats.json"],
        encoding="utf-8",
    )

    header = textwrap.dedent(
        f"""
    # Pystats results

    - fork: {fork}
    - ref: {ref}
    - commit hash: {git.get_git_hash('cpython')[:7]}
    - commit date: {git.get_git_commit_date('cpython')}

    """
    )

    result = Result.from_scratch(python, fork, ref, ["pystats"])
    result.filename.parent.mkdir(parents=True, exist_ok=True)

    with open(
        result.filename.with_suffix(".md"),
        "w",
    ) as fd:
        fd.write(header)
        fd.write(table)

    pystats_json = Path("pystats.json")
    if pystats_json.is_file():
        update_metadata(pystats_json, fork, ref, publish)
        shutil.copy(
            pystats_json,
            result.filename.with_suffix(".json"),
        )
    else:
        print(
            "WARNING: No pystats.json file generated. "
            "This is expected with CPython < 3.12"
        )


def main(
    mode: str,
    python: str,
    fork: str,
    ref: str,
    benchmarks: str,
    publish: str,
    fast: bool,
    run_id: Optional[str],
) -> None:
    run_benchmarks(python, benchmarks, fast)
    if mode == "benchmark":
        update_metadata(BENCHMARK_JSON, fork, ref, publish, run_id=run_id)
        copy_to_directory(BENCHMARK_JSON, python, fork, ref)
    elif mode == "pystats":
        run_summarize_stats(python, fork, ref, publish)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        """
        Run benchmarks in `pyperformance` with the given python executable. Add
        additional metadata to a benchmark results file and then copy it to the
        correct location in the results tree.
        """
    )
    parser.add_argument(
        "mode", choices=["benchmark", "pystats"], help="The mode of execution"
    )
    parser.add_argument("python", help="The path to the Python executable")
    parser.add_argument("fork", help="The fork of CPython")
    parser.add_argument("ref", help="The git ref in the fork")
    parser.add_argument("benchmarks", help="The benchmarks to run")
    parser.add_argument("publish", help="Publish results to the public repo")
    parser.add_argument(
        "--fast", action="store_true", help="Run fewer iterations of the benchmarks"
    )
    parser.add_argument("--run_id", default=None, type=str, help="The github run id")
    args = parser.parse_args()

    main(
        args.mode,
        args.python,
        args.fork,
        args.ref,
        args.benchmarks,
        args.publish,
        args.fast,
        args.run_id,
    )
