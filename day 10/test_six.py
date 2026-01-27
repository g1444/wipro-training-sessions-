import pytest

@pytest.fixture()
def setup_teardown():
    print("\nsetup")
    yield
    print("\nteardown")
def test_setup(setup_teardown):
    print("test running")