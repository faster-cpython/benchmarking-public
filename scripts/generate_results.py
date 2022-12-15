import argparse
import io
from pathlib import Path
import sys


sys.path.insert(0, str(Path(__file__).parent))


from lib import _bases
from lib import _plot
from lib import _result
from lib import _table
from lib import _util


def save_generated_results(results, force=False):
    """
    Write out the comparison tables and plots for every result.

    By default, files are only written out if they don't already exist. To force
    regeneration, pass ``force=True``.
    """
    for result in results:
        for compare in result.bases.values():
            if compare.filename is not None:
                if not compare.filename.with_suffix(".md").exists() or force:
                    _util.status(".")
                    contents = compare.contents
                    with open(compare.filename.with_suffix(".md"), "w") as fd:
                        fd.write(contents)
                else:
                    _util.status("/")
                if not compare.filename.with_suffix(".png").exists() or force:
                    _util.status(".")
                    _plot.plot_diff(
                        compare.ref,
                        compare.head,
                        compare.filename.with_suffix(".png"),
                        (
                            f"{compare.head.fork}-{compare.head.ref}-"
                            f"{compare.head.cpython_hash}"
                            f" vs. {compare.ref.version}"
                        ),
                    )
                else:
                    _util.status("/")
    print()


def output_results_table(fd, bases, results, filename):
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
                result.ref,
                result.version,
                result.cpython_hash,
            ]
            + versus
        )
    _table.output_table(fd, head, rows)


def results_by_platform(results):
    """
    Separate results by platform (system/machine pairs).
    """
    platforms = set()
    for result in results:
        platforms.add((result.system, result.machine))
    platforms = sorted(list(platforms))

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


def summarize_results(results):
    """
    Create a shorter list of results where only the most recent for each Python
    version is included.
    """
    results = list(results)
    new_results = []
    prev_version = None
    for result in results[::-1]:
        if not (result.fork == "python" and result.ref == "main"):
            continue
        if result.version != prev_version:
            new_results.append(result)
            prev_version = result.version
    return new_results[::-1]


def generate_table(filename, bases, results, summarize):
    """
    Generate the tables, by each platform.
    """
    content = io.StringIO()
    for system, machine, results in results_by_platform(results):
        content.write(f"## {system} {machine}\n")
        if summarize:
            results = summarize_results(results)
        output_results_table(content, bases, results, filename)
        content.write("\n")
    _table.replace_section(filename, "table", content.getvalue())


def generate_tables(bases, results, repo_dir):
    generate_table(repo_dir / "README.md", bases, results, True)
    generate_table(repo_dir / "results" / "README.md", bases, results, False)


def link_to_hash(hash, fork):
    return _table.md_link(
        hash,
        f"https://github.com/{fork}/cpython/commit/{hash}",
    )


def generate_directory_indices(results_dir):
    """
    Generate the indices that go in each results directory.
    """
    for path in results_dir.iterdir():
        if not path.is_dir():
            continue
        results = []
        for filename in path.iterdir():
            if filename.name == "README.md":
                continue
            results.append(_result.Result.from_filename(filename))
        if not len(results):
            continue
        for result in results:
            if result.suffix == ".json":
                break
        else:
            raise ValueError(f"Couldn't find raw results in {path}")
        with open(path / "README.md", "w") as fd:
            fd.write("# Results\n\n")

            entries = [
                ("fork", result.fork),
                ("ref", result.ref),
                ("commit hash", link_to_hash(result.cpython_hash, result.fork)),
                ("commit date", result.commit_datetime),
                (
                    "commit merge base",
                    link_to_hash(result.commit_merge_base, result.fork),
                ),
            ]

            for key, val in entries:
                fd.write(f"- {key}: {val}\n")
            fd.write("\n")

            for system, machine, results in results_by_platform(results):
                results = sorted(results, key=lambda x: (x.extra, x.suffix))
                fd.write(f"## {system} {machine}\n\n")
                for result in results:
                    if result.suffix == ".json":
                        fd.write(
                            f"- {_table.md_link('raw results', result.filename.name)}\n"
                        )
                    elif result.suffix in (".md", ".png"):
                        if result.suffix == ".md":
                            filetype = "table"
                        else:
                            filetype = "plot"
                        link = _table.md_link(
                            f"{filetype} vs. {result.extra[-1]}", result.filename.name
                        )
                        fd.write(f"- {link}\n")
                fd.write("\n")


def main(repo_dir, force=False):
    results_dir = repo_dir / "results"
    bases = _bases.get_bases()
    print(f"Comparing to bases {bases}")
    results = _result.load_all_results(bases, results_dir)
    print(f"Found {len(results)} results")
    print("Generating comparison tables")
    save_generated_results(results, force=force)
    print("Generating indices")
    generate_tables(bases, results, repo_dir)
    generate_directory_indices(repo_dir / "results")


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
