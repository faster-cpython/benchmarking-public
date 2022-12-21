import json
from pathlib import Path
import shutil
import subprocess


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

    print(metadata)

    assert metadata["commit_id"] == "9d38120"
    assert metadata["commit_fork"] == "myfork"
    assert metadata["commit_branch"] == "myref"
    assert metadata["commit_date"] == "2022-03-23T20:12:04+00:00"
    assert "commit_merge_base" not in metadata
    assert metadata["benchmark_hash"] == "e3b0c4"
    assert not metadata.get("publish")
