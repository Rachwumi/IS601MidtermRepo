from app.calculator.calculation import Calculation as calc
from typing import List as list

## History needs an init class now to load all the data from the pandas library into the calculation list
class Calculator_History:
    log: list[calc] = []

    @classmethod
    def addCalculation(cls, Calc):
        return cls.log.append(Calc)
    
    @classmethod
    def getLastCalculation(cls):
        return cls.log[len(cls.log)-1]
    
    @classmethod
    def removeCalculation(cls, pos):
        return cls.log.pop(pos)

    @classmethod
    def removeLastCalculation(cls):
        return cls.log.pop()

    @classmethod
    def emptyList(cls):
        return cls.log.clear()
