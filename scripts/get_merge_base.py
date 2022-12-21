from pathlib import Path
import sys


sys.path.insert(0, str(Path(__file__).parent))


from lib import _git


def main(need_to_run: bool, cpython: Path = Path("cpython")) -> None:
    if not need_to_run:
        print("ref=xxxxxxx")
        print("need_to_run=false")
    else:
        merge_base = _git.get_git_merge_base(cpython)

        need_to_run = True
        for entry in Path("results").iterdir():
            parts = entry.name.split("-")
            if merge_base.startswith(parts[-1]):
                need_to_run = False
                break

        print(f"ref={merge_base}")
        print(f"need_to_run={str(need_to_run).lower()}")


if __name__ == "__main__":
    need_to_run = sys.argv[-1] != "false"

    main(need_to_run)
