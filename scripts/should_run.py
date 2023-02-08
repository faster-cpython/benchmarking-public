# Determines if this should run.
# If force is `true`, we always run, otherwise, we only run if we don't have
# results.

import argparse
from pathlib import Path
import subprocess
import sys


sys.path.insert(0, str(Path(__file__).parent))


from lib import git


def main(
    force: bool,
    fork: str,
    ref: str,
    cpython: Path = Path("cpython"),
    results: Path = Path("results"),
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

    entry = None
    for entry in results.iterdir():
        parts = entry.name.split("-")
        if commit_hash.startswith(parts[-1]):
            has_result = True
            break
    else:
        has_result = False

    if force:
        if has_result and entry is not None:
            for filepath in entry.iterdir():
                if filepath.suffix != ".json":
                    git.remove(results.parent, filepath)
        should_run = True
    else:
        should_run = not has_result

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
    args = parser.parse_args()

    force = sys.argv[-1] != "false"

    main(force, args.fork, args.ref)
