from app.calculator.calculation import Calculation as calc
from app.database import DataHandler
import logging
from decimal import Decimal
from typing import List as list
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
    def emptyList(cls):
        return cls.log.clear()

    @classmethod
    def saveDatabase(cls):
        DataHandler.saveDatabase(cls.buildSet())

    @classmethod
    def displayList(cls):
        for i in range(len(cls.log)):
            print(i, ': ', cls.log[i].x, cls.log[i].y, cls.log[i].comp)
            logging.info(f"{i} : {cls.log[i].x}, {cls.log[i].y}, {cls.log[i].comp}")

    @classmethod
    def assistLoad(cls, db):
        result: list[calc] = []
        try:
            for index, row in db.iterrows():
                n1 = row['num1']
                n2 = row['num2']
                comp = row['computation']
                logging.info(f'Database record being loaded: {n1}, {n2}, {comp}')
                result.append(calc(Decimal(n1), Decimal(n2), comp))
            logging.info('Database loaded into calculator')
            cls.log = result
        except Exception as e:
            print("Could not load database")
            logging.warning(f'Could not load database: {repr(e)}')
        finally:
            cls.log = result
            
    @classmethod
    def buildSet(cls):
        result = []
        print(f"Saving {len(cls.log)} calculation(s).")
        logging.info(f"Size of the calculator history: {len(cls.log)}")
        for c in cls.log:
            result.append([c.x,c.y,c.comp])
        return result
