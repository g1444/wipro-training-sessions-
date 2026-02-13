import pytest
@pytest.mark.smoke
def test_smoke():
    assert 2+2==4

@pytest.mark.skip(reason="not ready")
def test_skip1():
    assert 11==11
