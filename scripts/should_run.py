# Determines if this should run.
# If force is `true`, we always run, otherwise, we only run if we don't have
# results.

import argparse
from pathlib import Path
import subprocess
import sys


sys.path.insert(0, str(Path(__file__).parent))


from lib import git
from lib.result import has_result


def main(
    force: bool,
    fork: str,
    ref: str,
    machine: str,
    cpython: Path = Path("cpython"),
    results_dir: Path = Path("results"),
) -> None:
    try:
        commit_hash = git.get_git_hash(cpython)
    except subprocess.CalledProcessError:
        # This will fail if the cpython checkout failed for some reason. Print
        # a nice error message since the one the checkout itself gives is
        # totally inscrutable.
        print("The checkout of cpython failed.")
        print(f"You specified fork {fork!r} and ref {ref!r}.")
        print("Are you sure you entered the fork and ref correctly?")
        # Fail the rest of the workflow
        sys.exit(1)

    found_result = has_result(results_dir, commit_hash, machine)

    if force:
        if found_result is not None:
            for filepath in found_result.filename.parent.iterdir():
                if filepath.suffix != ".json":
                    git.remove(results_dir.parent, filepath)
        should_run = True
    else:
        should_run = machine == "all" or found_result is None

    print(f"should_run={str(should_run).lower()}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Generate master index tables and comparison plots for all of the results.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "force",
        help="If true, force a re-run",
    )
    parser.add_argument("fork")
    parser.add_argument("ref")
    parser.add_argument("machine")
    args = parser.parse_args()

    force = args.force != "false"

    main(force, args.fork, args.ref, args.machine)
