import logging #imports the logging class
from app.commands import Command #imports the command parent class to create child classes of command
from app.calculator import Calculator #imports the Calculator class to make calculator operations

class LoadCommand(Command):
    '''
    Uses EAFP to perform the loadHistory command in calculator when the user wants to load database records again at any point
    '''
    def execute(self):
        try:
            Calculator.loadHistory()
            logging.info("Calculation History was retrieved and loaded")
        except Exception as e:
            print("Could not retrieve and load the calculation history.")
            logging.warning("Could not retrieve and load the calculation history: %s", repr(e))