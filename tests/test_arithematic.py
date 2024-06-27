'''My Arithematic Test'''
from decimal import Decimal
import pytest
from app.calculator.arithematic import add, subtract, multiply, divide

def test_faker(int1, int2, operation, expected):
    ''' Testing the add, multiply, divide, and subtract arithematic'''
    if operation == 'add':
        assert add(int1, int2) == expected, f"Failed the addition with {int1} and {int2}"
    elif operation == 'multiply':
        assert multiply(int1, int2) == expected, f"Failed the multiply with {int1} and {int2}"
    elif operation == 'divide':
        assert divide(int1, int2) == expected, f"Failed the divide with {int1} and {int2}"
    else:
        assert subtract(int1, int2) == expected, f"Failed the subtract with {int1} and {int2}"

def test_dividefail():
    ''' Testing the divide fail arithematic'''
    with pytest.raises(Exception, match="You can not divide by zero"):
        assert divide(Decimal('10'), Decimal('0'))
