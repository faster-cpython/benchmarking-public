import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys


import pytest


from scripts import run_benchmarks


DATA_PATH = Path(__file__).parent / "data"


def test_update_metadata(tmp_path):
    subprocess.check_call(
        [
            "git",
            "clone",
            "https://github.com/python/cpython",
            "--depth",
            "1",
            "--branch",
            "v3.10.4",
        ],
        cwd=tmp_path,
    )
    shutil.copy(
        DATA_PATH
        / "results"
        / "bm-20211208-3.11.0a3-2e91dba"
        / "bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba.json",
        tmp_path / "benchmarks.json",
    )
    run_benchmarks.update_metadata(
        tmp_path / "benchmarks.json", "myfork", "myref", "false", tmp_path / "cpython"
    )

    with open(tmp_path / "benchmarks.json") as fd:
        content = json.load(fd)

    metadata = content["metadata"]

    assert metadata["commit_id"] == "9d38120"
    assert metadata["commit_fork"] == "myfork"
    assert metadata["commit_branch"] == "myref"
    assert metadata["commit_date"] == "2022-03-23T20:12:04+00:00"
    assert "commit_merge_base" not in metadata
    assert metadata["benchmark_hash"] == "e3b0c4"
    assert not metadata.get("publish")


def test_run_benchmarks(tmp_path):
    # This is mainly recreating the first few steps in _benchmark.yml, except
    # for compiling Python from scratch
    subprocess.check_call(
        [
            "git",
            "clone",
            "https://github.com/python/cpython",
            "--depth",
            "1",
            "--branch",
            "v3.10.4",
        ],
        cwd=tmp_path,
    )
    subprocess.check_call(
        [
            "git",
            "clone",
            "https://github.com/pyston/python-macrobenchmarks",
            "--depth",
            "1",
            "pyston-benchmarks",
        ],
        cwd=tmp_path,
    )
    subprocess.check_call(
        [
            "git",
            "clone",
            "https://github.com/mdboom/pyperformance",
            "--depth",
            "1",
            "--branch",
            "fix-manifest-parsing",
        ],
        cwd=tmp_path,
    )

    venv_dir = tmp_path / "venv"
    venv_python = venv_dir / "bin" / "python"

    subprocess.check_call([sys.executable, "-m", "venv", venv_dir], cwd=tmp_path)
    subprocess.check_call(
        [venv_python, "-m", "pip", "install", "setuptools", "wheel"], cwd=tmp_path
    )
    subprocess.check_call(
        [venv_python, "-m", "pip", "install", tmp_path / "pyperformance"], cwd=tmp_path
    )

    shutil.copy(
        Path(__file__).parents[1] / "benchmarks.manifest",
        tmp_path / "benchmarks.manifest",
    )

    # Now actually run the run_benchmarks.py script
    subprocess.check_call(
        [
            venv_python,
            run_benchmarks.__file__,
            "benchmark",
            sys.executable,
            "python",
            "main",
            "deepcopy",
            "false",
        ],
        cwd=tmp_path,
    )

    with open(
        tmp_path
        / "results"
        / f"bm-20220323-{platform.python_version()}-9d38120"
        / f"bm-20220323-{platform.system().lower()}-{platform.machine()}-"
        f"python-main-{platform.python_version()}-9d38120.json"
    ) as fd:
        content = json.load(fd)

    metadata = content["metadata"]
    benchmarks = content["benchmarks"]

    assert metadata["commit_id"] == "9d38120"
    assert metadata["commit_fork"] == "python"
    assert metadata["commit_branch"] == "main"
    assert metadata["commit_date"] == "2022-03-23T20:12:04+00:00"
    assert "commit_merge_base" not in metadata
    assert metadata["benchmark_hash"] == "9d2e5f"
    assert not metadata.get("publish")

    assert len(benchmarks) == 3
    assert all(len(benchmark["runs"]) > 1 for benchmark in benchmarks)
    assert set(bm["metadata"]["name"] for bm in benchmarks) == {
        "deepcopy",
        "deepcopy_memo",
        "deepcopy_reduce",
    }

    # Run an unknown benchmark, expect an error
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.check_call(
            [
                venv_python,
                run_benchmarks.__file__,
                "benchmark",
                sys.executable,
                "python",
                "main",
                "foo",
                "false",
            ],
            cwd=tmp_path,
        )
