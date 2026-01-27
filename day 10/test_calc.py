from calc import add,sub,mul,div
import pytest
def test_add():
    assert add(2,3)==5
def test_sub():
    assert sub(2,1)==1
def test_mul():
    assert mul(2,3)==6
def test_div():
    assert div(10,5)==2
def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        div(10,0)