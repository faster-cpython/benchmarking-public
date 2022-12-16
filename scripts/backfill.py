import argparse
import datetime
from pathlib import Path
import sys


sys.path.insert(0, str(Path(__file__).parent))


from lib import _gh
from lib import _git
from lib import _result


DEFAULTS = (["v3.11"], ["v3.10"], ["2022-09-01"])


class Commit:
    def __init__(self, cpython, ref, source):
        self.ref = ref
        hash, date = _git.get_log("%H %cI", cpython, ref).split()
        self.hash = hash
        self.date = datetime.datetime.fromisoformat(date)
        self.source = source


def get_all_with_prefix(cpython, tags, entry):
    for tag in tags:
        if tag.startswith(entry):
            yield Commit(cpython, tag, f"--all-with-prefix {entry}")


def get_latest_with_prefix(cpython, tags, entry):
    commits = []
    for tag in tags:
        if tag.startswith(entry):
            commits.append(Commit(cpython, tag, f"--latest-with-prefix {entry}"))

    commits.sort(key=lambda x: x.date)
    yield commits[-1]


def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


def get_weekly_since(cpython, entry):
    start_date = datetime.datetime.fromisoformat(entry).replace(
        tzinfo=datetime.timezone.utc
    )
    today = datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)

    commits = _git.get_log(
        "%cI %h", cpython, n=None, extra=[f"--since={entry}"]
    ).splitlines()
    commits.sort()
    commits = [x.split() for x in commits]
    commits = [(datetime.datetime.fromisoformat(x), y) for x, y in commits]

    current_date = next_weekday(start_date, 7)
    while current_date < today and len(commits):
        while len(commits):
            commit_date, ref = commits.pop(0)
            if commit_date > current_date:
                yield Commit(cpython, ref, f"--weekly-since {entry}")
                current_date = next_weekday(current_date, 7)
                break


def remove_existing(commits):
    results = _result.load_all_results([], Path("results"))
    has_commits = [result.cpython_hash for result in results]
    commits = [
        commit
        for commit in commits
        if not any(commit.hash.startswith(hash) for hash in has_commits)
    ]
    return commits


def main(cpython, all_with_prefix, latest_with_prefix, weekly_since, machine, force):
    all_with_prefix = all_with_prefix or []
    latest_with_prefix = latest_with_prefix or []
    weekly_since = weekly_since or []

    if all_with_prefix == [] and latest_with_prefix == [] and weekly_since == []:
        all_with_prefix, latest_with_prefix, weekly_since = DEFAULTS

    commits = []
    tags = _git.get_tags(cpython)

    for entry in all_with_prefix:
        commits.extend(get_all_with_prefix(cpython, tags, entry))

    for entry in latest_with_prefix:
        commits.extend(get_latest_with_prefix(cpython, tags, entry))

    for entry in weekly_since:
        commits.extend(get_weekly_since(cpython, entry))

    if not force:
        commits = remove_existing(commits)

    commits.sort(key=lambda x: x.date)

    print(f"{'date':10s} {'hash':7s} {'ref':15s} source")
    for commit in commits:
        print(
            f"{str(commit.date)[:10]} {commit.hash[:7]:7s} "
            f"{commit.ref[:15]:15s} {commit.source}"
        )

    print()
    print(f"Selected {len(commits)} commits.")
    choice = input("Are you sure you want to run them all? [y/N]")

    if choice.lower() in ("y", "yes"):
        for commit in commits:
            _gh.benchmark(ref=commit.hash, machine=machine, publish=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        """
        Fire off a set of benchmark jobs based on tags in the cpython
        repository. Useful for regenerating or catching up with old data. The
        set of tags to run will be displayed for confirmation before actually
        setting up the jobs.

        If no named arguments are provided, a set of defaults will be used.
        """
    )
    parser.add_argument(
        "--all-with-prefix",
        nargs="*",
        action="extend",
        help="Add all tags with the given version prefix, e.g. v3.11",
    )
    parser.add_argument(
        "--latest-with-prefix",
        nargs="*",
        action="extend",
        help="Add the latest tag with the given version prefix, e.g. v3.10",
    )
    parser.add_argument(
        "--weekly-since",
        nargs="?",
        help="Select one commit per week since the given iso date, e.g. 2022-09-01",
    )
    parser.add_argument(
        "--machine", default="linux-amd64", help="The machine to run on."
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-run benchmark, even if we already have results for that commit hash.",
    ),
    parser.add_argument("cpython", help="The path to a checkout of CPython")

    args = parser.parse_args()

    main(
        args.cpython,
        args.all_with_prefix,
        args.latest_with_prefix,
        args.weekly_since,
        args.machine,
        args.force,
    )
