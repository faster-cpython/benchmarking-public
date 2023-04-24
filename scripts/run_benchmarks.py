import argparse
import csv
import json
from pathlib import Path
import shutil
import subprocess
import sys
import textwrap
from typing import Iterable, List, Optional, Union


sys.path.insert(0, str(Path(__file__).parent))


from lib import git
from lib.result import Result


REPO_ROOT = Path(__file__).parents[1]
BENCHMARK_JSON = REPO_ROOT / "benchmark.json"
PROFILING_RESULTS = REPO_ROOT / "profiling" / "results"
GITHUB_URL = "https://github.com/faster-cpython/benchmarking"


class NoBenchmarkError(Exception):
    pass


def run_benchmarks(
    python: Union[Path, str],
    benchmarks: str,
    command_prefix: List[str] = [],
    test_mode: bool = False,
) -> None:
    if benchmarks.strip() == "":
        benchmarks = "all"

    if BENCHMARK_JSON.is_file():
        BENCHMARK_JSON.unlink()

    if test_mode:
        fast_arg = ["--fast"]
    else:
        fast_arg = []

    subprocess.call(
        command_prefix
        + [
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
        raise NoBenchmarkError("No benchmark file created.")
    with open(BENCHMARK_JSON) as fd:
        contents = json.load(fd)
    if len(contents.get("benchmarks", [])) == 0:
        raise NoBenchmarkError("No benchmarks were run.")


def perf_to_csv(lines: Iterable[str], output: Path):
    rows = []
    for line in lines:
        line = line.strip()
        if line.startswith("#") or line == "":
            continue
        children, self_time, _, shared, _, symbol = line.split(maxsplit=5)
        children = float(children[:-1])
        self = float(self_time[:-1])
        if children > 0.0 or self > 0.0:
            rows.append([self, children, shared, symbol])

    rows.sort(key=lambda x: x[0], reverse=True)

    with open(output, "w") as fd:
        csvwriter = csv.writer(fd)
        csvwriter.writerow(["self", "children", "object", "symbol"])
        for row in rows:
            csvwriter.writerow(row)


def collect_perf(python: Union[Path, str], benchmarks: str):
    if benchmarks.strip() == "":
        benchmarks = "all"

    output = subprocess.check_output(
        [
            sys.executable,
            "-m",
            "pyperformance",
            "list",
            "--manifest",
            "benchmarks.manifest",
            "--benchmarks",
            benchmarks,
        ],
        encoding="utf-8",
    )

    all_benchmarks = [
        line[2:].strip() for line in output.splitlines() if line.startswith("- ")
    ]

    perf_data = Path("perf.data")
    for benchmark in all_benchmarks:
        if perf_data.exists():
            perf_data.unlink()

        try:
            run_benchmarks(
                python,
                benchmark,
                ["perf", "record", "--call-graph=dwarf", "-o", "perf.data", "--"],
            )
        except NoBenchmarkError:
            pass
        else:
            if perf_data.exists():
                output = subprocess.check_output(
                    [
                        "perf",
                        "report",
                        "--stdio",
                        "-g",
                        "none",
                        "-i",
                        "perf.data",
                    ],
                    encoding="utf-8",
                )
                perf_to_csv(
                    output.splitlines(), PROFILING_RESULTS / f"{benchmark}.perf.csv"
                )


def update_metadata(
    filename: Path,
    fork: str,
    ref: str,
    cpython="cpython",
    run_id: Optional[str] = None,
) -> None:
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
    if run_id is not None:
        metadata["github_action_url"] = f"{GITHUB_URL}/actions/runs/{run_id}"

    with open(filename, "w") as fd:
        json.dump(content, fd, indent=2)


def copy_to_directory(filename: Path, python: str, fork: str, ref: str) -> None:
    result = Result.from_scratch(python, fork, ref)
    result.filename.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(filename, result.filename)


def run_summarize_stats(python: str, fork: str, ref: str) -> None:
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
        update_metadata(pystats_json, fork, ref)
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
    perf: bool,
    test_mode: bool,
    run_id: Optional[str],
) -> None:
    if perf:
        collect_perf(python, benchmarks)
    else:
        run_benchmarks(python, benchmarks, [], test_mode)
    if mode == "benchmark":
        update_metadata(BENCHMARK_JSON, fork, ref, run_id=run_id)
        copy_to_directory(BENCHMARK_JSON, python, fork, ref)
    elif mode == "pystats":
        run_summarize_stats(python, fork, ref)


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
    parser.add_argument("perf", help="Collect Linux perf profiling data")
    parser.add_argument(
        "--test_mode",
        action="store_true",
        help="Run in a special mode for unit testing",
    )
    parser.add_argument("--run_id", default=None, type=str, help="The github run id")
    args = parser.parse_args()

    if args.test_mode:
        import socket

        def gethostname():
            return "pyperf"

        socket.gethostname = gethostname

    main(
        args.mode,
        args.python,
        args.fork,
        args.ref,
        args.benchmarks,
        args.perf.lower() != "false",
        args.test_mode,
        args.run_id,
    )
