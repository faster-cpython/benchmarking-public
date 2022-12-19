"""
Handling the list of base versions defined in bases.txt.
"""

from pathlib import Path
from typing import List


def get_bases(
    bases_filepath: Path = Path(__file__).parents[2] / "bases.txt",
) -> List[str]:
    with open(bases_filepath) as fd:
        return list(
            line.strip() for line in fd.readlines() if line and not line.startswith("#")
        )
