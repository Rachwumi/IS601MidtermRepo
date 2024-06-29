import logging
from decimal import Decimal
from app.commands import Command
from app.calculator import Calculator

class DivideCommand(Command):
    def execute(self):
        try:
            i1 = input("Please type your first decimal >>> ")
            i2 = input("Please type your second decimal >>> ")
            result = Calculator.subtract( Decimal(i1), Decimal(i2) , 'divide')
            logging.info(f"The value of {i1} / {i2} is equal to {result}")
            print(f"The value of", i1, "/",i2, "is equal to",result)
        except Exception:
            logging.error('Please type in Decimal or Integer format: 2.0, 1.5, 18, and your second decimal can not be 0.0')
            print('Please type in Decimal or Integer format: 2.0, 1.5, 18, and your second decimal can not be 0.0')