import logging #imports the logging class
from decimal import Decimal #imports the decimal class
from app.commands import Command #imports the command parent class to create child classes of command
from app.calculator import Calculator #imports the Calculator class to make calculator operations

class SubtractCommand(Command):
    def execute(self):
        '''
        Uses EAFP to get two numbers from the user and then performs the associated calculation with the command
        '''
        try:
            i1 = input("Please type your first decimal >>> ")
            i2 = input("Please type your second decimal >>> ")
            result = Calculator.subtract( Decimal(i1), Decimal(i2) , 'subtract')
            logging.info(f"The value of {i1} - {i2} is equal to {result}")
            print(f"The value of", i1, "-",i2, "is equal to",result)
        except Exception as e:
            logging.error('Please type in Decimal or Integer format: 2.0, 1.5, 18. %s', repr(e))
            print('Please type in Decimal or Integer format: 2.0, 1.5, 18')