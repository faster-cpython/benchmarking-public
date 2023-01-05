import json
from pathlib import Path
import platform
import shutil
import sys


from scripts.lib import result as mod_result


DATA_PATH = Path(__file__).parent / "data"


def _copy_results(tmp_path):
    results_path = tmp_path / "results"
    shutil.copytree(DATA_PATH / "results", tmp_path / "results")
    return results_path


def test_load_all_results(tmp_path):
    results_path = _copy_results(tmp_path)

    results = mod_result.load_all_results(["3.10.4", "3.11.0b3"], results_path)

    assert len(results) == 16

    by_version = {x.version: x for x in results}

    result_310 = by_version["3.10.4"]

    for result in results:
        if result is not result_310:
            comparison = result.bases["3.10.4"]
            assert comparison.ref is result_310
            assert comparison.head is result
            assert comparison.base == "3.10.4"

    assert result_310.commit_datetime == "2022-03-23T20:12:04+00:00"
    assert result_310.commit_date == "2022-03-23"
    assert result_310.commit_merge_base is None
    assert result_310.benchmark_hash == "aea5ad"


def test_merge_base(tmp_path):
    results_path = _copy_results(tmp_path)

    # Hack up so one of the results has an explicit commit_merge_base
    result_with_base = (
        results_path
        / "bm-20221119-3.12.0a3+-b0e1f9c"
        / "bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c.json"
    )
    with open(result_with_base) as fd:
        contents = json.load(fd)
    contents["metadata"][
        "commit_merge_base"
    ] = "9d38120e335357a3b294277fd5eff0a10e46e043"
    with open(result_with_base, "w") as fd:
        json.dump(contents, fd)
    # End hack

    results = mod_result.load_all_results([], results_path)

    by_hash = {x.cpython_hash: x for x in results}

    head = by_hash["b0e1f9c"]
    comparison = head.bases["base"]

    assert head.commit_merge_base == "9d38120e335357a3b294277fd5eff0a10e46e043"
    assert comparison.ref.version == "3.10.4"
    assert comparison.head is head
    assert comparison.geometric_mean == "1.70x faster \\*"


def test_from_scratch(monkeypatch):
    python = sys.executable

    def get_git_hash(*args):
        return "b7e4f1d97c6e784d2dee182d2b81541ddcff5751"

    monkeypatch.setattr(mod_result.git, "get_git_hash", get_git_hash)

    def get_git_commit_date(*args):
        return "2022-11-19T20:47:09+00:00"

    monkeypatch.setattr(mod_result.git, "get_git_commit_date", get_git_commit_date)

    result = mod_result.Result.from_scratch(
        python, "my-fork", "9d38120e335357a3b294277fd5eff0a10e46e043"
    )

    assert result.filename == Path(
        f"results/bm-20221119-{platform.python_version()}-b7e4f1d/"
        f"bm-20221119-{platform.system().lower()}-{platform.machine().lower()}"
        f"-my_fork-9d38120e335357a3b294-{platform.python_version()}-b7e4f1d.json"
    )
