import logging #imports the logging class
from app.commands import Command #imports the command parent class to create child classes of command
from app.calculator import Calculator #imports the Calculator class to make calculator operations

class SaveCommand(Command):
    '''
    Uses EAFP to perform the saveHistory command in calculator when the user wants to save at any point
    '''
    def execute(self):
        try:
            Calculator.saveHistory()
            logging.info("Calculation History was saved and stored into the database")
        except Exception as e:
            print("Could not save and store the calculation history.")
            logging.warning("Could not save and store the calculation history: %s", repr(e))