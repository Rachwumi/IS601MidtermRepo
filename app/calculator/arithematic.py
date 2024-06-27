from decimal import Decimal

def add(x: Decimal , y: Decimal) -> Decimal:
    return x + y

def subtract(x: Decimal, y: Decimal) -> Decimal:
    return x - y

def divide(x: Decimal, y: Decimal) -> Decimal:
    if y == 0.0:
        raise Exception("You can not divide by zero")
    return x / y

def multiply(x: Decimal, y: Decimal) -> Decimal:
    return x * y