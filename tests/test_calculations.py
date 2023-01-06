import pytest
from app.calculations import add 

@pytest.mark.parametrize("num1, num2, expected", [
    (3,2,5), 
    (5,3,8),
    (-10,-2,-12)

])
def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1,num2) == expected

