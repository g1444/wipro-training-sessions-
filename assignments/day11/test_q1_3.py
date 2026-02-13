import pytest
@pytest.mark.slow
def test_slow_demo():
    assert "pytest".upper() == "PYTEST"