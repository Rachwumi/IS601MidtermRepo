import logging
from app.commands import Command
from app.calculator import Calculator

class DisplayLastCommand(Command):
    def execute(self):
        try:
            calc = Calculator.displayLast()
            print(f"Here is the last calculation that was made: {calc.x}, {calc.y}, {calc.comp}")
            logging.info(f"Here is the last calculation that was made: {calc.x}, {calc.y}, {calc.comp}")
        except Exception as e:
            print("Could not retrieve the last calculation made")
            logging.warning("Could not retrieve the last calculation made: %s", repr(e))