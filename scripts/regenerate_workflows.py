"""
Regenerates some Github Actions workflow files from templates.
"""

import argparse
import copy
import io
from pathlib import Path
import sys
from typing import Any, List


from ruamel.yaml import YAML


sys.path.insert(0, str(Path(__file__).parent))


from lib import runners


ROOT_PATH = Path(__file__).parents[1]
TEMPLATE_PATH = Path(__file__).parent / "templates"
WORKFLOW_PATH = Path(__file__).parents[1] / ".github" / "workflows"


def write_yaml(dst: Path, contents: Any, check: bool):
    """
    Write `contents` to `dst` as YAML.

    If `check` is True, raise SystemExit if the file would change. This is used
    in CI to confirm that the file was regenerated after changes to the source
    file.
    """

    def do_write(contents, fd):
        fd.write("# Generated file: !!! DO NOT EDIT !!!\n")
        fd.write("---\n")
        yaml = YAML()
        yaml.dump(contents, fd)

    if check:
        with open(dst) as fd:
            orig_contents = fd.read()
        fd = io.StringIO()
        do_write(contents, fd)
        new_contents = fd.getvalue()
        if orig_contents != new_contents:
            print(f"{dst.relative_to(ROOT_PATH)} needs to be regenerated.")
            print("Run scripts/regenerate_workflows.py and commit the result.")
            sys.exit(1)
    else:
        with open(dst, "w") as fd:
            do_write(contents, fd)


def load_yaml(src: Path) -> Any:
    """
    Load YAML from `src`.
    """
    with open(src) as fd:
        yaml = YAML()
        return yaml.load(fd)


def generate__benchmark(
    runners: List[runners.Runner], runner_choices: List[str], check: bool
) -> None:
    """
    Generates _benchmark.yml from _benchmark.src.yml.

    For each runner machine, inserts the platform-specific set of steps for
    that machine.

    Inserts the list of available machines to the drop-down presented to the
    user.
    """
    src = load_yaml(TEMPLATE_PATH / "_benchmark.src.yml")
    dst = copy.deepcopy(src)

    dst["jobs"] = {}
    for runner in runners:
        runner_template = copy.deepcopy(src["jobs"][f"benchmark-{runner.os}"])
        runner_template["runs-on"].append(f"hostname:{runner.hostname}")
        runner_template[
            "if"
        ] = f"${{{{ (inputs.machine == '{runner.name}' || inputs.machine == 'all') }}}}"
        dst["jobs"][f"benchmark-{runner.os}-{runner.hostname}"] = runner_template

    dst["on"]["workflow_dispatch"]["inputs"]["machine"]["options"] = runner_choices

    write_yaml(WORKFLOW_PATH / "_benchmark.yml", dst, check)


def generate_benchmark(runner_choices: List[str], check: bool) -> None:
    """
    Generates benchmark.yml from benchmark.src.yml.

    Inserts the list of available machines to the drop-down presented to the
    user.
    """
    src = load_yaml(TEMPLATE_PATH / "benchmark.src.yml")
    src["on"]["workflow_dispatch"]["inputs"]["machine"]["options"] = runner_choices
    write_yaml(WORKFLOW_PATH / "benchmark.yml", src, check)


def main(check: bool) -> None:
    available_runners = [r for r in runners.get_runners() if r.available]
    runner_choices = [x.name for x in available_runners] + ["all"]

    generate__benchmark(available_runners, runner_choices, check)
    generate_benchmark(runner_choices, check)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Regenerate Github Actions workflow files from the templates"
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check whether any files need regeneration",
    )
    args = parser.parse_args()

    main(args.check)
