import argparse
import datetime
import io
from pathlib import Path
import re
import sys
import textwrap
from typing import Dict, Iterable, List, Optional, TextIO, Tuple
from urllib.parse import unquote


sys.path.insert(0, str(Path(__file__).parent))


from lib.bases import get_bases
from lib import plot
from lib.result import load_all_results, remove_duplicate_results, Comparison, Result
from lib import table
from lib import util


def _tuple_to_nested_dicts(entries: List[Tuple], d: Optional[Dict] = None) -> Dict:
    def recurse(entry: Tuple, d: Dict):
        if len(entry) == 2:
            d.setdefault(entry[0], [])
            if entry[1] not in d[entry[0]]:
                d[entry[0]].append(entry[1])
        else:
            recurse(entry[1:], d.setdefault(entry[0], {}))

    assert len(set(len(x) for x in entries)) == 1

    if d is None:
        d = {}

    for entry in entries:
        recurse(entry, d)
    return d


def write_markdown_results(filename: Path, compare: Comparison) -> None:
    if filename.exists():
        filename.unlink()
        compare = compare.copy()

    contents = compare.contents
    if contents is None:
        return

    header = textwrap.dedent(
        f"""
    # Results vs. {compare.base}

    - fork: {unquote(compare.head.fork)}
    - ref: {compare.head.ref}
    - machine: {compare.head.system}-{compare.head.machine}
    - commit hash: {compare.head.cpython_hash}
    - commit date: {compare.head.commit_date}
    - overall geometric mean: {compare.geometric_mean}

    """
    )

    with open(filename, "w") as fd:
        fd.write(header)
        fd.write(contents)


def write_plot_results(filename: Path, compare: Comparison) -> None:
    plot.plot_diff(
        compare.ref,
        compare.head,
        filename,
        (
            f"{unquote(compare.head.fork)}-{compare.head.ref}-"
            f"{compare.head.cpython_hash}"
            f" vs. {compare.ref.version}"
        ),
    )


RESULT_TYPES = {".md": write_markdown_results, ".png": write_plot_results}


def save_generated_results(results: Iterable[Result], force: bool = False) -> None:
    """
    Write out the comparison tables and plots for every result.

    By default, files are only written out if they don't already exist. To force
    regeneration, pass ``force=True``.
    """
    for result in results:
        for compare in result.bases.values():
            if compare.filename is not None:
                for suffix, func in RESULT_TYPES.items():
                    filename = compare.filename.with_suffix(suffix)
                    if not filename.exists() or force:
                        util.status(".")
                        func(filename, compare)
                    else:
                        util.status("/")

        # Remove any outdated comparison files if the bases have changed.
        for filename in result.filename.parent.iterdir():
            match = re.match(r"(?P<root>.*)-vs-(?P<base>.*)", filename.stem)
            if match is not None:
                if (
                    match.group("root") == result.filename.stem
                    and match.group("base") not in result.bases
                ) or not (filename.parent / (match.group("root") + ".json")).exists():
                    util.status("x")
                    filename.unlink()

    print()


def output_results_index(
    fd: TextIO, bases: List[str], results: Iterable[Result], filename: Path
):
    """
    Outputs a results index table.
    """
    bases = bases + ["base"]

    head = ["date", "fork", "ref", "version", "hash"] + [
        f"vs. {base}:" for base in bases
    ]

    rows = []
    for result in results:
        versus = []
        for base in bases:
            if base in result.bases:
                versus.append(
                    table.md_link(
                        result.bases[base].geometric_mean,
                        result.bases[base].filename.with_suffix(".md"),
                        filename,
                    )
                )
            else:
                versus.append("")

        rows.append(
            [
                table.md_link(result.commit_date, result.filename.parent, filename),
                unquote(result.fork),
                result.ref[:10],
                result.version,
                result.cpython_hash,
            ]
            + versus
        )
    table.output_table(fd, head, rows)


def sort_runner_names(runner_names: Iterable[str]) -> List[str]:
    # We want linux first, as the most meaningful/reliable one
    order = ["linux", "windows", "darwin"]

    def sorter(val):
        if val is None:
            return ()
        return order.index(val.split()[0]), val

    return sorted(runner_names, key=sorter)


def results_by_runner(
    results: Iterable[Result],
) -> Iterable[Tuple[str, Iterable[Result]]]:
    """
    Separate results by the runner used.
    """
    by_runner = {}
    for result in results:
        by_runner.setdefault(result.runner, []).append(result)

    for runner_name in sort_runner_names(by_runner.keys()):
        yield (runner_name, by_runner[runner_name])


def summarize_results(results: Iterable[Result], bases: List[str]) -> Iterable[Result]:
    """
    Create a shorter list of results which includes:

    - The 3 most recent
    - Any results in the last 3 days
    - The bases
    """
    results = list(results)
    new_results = []
    earliest = (datetime.date.today() - datetime.timedelta(days=3)).isoformat()
    for i, result in enumerate(results):
        if i < 3 or result.run_date >= earliest or result.version in bases:
            new_results.append(result)
    return new_results


def generate_index(
    filename: Path,
    bases: List[str],
    results: Iterable[Result],
    summarize: bool = False,
) -> None:
    """
    Generate the tables, by each platform.
    """
    content = io.StringIO()
    for runner, results in results_by_runner(results):
        content.write(f"## {runner}\n")
        if summarize:
            results = summarize_results(results, bases)
        output_results_index(content, bases, results, filename)
        content.write("\n")
    table.replace_section(filename, "table", content.getvalue())


