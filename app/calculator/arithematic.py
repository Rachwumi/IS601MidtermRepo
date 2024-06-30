from decimal import Decimal #imports the decimal class

def add(x: Decimal , y: Decimal) -> Decimal:
    '''
    returns the addition of the two numbers given
    '''
    return x + y

def subtract(x: Decimal, y: Decimal) -> Decimal:
    '''
    returns the subtraction of the two numbers given
    '''
    return x - y

def divide(x: Decimal, y: Decimal) -> Decimal:
    '''
    returns the division of the two numbers given as long as y is not 0, if y is 0 then an exception is thrown
    '''
    if y == 0.0:
        raise Exception("You can not divide by zero")
    return x / y

def multiply(x: Decimal, y: Decimal) -> Decimal:
    '''
    returns the multiplication of the two numbers given
    '''
    return x * y