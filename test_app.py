
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def test_add():
    assert add(2,3) == 5
    assert add(-2,-3) == -5
    assert add(2,-1) == 1
    assert add(-1,2) == 1

def test_sub():
    assert subtract(2,3) == -1
    assert subtract(-2,-3) == 1
    assert subtract(2,-1) == 3
    assert subtract(-1,2) == -3

def test_mul():
    assert multiply(2,3) == 6
    assert multiply(-2,-3) == 6
    assert multiply(2,-1) == -2
    assert multiply(-1,2) == -2

def test_div():
    assert divide(2,1) == 2