def generate_master_indices(
    bases: List[str], results: Iterable[Result], repo_dir: Path
) -> None:
    """
    Generate both indices:

    - The summary one in `./README.md`
    - The full one in `./RESULTS.md`

    (For the ideas repo, the second file is at `results/README.md`).
    """
    generate_index(repo_dir / "README.md", bases, results, True)
    results_file = repo_dir / "RESULTS.md"
    if not results_file.is_file():
        results_file = repo_dir / "results" / "README.md"
    generate_index(results_file, bases, results, False)


def find_different_benchmarks(head: Result, ref: Result) -> Tuple[List[str], List[str]]:
    def get_benchmark_names(contents):
        for benchmark in contents["benchmarks"]:
            if "metadata" in benchmark:
                yield benchmark["metadata"]["name"]
            else:
                yield contents["metadata"]["name"]

    head_benchmarks = set(get_benchmark_names(head.contents))
    base_benchmarks = set(get_benchmark_names(ref.contents))
    return (
        sorted(base_benchmarks - head_benchmarks),
        sorted(head_benchmarks - base_benchmarks),
    )


def get_directory_indices_entries(
    results: List[Result],
) -> List[Tuple[Path, Optional[str], Optional[str], str]]:
    entries = []
    dirpaths = set()
    refs = {}
    for result in results:
        dirpath = result.filename.parent
        dirpaths.add(dirpath)
        refs.setdefault(dirpath, set()).add(result.ref)
        entries.append((dirpath, None, None, f"fork: {unquote(result.fork)}"))
        entries.append((dirpath, None, None, f"version: {result.version}"))
        link = table.link_to_hash(result.cpython_hash, result.fork)
        entries.append((dirpath, None, None, f"commit hash: {link}"))
        entries.append((dirpath, None, None, f"commit date: {result.commit_datetime}"))
        if result.commit_merge_base is not None:
            link = table.link_to_hash(result.commit_merge_base, result.fork)
            entries.append((dirpath, None, None, f"commit merge base: {link}"))
        if result.github_action_url is not None:
            link = table.md_link("GitHub Action run", result.github_action_url)
            entries.append((dirpath, result.runner, None, link))

        entries.append(
            (dirpath, result.runner, None, f"cpu model: {result.cpu_model_name}")
        )
        entries.append((dirpath, result.runner, None, f"platform: {result.platform}"))

        for base, compare in result.bases.items():
            entries.append((dirpath, result.runner, base, compare.geometric_mean))
            missing_benchmarks, new_benchmarks = find_different_benchmarks(
                result, compare.ref
            )
            if len(missing_benchmarks):
                prefix = base == "base" and "🔴 " or ""
                entries.append(
                    (
                        dirpath,
                        result.runner,
                        base,
                        f"missing benchmarks: {prefix}{', '.join(missing_benchmarks)}",
                    )
                )
            if len(new_benchmarks):
                entries.append(
                    (
                        dirpath,
                        result.runner,
                        base,
                        f"new benchmarks: {', '.join(new_benchmarks)}",
                    )
                )

    for dirpath in dirpaths:
        entries.append(
            (dirpath, None, None, f"ref: {', '.join(sorted(refs[dirpath]))}")
        )

        for filename in sorted(list(dirpath.iterdir())):
            if filename.name == "README.md":
                continue
            result = Result.from_filename(filename)
            type, base = result.result_info
            entries.append(
                (
                    dirpath,
                    result.runner,
                    base,
                    table.md_link(type, result.filename.name),
                )
            )

    return entries


def generate_directory_indices(results: List[Result]) -> None:
    """
    Generate the indices that go in each results directory.
    """

    # The data is in a considerably different form than what we need to write
    # it out. Therefore, this first generates a list of tuples of the form:
    #    (dirpath, runner, base, entry)
    # then converts that to a nested dictionary and then writes it out to each
    # of the README.md files.

    entries = get_directory_indices_entries(results)
    structure = _tuple_to_nested_dicts(entries)

    for dirpath, dirresults in structure.items():
        util.status(".")
        with open(dirpath / "README.md", "w") as fd:
            fd.write("# Results\n\n")
            table.write_md_list(fd, dirresults[None][None])
            for runner in sort_runner_names(dirresults.keys()):
                if runner is None:
                    continue
                data = dirresults[runner]
                fd.write(f"## {runner}\n\n")
                table.write_md_list(fd, data[None])
                for base, subdata in data.items():
                    if base is None:
                        continue
                    fd.write(f"### vs. {base}\n\n")
                    table.write_md_list(fd, subdata)
    print()


def main(repo_dir: Path, force: bool = False, bases: Optional[List[str]] = None):
    results_dir = repo_dir / "results"
    if bases is None:
        bases = get_bases()
    if len(bases) == 0:
        raise ValueError("Must have at least one base specified")
    print(f"Comparing to bases {bases}")
    remove_duplicate_results(results_dir)
    results = load_all_results(bases, results_dir)
    print(f"Found {len(results)} results")
    print("Generating comparison tables")
    save_generated_results(results, force=force)
    print("Generating indices")
    generate_master_indices(bases, results, repo_dir)
    generate_directory_indices(results)
    print("Generating longitudinal plot")
    plot.longitudinal_plot(results, repo_dir / "longitudinal.png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Generate master index tables and comparison plots for all of the results.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "repo_dir",
        nargs="?",
        type=Path,
        default=Path(__file__).parents[1],
        help="The location of the results repository",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Regenerate the comparison files, even if they already exist.",
    )

    args = parser.parse_args()

    if not args.repo_dir.is_dir():
        print(f"{args.repo_dir} is not a directory.")
        sys.exit(1)

    main(args.repo_dir, force=args.force)
