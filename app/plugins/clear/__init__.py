import logging #imports the logging class
from app.commands import Command #imports the command parent class to create child classes of command
from app.calculator import Calculator #imports the Calculator class to make calculator operations

class ClearCommand(Command):
    '''
    Uses EAFP to perform the clearDatabase command in calculator 
    '''
    def execute(self):
        try:
            Calculator.clearDatabase()
            print("Calculation history was cleared. Please 'save' save to clear the database ")
            logging.info("Calculation history was cleared. Please 'save' to clear the database ")
        except Exception as e:
            print("Could not clear calculation history and database.")
            logging.warning("Could not clear calculation history and database: %s", repr(e))