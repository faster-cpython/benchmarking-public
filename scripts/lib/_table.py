"""
Utilities to generate markdown tables.
"""


from pathlib import Path


def output_table(fd, head, rows):
    """
    Output a table in markdown format.
    """

    def output_row(row):
        fd.write(f'| {" | ".join(row)} |\n')

    output_row(head)
    output_row([col.endswith(":") and "---:" or "---" for col in head])
    for row in rows:
        output_row(row)


def replace_section(filename, name, content):
    """
    Replace a table in a markdown file with the new content.

    The section is defined with the delimiters:

    ```
    <!-- START {name} -->
    ... content goes here ...
    <!-- END {name} -->
    ```
    """
    lines = iter(filename.read_text().splitlines())

    with filename.open("w") as fd:
        while True:
            try:
                line = next(lines)
            except StopIteration:
                break

            if line == f"<!-- START {name} -->":
                fd.write(line + "\n")
                fd.write(content)
                fd.write("\n")

                while True:
                    line = next(lines)
                    if line == f"<!-- END {name} -->":
                        fd.write(line + "\n")
                        break
            else:
                fd.write(line + "\n")


def md_link(text, link, root=None):
    """
    Formats a Markdown link. The link is resolved relative to the given root.
    """
    if root is not None:
        link = Path(link).resolve().relative_to(Path(root).parent.resolve())
    return f"[{text}]({link})"


def link_to_hash(hash, fork):
    """
    Create a markdown link to a specific hash of a specific fork on GitHub.
    """
    return md_link(
        hash,
        f"https://github.com/{fork}/cpython/commit/{hash}",
    )
