from pathlib import Path

import pytest

from check_reqs.check_reqs import _process_file

THIS_DIR = Path(__file__).resolve().parent
INPUT_FILES = (THIS_DIR / "data").glob("*.txt")


@pytest.mark.parametrize("input_file", INPUT_FILES)
def test_parse(input_file):
    _process_file(input_file)
