'''My History Test'''

from decimal import Decimal
import pytest
from faker import Faker
from app.calculator.calculation import Calculation as calc
from app.calculator.history import Calculator_History as log

fake = Faker()

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

@pytest.mark.parametrize("pos, cal", [
    (int("0"), calc(Decimal('20'), Decimal('36'), 'add')),
    (int("0"), calc(Decimal('4'), Decimal('5'), 'subtract'))
])

def test_removecalc(pos, cal):
    '''Test that the calculation history removeCalculation() method works '''
    log.emptyList()
    log.addCalculation(cal)
    temp = log.removeCalculation(pos)
    assert f"{cal.x}, {cal.y}, {cal.comp}" == f"{temp.x}, {temp.y}, {temp.comp}"

def test_emptylist():
    '''Test that the calculation history emptyList() method works '''
    calclist = [calc(Decimal(fake.random_number(digits=2)), Decimal(fake.random_number(digits=2)), 'add'),
                calc(Decimal(fake.random_number(digits=2)), Decimal(fake.random_number(digits=2)), 'add'),
                calc(Decimal(fake.random_number(digits=2)), Decimal(fake.random_number(digits=2)), 'subtract'),
                calc(Decimal(fake.random_number(digits=2)), Decimal(fake.random_number(digits=2)), 'multiply'),]
    for i in calclist:
        log.addCalculation(i)
    log.emptyList()
    assert len(log.log) == 0
