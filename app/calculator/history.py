from app.calculator.calculation import Calculation as calc #imports the calculation class to make calculation instances
from app.database import DataHandler #imports the datahandler class for database operations
import logging #imports the logging class
from decimal import Decimal #imports the decimal class
from typing import List as list #imports the list class for array type casting
class Calculator_History:

    log: list[calc] = []

    @classmethod
    def addCalculation(cls, Calc):
        '''
            parameter: calc - calculation instance,
            Adds the given calculation instance to the history array
        '''
        cls.log.append(Calc)
    
    @classmethod
    def getLastCalculation(cls):
        '''
            Returns the last calculation (most recent) in the history array 
        '''
        return cls.log[len(cls.log)-1]
    
    @classmethod
    def removeCalculation(cls, pos: int):
        '''
            parameter: pos - user input number,
            returns and removes the history record chosen by the user
        '''
        return cls.log.pop(pos)

    @classmethod
    def emptyList(cls):
        '''
            empties the history array 
        '''
        cls.log.clear()

    @classmethod
    def saveDatabase(cls):
        '''
            saves the current records in the history array to the database
        '''
        DataHandler.saveDatabase(cls.buildSet())

    @classmethod
    def displayList(cls):
        '''
            displays the records and their position in the history array to the user 
        '''
        for i in range(len(cls.log)):
            print(i, ': ', cls.log[i].x, cls.log[i].y, cls.log[i].comp)
            logging.info(f"{i} : {cls.log[i].x}, {cls.log[i].y}, {cls.log[i].comp}")

    @classmethod
    def assistLoad(cls, db):
        '''
           takes the records from the database and loads them into the history array 
        '''
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
        '''
           Helper method used to build the list that will store the calculations to the database 
        '''
        result = []
        print(f"Saving {len(cls.log)} calculation(s).")
        logging.info(f"Size of the calculator history: {len(cls.log)}")
        for c in cls.log:
            result.append([c.x,c.y,c.comp])
        return result
