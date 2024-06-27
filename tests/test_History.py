'''My History Test'''

from decimal import Decimal
from app.calculator.calculation import Calculation as calc
from app.calculator.history import Calculator_History as log

def test_addcalc():
    '''Test that the calculation history addCalculation() method works ''' 
    log.log.clear()
    c = calc(Decimal('10'), Decimal('5'), 'add')
    log.addCalculation(c)
    assert len(log.log) == 1

def test_getlastcalc():
    '''Test that the calculation history getLastCalculation() method works '''
    c = calc(Decimal('10'), Decimal('5'), 'add')
    log.addCalculation(c)
    assert log.getLastCalculation() == c
