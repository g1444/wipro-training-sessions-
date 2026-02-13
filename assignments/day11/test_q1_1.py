import pytest

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (5, 5, 10),
    (1, 9, 10)
])
def test_addition(a, b, expected):
    assert a + b == expected
