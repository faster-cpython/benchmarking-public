# Generated file: !!! DO NOT EDIT !!!

# This script may only use the standard library, since it bootstraps setting up
# the virtual environment to run the full bench_runner.


# NOTE: This file should import in Python 3.9 or later so it can at least print
# the error message that the version of Python is too old.


from pathlib import Path
import shutil
import subprocess
import sys


def create_venv(venv: Path) -> None:
    if venv.exists():
        shutil.rmtree(venv)

    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "venv",
            str(venv),
        ]
    )


def run_in_venv(
    venv: Path, module: str, cmd: list[str], prefix: list[str] = []
) -> None:
    venv = Path(venv)

    if sys.platform.startswith("win"):
        exe = Path("Scripts") / "python.exe"
    else:
        exe = Path("bin") / "python"

    args = [
        *prefix,
        str(venv / exe),
        "-m",
        module,
        *cmd,
    ]

    print("Running command:", " ".join(args))
    subprocess.check_call(args)


def install_requirements(venv: Path) -> None:
    run_in_venv(venv, "pip", ["install", "--upgrade", "pip"])
    run_in_venv(venv, "pip", ["install", "-r", "requirements.txt"])

    # To facilitate coverage testing
    if "--_fast" in sys.argv:
        run_in_venv(venv, "pip", ["install", "pytest-cov"])


def main():
    venv = Path("venv")
    print("::group::Creating venv", file=sys.stderr)
    create_venv(venv)
    print("::endgroup::", file=sys.stderr)
    print("::group::Installing requirements", file=sys.stderr)
    install_requirements(venv)
    print("::endgroup::", file=sys.stderr)

    # Now that we've installed the full bench_runner library,
    # continue on in a new process...

    last_arg = sys.argv.index("workflow_bootstrap.py")
    if last_arg == -1:
        raise ValueError("Couldn't parse command line")

    run_in_venv(venv, "bench_runner", ["workflow", *sys.argv[last_arg + 1 :]])


if __name__ == "__main__":
    if sys.version_info[:2] < (3, 11):
        print(
            "The benchmarking infrastructure requires Python 3.11 or later.",
            file=sys.stderr,
        )
        sys.exit(1)

    main()
