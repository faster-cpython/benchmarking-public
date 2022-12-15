"""
Handling the list of base versions defined in bases.txt.
"""

from pathlib import Path


def get_bases():
    with open(Path(__file__).parents[2] / "bases.txt") as fd:
        bases = list(
            line.strip() for line in fd.readlines() if line and not line.startswith("#")
        )
    return bases
