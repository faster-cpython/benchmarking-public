import argparse
import json
from pathlib import Path
import shutil


def copy(srcfile: Path, src: Path, dst: Path) -> None:
    dstfile = dst / srcfile.relative_to(src)
    dstfile.parent.mkdir(parents=True, exist_ok=True)
    print(f"Copying {srcfile.resolve()} to {dstfile.resolve()}")
    shutil.copyfile(srcfile, dstfile)


def main(src: Path, dst: Path) -> None:
    for srcfile in Path(src).glob("**/*.json"):
        with open(srcfile) as fd:
            contents = json.load(fd)
        if contents.get("metadata", {}).get("publish"):
            copy(srcfile, src, dst)

            # pystats have a companion markdown file
            if srcfile.name.endswith("-pystats.json"):
                copy(
                    Path(str(srcfile).replace("-pystats.json", "-pystats.md")), src, dst
                )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Copies .json files flagged as 'publish' from a source dir to a dest dir."
    )
    parser.add_argument("src", type=Path)
    parser.add_argument("dst", type=Path)

    args = parser.parse_args()

    main(args.src, args.dst)
