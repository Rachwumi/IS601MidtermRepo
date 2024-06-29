import logging
from decimal import Decimal
from app.commands import Command
from app.calculator import Calculator

class AddCommand(Command):
    def execute(self):
        try:
            i1 = input("Please type your first decimal >>> ")
            i2 = input("Please type your second decimal >>> ")
            result = Calculator.subtract( Decimal(i1), Decimal(i2) , 'add')
            logging.info(f"The value of {i1} + {i2} is equal to {result}")
            print(f"The value of", i1, "+",i2, "is equal to",result)
            print(len(Calculator.calc_history.log))
        except Exception as e:
            logging.error('Please type in Decimal or Integer format: 2.0, 1.5, 18 %s', repr(e))
            print('Please type in Decimal or Integer format: 2.0, 1.5, 18')