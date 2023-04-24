import argparse
import datetime
from pathlib import Path
import sys
from typing import Iterable, List, Optional, Sequence, TypeAlias


sys.path.insert(0, str(Path(__file__).parent))


from lib import gh
from lib import git
from lib import result as mod_result
from lib import runners


DEFAULTS = (["v3.11"], ["v3.10"], ["2022-11-20"], [])


RunnerType: TypeAlias = runners.Runner


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
        self.runners: List[RunnerType] = []


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


def get_bisect(cpython: Path, refs: Sequence[str]) -> Iterable[Commit]:
    if len(refs) != 2:
        raise ValueError(f"Each --bisect entry must contain 2 refs, got {len(refs)}")

    yield Commit(
        cpython,
        git.bisect_commits(cpython, refs[0], refs[1]),
        f"--bisect {refs[0]} {refs[1]}",
    )


def match_machine(a, b):
    return (
        (a == "amd64" and b == "x86_64") or (a == "x86_64" and b == "amd64") or (a == b)
    )


def remove_existing(
    force: bool,
    commits: Iterable[Commit],
    runners: Sequence[RunnerType],
    results: Optional[Sequence[mod_result.Result]] = None,
) -> Iterable[Commit]:
    """
    Remove any runner/commit combinations that we already have results for.
    If force is True, all runner/commit combinations will be generated.
    """
    if force:
        for commit in commits:
            commit.runners = list(runners)
            yield commit
        return

    if results is None:
        results = mod_result.load_all_results(None, Path("results"), sorted=False)

    for commit in commits:
        commit.runners = []
        for runner in runners:
            for result in results:
                if result.nickname == runner.nickname and commit.hash.startswith(
                    result.cpython_hash
                ):
                    break
            else:
                commit.runners.append(runner)

        if len(commit.runners):
            yield commit


def get_commits(
    cpython: Path,
    tags: Iterable[str],
    all_with_prefix: Iterable[str],
    latest_with_prefix: Iterable[str],
    weekly_since: Iterable[str],
    bisect: Iterable[Sequence[str]],
) -> Iterable[Commit]:
    for entry in all_with_prefix:
        yield from get_all_with_prefix(cpython, tags, entry)

    for entry in latest_with_prefix:
        yield from get_latest_with_prefix(cpython, tags, entry)

    for entry in weekly_since:
        yield from get_weekly_since(cpython, entry)

    for entry in bisect:
        yield from get_bisect(cpython, entry)


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


def format_runners(
    active_runners: Sequence[RunnerType], all_runners: Sequence[RunnerType]
):
    result = []
    for runner in all_runners:
        if runner in active_runners:
            result.append("X")
        else:
            result.append("-")
    return "".join(result)


def main(
    cpython: Path,
    all_with_prefix: Optional[Sequence[str]],
    latest_with_prefix: Optional[Sequence[str]],
    weekly_since: Optional[Sequence[str]],
    bisect: Optional[Sequence[Sequence[str]]],
    runners: Sequence[RunnerType],
    force: bool,
    all_runners: Sequence[RunnerType],
) -> None:
    all_with_prefix = all_with_prefix or []
    latest_with_prefix = latest_with_prefix or []
    weekly_since = weekly_since or []
    bisect = bisect or []

    if (
        all_with_prefix == []
        and latest_with_prefix == []
        and weekly_since == []
        and bisect == []
    ):
        all_with_prefix, latest_with_prefix, weekly_since, bisect = DEFAULTS

    tags = git.get_tags(cpython)

    commits = get_commits(
        cpython, tags, all_with_prefix, latest_with_prefix, weekly_since, bisect
    )

    commits = deduplicate_commits(cpython, commits)
    commits = remove_existing(force, commits, runners)

    commits = sorted(commits, key=lambda x: x.date)

    print(f"runners: {', '.join(x.nickname for x in runners)}")
    print()
    print(f"{'date':10s} {'hash':7s} {'ref':15s} {'#' * len(runners)} source")
    runs = 0
    for commit in commits:
        print(
            f"{str(commit.date)[:10]} {commit.hash[:7]:7s} "
            f"{commit.ref[:15]:15s} {format_runners(commit.runners, runners)} "
            f"{commit.source}"
        )
        runs += len(commit.runners)

    print()
    print(f"Selected {len(commits)} commits, {runs} runs.")
    choice = input("Are you sure you want to run them all? [y/N]")

    if choice.lower() in ("y", "yes"):
        for commit in commits:
            if len(commit.runners) == len(all_runners):
                gh.benchmark(ref=commit.hash, machine="all")
            else:
                for runner in commit.runners:
                    gh.benchmark(ref=commit.hash, machine=runner.name)


if __name__ == "__main__":
    all_runners = [x for x in runners.get_runners() if x.available]
    runners_by_names = {x.nickname: x for x in all_runners}

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
        action="append",
        help="Add all tags with the given version prefix, e.g. v3.11",
    )
    parser.add_argument(
        "--latest-with-prefix",
        action="append",
        help="Add the latest tag with the given version prefix, e.g. v3.10",
    )
    parser.add_argument(
        "--weekly-since",
        action="append",
        help="Select one commit per week since the given iso date, e.g. 2022-09-01",
    )
    parser.add_argument(
        "--bisect",
        nargs=2,
        action="append",
        help="Select the commit between the two given refs",
    )
    parser.add_argument(
        "--machine",
        choices=list(runners_by_names.keys()) + ["all"],
        default=all_runners[0].nickname,
        help="The machine to run on.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-run benchmark, even if we already have results for that commit hash.",
    )
    parser.add_argument("cpython", type=Path, help="The path to a checkout of CPython")

    args = parser.parse_args()

    if args.machine != "all":
        runners = [runners_by_names[args.machine]]
    else:
        runners = all_runners

    main(
        args.cpython,
        args.all_with_prefix,
        args.latest_with_prefix,
        args.weekly_since,
        args.bisect,
        runners,
        args.force,
        all_runners,
    )
