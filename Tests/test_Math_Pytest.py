import pytest

def add_twoNumbers(a, b):
    return a + b

@pytest.mark.math
def testSmallNumbers():
    assert add_twoNumbers(1, 2) == 3, "The sum of 1 and 2 should be 3"

@pytest.mark.math
def testLargeNumbers():
    assert add_twoNumbers(100, 300) == 400, "Damn! It should be 400!"
