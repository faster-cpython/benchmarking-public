"""
Utility to compare a matrix of arbitrary commits, for when the usual key
versions or git merge base aren't enough.
"""

import argparse
from pathlib import Path
import sys
from typing import Iterable, List, Set, Tuple


sys.path.insert(0, str(Path(__file__).parent))


from lib import result as mod_result
from lib import plot


def parse_commit(commit: str) -> Tuple[str, str]:
    if "," in commit:
        return tuple(commit.split(",", 1))
    else:
        return (commit, commit)


def get_machines(results: Iterable[mod_result.Result]) -> Set[str]:
    return set(result.nickname for result in results)


def compare_pair(
    output_dir: Path,
    ref_name: str,
    ref: mod_result.Result,
    head_name: str,
    head: mod_result.Result,
    counter: List[int],
) -> str:
    print(f"Comparing {counter[0]+1}/{counter[1]}", end="\r")
    counter[0] += 1
    name = f"{head_name}-vs-{ref_name}"
    comparison = mod_result.Comparison(ref, head, "")
    if comparison.contents is None:
        raise RuntimeError()
    with open(output_dir / f"{name}.md", "w", encoding="utf-8") as fd:
        fd.write(comparison.contents)
    plot.plot_diff(ref, head, output_dir / f"{name}.png", f"{head_name} vs. {ref_name}")

    return f"{comparison.geometric_mean} [table]({name}.md) [plot]({name}.png)"


def do_one_to_many(
    fd,
    parsed_commits: List[Tuple[str, str, List[mod_result.Result]]],
    machine: str,
    output_dir: Path,
    counter: List[int],
) -> None:
    _, first_name, first_results = parsed_commits[0]
    first_result = [result for result in first_results if result.nickname == machine][0]
    fd.write("| commit | change |\n")
    fd.write("| -- | -- |\n")
    for hash, name, results in parsed_commits[1:]:
        result = [result for result in results if result.nickname == machine][0]
        link = compare_pair(output_dir, first_name, first_result, name, result, counter)
        fd.write(f"| {name} ({hash}) | {link} |\n")


def do_many_to_many(
    fd,
    parsed_commits: List[Tuple[str, str, List[mod_result.Result]]],
    machine: str,
    output_dir: Path,
    counter: List[int],
) -> None:
    fd.write("| ")
    fd.write(" | ".join([""] + [f"{x[1]} ({x[0]})" for x in parsed_commits]))
    fd.write(" |\n")
    fd.write("| ")
    fd.write(" | ".join(["--"] * (len(parsed_commits) + 1)))
    fd.write(" |\n")
    for hash1, name1, results1 in parsed_commits:
        result1 = [result for result in results1 if result.nickname == machine][0]
        fd.write(f"| {name1} |")
        for hash2, name2, results2 in parsed_commits:
            if hash1 == hash2:
                fd.write(" |")
                continue
            else:
                result2 = [result for result in results2 if result.nickname == machine][
                    0
                ]
                link = compare_pair(output_dir, name1, result1, name2, result2, counter)
                fd.write(f" {link} |")
        fd.write("\n")


def main(commits: List[str], output_dir: str, comparison_type: str):
    results = mod_result.load_all_results(
        None, Path(__file__).parents[1] / "results", sorted=False
    )

    if len(commits) < 2:
        raise ValueError("Must provide at least 2 commits")

    parsed_commits = []
    machines = set()

    for commit in commits:
        commit_hash, name = parse_commit(commit)

        subresults = []
        for result in results:
            if result.cpython_hash.startswith(commit_hash):
                subresults.append(result)

        if len(subresults) == 0:
            raise ValueError(f"Couldn't find commit {commit_hash}")

        parsed_commits.append((commit_hash, name, subresults))

        if len(machines) == 0:
            machines = get_machines(subresults)
        else:
            machines &= get_machines(subresults)

    if len(machines) == 0:
        raise ValueError("No single machine in common with all of the results")

    output_dir_path = Path(output_dir)
    if not output_dir_path.exists():
        output_dir_path.mkdir()

    if comparison_type == "1:n":
        total = (len(parsed_commits) - 1) * len(machines)
        func = do_one_to_many
    elif comparison_type == "n:n":
        total = ((len(parsed_commits) ** 2) - len(parsed_commits)) * len(machines)
        func = do_many_to_many
    else:
        raise ValueError(f"Unknown comparison type {comparison_type}")

    with open(output_dir_path / "README.md", "w", encoding="utf-8") as fd:
        for machine in machines:
            fd.write(f"# {machine}\n\n")
            func(fd, parsed_commits, machine, output_dir_path, [0, total])
            fd.write("\n")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        """
        Generate a set of comparisons between arbitrary commits. The commits
        must already exist in the dataset.
        """
    )

    parser.add_argument(
        "--output-dir", required=True, help="Directory to output results to."
    )
    parser.add_argument(
        "commit",
        nargs="+",
        help="""
            Commits to compare. Must be a git hash prefix. May optionally have a
            friendly name after a comma, e.g. c0ffee,main
        """,
    )
    parser.add_argument(
        "--type",
        choices=["1:n", "n:n"],
        default="1:n",
        help="""
            Compare the first commit to all others, or do the full product of all
            commits
        """,
    )

    args = parser.parse_args()

    try:
        main(args.commit, args.output_dir, args.type)
    except ValueError as e:
        print(str(e))
        sys.exit(1)
