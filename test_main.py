from main import add
from main import subtract

def test_add():
    assert add(1, 2) == 3
    assert add(4, 9) == 13
def test_subtract():
    assert subtract(5, 1) == 4
    assert subtract(100, 56) == 44