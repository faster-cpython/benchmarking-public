import json
from pathlib import Path
import shutil


from scripts import publish


DATA_PATH = Path(__file__).parent / "data"


def _copy_repo(tmp_path):
    repo_path = tmp_path / "repo"
    shutil.copytree(DATA_PATH, tmp_path / "repo")
    return repo_path


def test_publish(tmp_path):
    repo_path = _copy_repo(tmp_path)
    public_path = tmp_path / "public"

    public_path.mkdir()

    publish.main(repo_path, public_path)

    assert len(list((public_path / "results").iterdir())) == 14

    for filepath in (public_path / "results").glob("**/*.json"):
        with open(filepath) as fd:
            contents = json.load(fd)
        assert contents["metadata"]["publish"]


def test_publish2(tmp_path):
    repo_path = _copy_repo(tmp_path)

    # Hack -- remove the publish flag from one more
    for filepath in (repo_path / "results").glob("**/*.json"):
        with open(filepath) as fd:
            contents = json.load(fd)
        if contents["metadata"].get("publish"):
            del contents["metadata"]["publish"]
            with open(filepath, "w") as fd:
                json.dump(contents, fd)
            break
    # End Hack

    public_path = tmp_path / "public"

    public_path.mkdir()

    publish.main(repo_path, public_path)

    assert len(list((public_path / "results").iterdir())) == 13

    for filepath in (public_path / "results").glob("**/*.json"):
        with open(filepath) as fd:
            contents = json.load(fd)
        assert contents["metadata"]["publish"]
