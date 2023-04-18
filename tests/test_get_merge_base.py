import shutil
import subprocess
import textwrap


import pytest


from scripts import get_merge_base


@pytest.fixture
def checkout(request):
    root = request.config.cache.mkdir("get-merge-base-checkout")

    if not (root / "cpython").is_dir():
        subprocess.check_call(
            [
                "git",
                "clone",
                "https://github.com/mdboom/cpython",
                "--branch",
                "fix-pystats",
                "--depth",
                "50",
            ],
            cwd=root,
        )

    return root


def test_get_merge_base(tmp_path, capsys, checkout):
    shutil.copytree(checkout / "cpython", tmp_path / "cpython")

    get_merge_base.main(True, "linux-x86_64-linux", tmp_path / "cpython")

    captured = capsys.readouterr()

    assert (
        captured.out.strip()
        == textwrap.dedent(
            """
    ref=158b8a07212cea6066afe8bb91f1cd542d922dba
    need_to_run=true
    """
        ).strip()
    )


def test_hard_coded(capsys):
    get_merge_base.main(False, "linux-x86_64-linux")

    captured = capsys.readouterr()

    assert "need_to_run=false" in captured.out
