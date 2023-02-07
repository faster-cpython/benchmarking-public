# Determines if this should run.
# If force is `true`, we always run, otherwise, we only run if we don't have
# results.

from pathlib import Path
import subprocess
import sys


sys.path.insert(0, str(Path(__file__).parent))


from lib import git


def main(
    force: bool, cpython: Path = Path("cpython"), results: Path = Path("results")
) -> None:
    try:
        commit_hash = git.get_git_hash(cpython)
    except subprocess.CalledProcessError:
        # This will fail if the cpython checkout failed for some reason. Print
        # a nice error message since the one the checkout itself gives is
        # totally inscrutable.
        print(
            "The checkout of cpython failed. "
            "Are you sure you entered the fork and ref correctly?"
        )
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
            git.remove_dir(results.parent, entry)
        should_run = True
    else:
        should_run = not has_result

    print(f"should_run={str(should_run).lower()}")


if __name__ == "__main__":
    force = sys.argv[-1] != "false"

    main(force)
