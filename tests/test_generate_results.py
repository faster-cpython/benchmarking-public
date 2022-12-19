import collections
import json
from pathlib import Path
import shutil


from scripts import generate_results


DATA_PATH = Path(__file__).parent / "data"


def _copy_repo(tmp_path):
    repo_path = tmp_path / "repo"
    shutil.copytree(DATA_PATH, tmp_path / "repo")
    return repo_path


def test_main(tmp_path):
    repo_path = _copy_repo(tmp_path)
    results_path = repo_path / "results"

    # Hack up so one of the results has an explicit commit_merge_base
    result_with_base = (
        results_path
        / "bm-20221119-python-main-3.12.0a3+-b0e1f9c"
        / "bm-20221119-linux-amd64-python-main-3.12.0a3+-b0e1f9c.json"
    )
    with open(result_with_base) as fd:
        contents = json.load(fd)
    contents["metadata"][
        "commit_merge_base"
    ] = "9d38120e335357a3b294277fd5eff0a10e46e043"
    with open(result_with_base, "w") as fd:
        json.dump(contents, fd)
    # End hack

    generate_results.main(repo_path)

    for dirpath in results_path.iterdir():
        if not dirpath.is_dir():
            continue

        files_by_type = collections.Counter()
        for filepath in dirpath.iterdir():
            files_by_type[filepath.suffix] += 1
        assert files_by_type[".json"] == 1

        if "b0e1f9c" in dirpath.name:
            assert files_by_type[".md"] == 4
            assert files_by_type[".png"] == 3
        elif "3.10.4" in dirpath.name or "3.11.0b3" in dirpath.name:
            assert files_by_type[".md"] == 2
            assert files_by_type[".png"] == 1
        else:
            assert files_by_type[".md"] == 3
            assert files_by_type[".png"] == 2

        # Make sure all files in the directory have a link
        contents = (dirpath / "README.md").read_text()
        assert contents.count("\n- [") == len(list(dirpath.iterdir())) - 1

    contents = (repo_path / "README.md").read_text()
    assert contents.count("\n|") == 14

    contents = (repo_path / "results" / "README.md").read_text()
    assert contents.count("\n|") == 18
