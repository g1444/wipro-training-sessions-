import pytest

@pytest.mark.xfail(reason="Known bug: division error")
def test_xfail_demo():
    assert 10 / 0

@pytest.mark.skip(reason="skipping feature because it is not ready")
def test_skip_1():
    assert True