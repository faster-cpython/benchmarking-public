"""
Handling the list of base versions defined in bases.txt.
"""

from pathlib import Path


def get_bases(bases_filepath=Path(__file__).parents[2] / "bases.txt"):
    with open(bases_filepath) as fd:
        return list(
            line.strip() for line in fd.readlines() if line and not line.startswith("#")
        )
