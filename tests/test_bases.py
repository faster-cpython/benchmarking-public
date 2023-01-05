from pathlib import Path


from scripts.lib import bases as mod_bases


DATA_PATH = Path(__file__).parent / "data"


def test_get_bases():
    bases = mod_bases.get_bases(DATA_PATH / "bases.txt")
    assert bases == ["base2", "base4"]
