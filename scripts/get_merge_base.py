from pathlib import Path
import sys


sys.path.insert(0, str(Path(__file__).parent))


from lib import git
from lib.result import has_result


def main(need_to_run: bool, machine: str, cpython: Path = Path("cpython")) -> None:
    if not need_to_run:
        print("ref=xxxxxxx")
        print("need_to_run=false")
    else:
        merge_base = git.get_git_merge_base(cpython)

        if merge_base is None:
            print("ref=xxxxxxx")
            print("need_to_run=false")
        else:
            need_to_run = (
                machine == "all"
                or has_result(Path("results"), merge_base, machine) is None
            )

            print(f"ref={merge_base}")
            print(f"need_to_run={str(need_to_run).lower()}")


if __name__ == "__main__":
    need_to_run = sys.argv[-2] != "false"

    main(need_to_run, sys.argv[-1])
