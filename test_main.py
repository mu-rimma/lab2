import pytest

from main import is_divisible_by

def data_for_testfun():
    return ((6, 2, True), (6, -1, True), (6, 5, False))

@pytest.mark.parametrize("x, y, res", data_for_testfun())   
def test_is_divisible_by(x, y, res):
    assert is_divisible_by(x, y) == res
