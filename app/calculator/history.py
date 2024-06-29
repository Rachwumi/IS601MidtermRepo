from app.calculator.calculation import Calculation as calc
from app.database import DataHandler
import logging
from decimal import Decimal
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

    @classmethod
    def saveDatabase(cls):
        DataHandler.saveDatabase(cls.buildSet())
        return

    @classmethod
    def assistLoad(cls, db):
        result: list[calc] = []
        try:
            for index, row in db.iterrows():
                print(row['num1'], row['num2'], row['computation'])
                result.append(calc(Decimal(row['num1']), row['num2'], row['computation']))
            logging.info('Database loaded')
            cls.log = result
        except Exception as e:
            logging.warning(f'Could not load database: {repr(e)}')
        finally:
            cls.log = result
            
    @classmethod
    def buildSet(cls):
        result = []
        print(len(cls.log))
        for c in cls.log:
            result.append([c.x,c.y,c.comp])
        return result
        