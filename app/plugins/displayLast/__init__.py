import logging #imports the logging class
from app.commands import Command #imports the command parent class to create child classes of command
from app.calculator import Calculator #imports the Calculator class to make calculator operations 

class DisplayLastCommand(Command):
    '''
    Uses EAFP to perform the displayLast command in calculator 
    '''
    def execute(self):
        try:
            calc = Calculator.displayLast()
            print(f"Here is the last calculation that was made: {calc.x}, {calc.y}, {calc.comp}")
            logging.info(f"Here is the last calculation that was made: {calc.x}, {calc.y}, {calc.comp}")
        except Exception as e:
            print("Could not retrieve the last calculation made")
            logging.warning("Could not retrieve the last calculation made: %s", repr(e))