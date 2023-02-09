import io
from pathlib import Path
import shutil
import textwrap


from scripts.lib import table


DATA_PATH = Path(__file__).parent / "data"


def test_output_table():
    head = ["col1", "col2", "col3:"]
    rows = [["a", "b", "c"], ["d", "e", "f"]]

    fd = io.StringIO()
    table.output_table(fd, head, rows)

    assert (
        fd.getvalue().strip()
        == textwrap.dedent(
            """
        | col1 | col2 | col3: |
        | --- | --- | ---: |
        | a | b | c |
        | d | e | f |
        """
        ).strip()
    )


def test_replace_section(tmp_path):
    readme_path = tmp_path / "README.md"
    shutil.copy(DATA_PATH / "RESULTS.md", readme_path)

    table.replace_section(readme_path, "table", "THIS IS THE CONTENT")

    assert (
        readme_path.read_text().strip()
        == textwrap.dedent(
            """
        ## Content before

        <!-- START table -->
        THIS IS THE CONTENT
        <!-- END table -->

        ## Content after
        """
        ).strip()
    )


def test_md_link():
    assert table.md_link("text", "link") == "[text](link)"
    assert table.md_link("text", "relative/link", "relative/other") == "[text](link)"
    assert table.md_link("text", "relative/link", "other") == "[text](relative/link)"


def test_link_to_hash():
    assert (
        table.link_to_hash("MYHASH", "MYFORK")
        == "[MYHASH](https://github.com/MYFORK/cpython/commit/MYHASH)"
    )
