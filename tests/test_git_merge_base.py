import subprocess
import textwrap


from scripts import get_merge_base


def test_get_merge_base(tmp_path, capsys):
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
        cwd=tmp_path,
    )

    get_merge_base.main(True, tmp_path / "cpython")

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
    get_merge_base.main(False)

    captured = capsys.readouterr()

    assert "need_to_run=false" in captured.out
