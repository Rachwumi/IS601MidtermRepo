import logging
from decimal import Decimal
from app.commands import Command
from app.calculator import Calculator

class SubtractCommand(Command):
    def execute(self, i1, i2):
        try:
            result = Calculator.subtract( Decimal(i1), Decimal(i2) , 'subtract')
            logging.info(f"The value of", i1, "-",i2, "is equal to",result)
            print(f"The value of", i1, "-",i2, "is equal to",result)
        except Exception:
            logging.error('Please type in Decimal or Integer format: 2.0, 1.5, 18')
            print('Please type in Decimal or Integer format: 2.0, 1.5, 18')