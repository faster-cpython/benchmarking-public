import argparse
import io
from pathlib import Path
import re
import sys
import textwrap
from typing import Iterable, List, Optional, TextIO, Tuple


sys.path.insert(0, str(Path(__file__).parent))


from lib import _bases
from lib import _plot
from lib import _result
from lib import _table
from lib import _util


def write_markdown_results(filename: Path, compare: _result.Comparison) -> None:
    if filename.exists():
        filename.unlink()
        compare._contents = None

    contents = compare.contents
    if contents is None:
        return

    header = textwrap.dedent(
        f"""
    # Results vs. {compare.base}

    - fork: {compare.head.fork}
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


def write_plot_results(filename: Path, compare: _result.Comparison) -> None:
    _plot.plot_diff(
        compare.ref,
        compare.head,
        filename,
        (
            f"{compare.head.fork}-{compare.head.ref}-"
            f"{compare.head.cpython_hash}"
            f" vs. {compare.ref.version}"
        ),
    )


RESULT_TYPES = {".md": write_markdown_results, ".png": write_plot_results}


def save_generated_results(
    results: Iterable[_result.Result], force: bool = False
) -> None:
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
                        _util.status(".")
                        func(filename, compare)
                    else:
                        _util.status("/")

        # Remove any outdated comparison files if the bases have changed.
        for filename in result.filename.parent.iterdir():
            match = re.match(r".*-vs-(?P<base>.*)", filename.stem)
            if match is not None:
                if match.group("base") not in result.bases:
                    _util.status("x")
                    filename.unlink()

    print()


def output_results_index(
    fd: TextIO, bases: List[str], results: Iterable[_result.Result], filename: Path
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
                    _table.md_link(
                        result.bases[base].geometric_mean,
                        result.bases[base].filename.with_suffix(".md"),
                        filename,
                    )
                )
            else:
                versus.append("")

        rows.append(
            [
                _table.md_link(result.commit_date, result.filename.parent, filename),
                result.fork,
                result.ref[:10],
                result.version,
                result.cpython_hash,
            ]
            + versus
        )
    _table.output_table(fd, head, rows)


def results_by_platform(
    results: Iterable[_result.Result],
) -> Iterable[Tuple[str, str, Iterable[_result.Result]]]:
    """
    Separate results by platform (system/machine pairs).
    """
    # We want linux first, as the most meaningful/reliable one
    order = ["linux", "windows", "darwin"]

    platforms = sorted(
        set((result.system, result.machine) for result in results),
        key=lambda x: (order.index(x[0]), x[1]),
    )

    for system, machine in platforms:
        yield (
            system,
            machine,
            (
                result
                for result in results
                if result.system == system and result.machine == machine
            ),
        )


def summarize_results(results: Iterable[_result.Result]) -> Iterable[_result.Result]:
    """
    Create a shorter list of results where only the most recent result for each
    Python version is included. Only results from the main `python` fork are
    included.
    """
    results = list(results)
    new_results = []
    prev_version = None
    for result in results[::-1]:
        if result.fork != "python":
            continue
        if result.version != prev_version:
            new_results.append(result)
            prev_version = result.version
    return new_results[::-1]


def generate_index(
    filename: Path,
    bases: List[str],
    results: Iterable[_result.Result],
    summarize: bool = False,
) -> None:
    """
    Generate the tables, by each platform.
    """
    content = io.StringIO()
    for system, machine, results in results_by_platform(results):
        content.write(f"## {system} {machine}\n")
        if summarize:
            results = summarize_results(results)
        output_results_index(content, bases, results, filename)
        content.write("\n")
    _table.replace_section(filename, "table", content.getvalue())


def generate_master_indices(
    bases: List[str], results: Iterable[_result.Result], repo_dir: Path
) -> None:
    """
    Generate both indices:

    - The summary one in `./README.md`
    - The full on in `./results/README.md`
    """
    generate_index(repo_dir / "README.md", bases, results, True)
    generate_index(repo_dir / "results" / "README.md", bases, results, False)


def generate_directory_index(result_dir: Path) -> None:
    results = []
    for filename in sorted(list(result_dir.iterdir())):
        if filename.name == "README.md":
            continue
        results.append(_result.Result.from_filename(filename))

    for result in results:
        if result.result_type == "raw results":
            break
    else:
        raise ValueError(f"Couldn't find raw results in {result_dir}")

    with open(result_dir / "README.md", "w") as fd:
        fd.write("# Results\n\n")

        entries = [
            ("fork", result.fork),
            ("ref", result.ref),
            ("commit hash", _table.link_to_hash(result.cpython_hash, result.fork)),
            ("commit date", result.commit_datetime),
            (
                "commit merge base",
                _table.link_to_hash(result.commit_merge_base, result.fork),
            ),
        ]

        for key, val in entries:
            fd.write(f"- {key}: {val}\n")
        fd.write("\n")

        for system, machine, results in results_by_platform(results):
            results = sorted(results, key=lambda x: (x.extra, x.suffix))
            fd.write(f"## {system} {machine}\n\n")
            for result in results:
                link = _table.md_link(result.result_type, result.filename.name)
                fd.write(f"- {link}\n")
            fd.write("\n")


def generate_directory_indices(results_dir: Path) -> None:
    """
    Generate the indices that go in each results directory.
    """
    for path in results_dir.iterdir():
        if not path.is_dir():
            continue

        generate_directory_index(path)

        _util.status(".")


def main(repo_dir: Path, force: bool = False, bases: Optional[List[str]] = None):
    results_dir = repo_dir / "results"
    if bases is None:
        bases = _bases.get_bases()
    print(f"Comparing to bases {bases}")
    results = _result.load_all_results(bases, results_dir)
    print(f"Found {len(results)} results")
    print("Generating comparison tables")
    save_generated_results(results, force=force)
    print("Generating indices")
    generate_master_indices(bases, results, repo_dir)
    generate_directory_indices(repo_dir / "results")
    print()


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
