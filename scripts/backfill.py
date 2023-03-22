import argparse
import datetime
from pathlib import Path
import sys
from typing import Iterable, Optional, Sequence


sys.path.insert(0, str(Path(__file__).parent))


from lib import gh
from lib import git
from lib import result as mod_result


DEFAULTS = (["v3.11"], ["v3.10"], ["2022-11-20"])


class Commit:
    """
    Represents a single commit to possibly benchmark.
    """

    def __init__(self, cpython: Path, ref: str, source: str):
        self.ref = ref
        hash, date = git.get_log("%H %cI", cpython, ref).split()
        self.hash = hash
        self.date = datetime.datetime.fromisoformat(date)
        self.source = source


def get_all_with_prefix(
    cpython: Path, tags: Iterable[str], prefix: str
) -> Iterable[Commit]:
    """
    Get all tags with the given prefix.
    """
    for tag in tags:
        if tag.startswith(prefix):
            yield Commit(cpython, tag, f"--all-with-prefix {prefix}")


def get_latest_with_prefix(
    cpython: Path, tags: Iterable[str], prefix: str
) -> Iterable[Commit]:
    """
    Get the most recent (by commit date) tag with the given prefix.
    """
    commits = []
    for tag in tags:
        if tag.startswith(prefix):
            commits.append(Commit(cpython, tag, f"--latest-with-prefix {prefix}"))

    commits.sort(key=lambda x: x.date)
    yield commits[-1]


def next_weekday(d: datetime.datetime, weekday: int) -> datetime.datetime:
    """
    Given datetime `d`, returns the next date on the given ISO weekday.
    """
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


def get_weekly_since(cpython: Path, start_date: str) -> Iterable[Commit]:
    """
    Get weekly commits on Sundays since the given start date.
    """
    start = datetime.datetime.fromisoformat(start_date).replace(
        tzinfo=datetime.timezone.utc
    )
    today = datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)

    commits = git.get_log(
        "%cI %h", cpython, n=0, extra=[f"--since={start_date}"]
    ).splitlines()
    commits.sort()
    commits = [x.split() for x in commits]
    commits = [(datetime.datetime.fromisoformat(x), y) for x, y in commits]

    current_date = next_weekday(start, 7)
    while current_date < today and len(commits):
        while len(commits):
            commit_date, ref = commits.pop(0)
            if commit_date > current_date:
                yield Commit(cpython, ref, f"--weekly-since {start_date}")
                current_date = next_weekday(current_date, 7)
                break


def match_machine(a, b):
    return (
        (a == "amd64" and b == "x86_64") or (a == "x86_64" and b == "amd64") or (a == b)
    )


def remove_existing(
    commits: Iterable[Commit], machine: str, results=None
) -> Iterable[Commit]:
    """
    Remove any commits that we already have results for the given machine.
    """
    if results is None:
        results = mod_result.load_all_results([], Path("results"))

    if machine == "all":
        all_commits = set()
        for submachine in gh.get_machines():
            if submachine == "all":
                continue
            all_commits |= set(remove_existing(commits, submachine, results))
        yield from all_commits
        return

    system, machine, nickname = machine.split("-")

    for commit in commits:
        for result in results:
            if (
                result.system == system
                and match_machine(result.machine, machine)
                and result.nickname == nickname
                and commit.hash.startswith(result.cpython_hash)
            ):
                break
        else:
            yield commit


def get_commits(
    cpython: Path,
    tags: Iterable[str],
    all_with_prefix: Iterable[str],
    latest_with_prefix: Iterable[str],
    weekly_since: Iterable[str],
) -> Iterable[Commit]:
    for entry in all_with_prefix:
        yield from get_all_with_prefix(cpython, tags, entry)

    for entry in latest_with_prefix:
        yield from get_latest_with_prefix(cpython, tags, entry)

    for entry in weekly_since:
        yield from get_weekly_since(cpython, entry)


def deduplicate_commits(cpython: Path, commits: Iterable[Commit]) -> Iterable[Commit]:
    commits_by_hash = {}

    for commit in commits:
        commits_by_hash.setdefault(commit.hash, []).append(commit)

    for commit_set in commits_by_hash.values():
        first_commit = commit_set[0]
        if len(commit_set) == 1:
            yield first_commit
        else:
            yield Commit(
                cpython, first_commit.ref, ", ".join(x.source for x in commit_set)
            )


def main(
    cpython: Path,
    all_with_prefix: Optional[Sequence[str]],
    latest_with_prefix: Optional[Sequence[str]],
    weekly_since: Optional[Sequence[str]],
    machine: str,
    force: bool,
) -> None:
    all_with_prefix = all_with_prefix or []
    latest_with_prefix = latest_with_prefix or []
    weekly_since = weekly_since or []

    if all_with_prefix == [] and latest_with_prefix == [] and weekly_since == []:
        all_with_prefix, latest_with_prefix, weekly_since = DEFAULTS

    tags = git.get_tags(cpython)

    commits = get_commits(
        cpython, tags, all_with_prefix, latest_with_prefix, weekly_since
    )

    if not force:
        commits = remove_existing(commits, machine)

    commits = deduplicate_commits(cpython, commits)

    commits = sorted(commits, key=lambda x: x.date)

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
            gh.benchmark(ref=commit.hash, machine=machine, publish=True)


if __name__ == "__main__":
    machines = gh.get_machines()

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
        "--machine",
        choices=machines,
        default=machines[0],
        help="The machine to run on.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-run benchmark, even if we already have results for that commit hash.",
    )
    parser.add_argument("cpython", type=Path, help="The path to a checkout of CPython")

    args = parser.parse_args()

    main(
        args.cpython,
        args.all_with_prefix,
        args.latest_with_prefix,
        args.weekly_since,
        args.machine,
        args.force,
    )
