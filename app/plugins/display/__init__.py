import logging #imports the logging class
from app.commands import Command #imports the command parent class to create child classes of command
from app.calculator import Calculator #imports the Calculator class to make calculator operations

class DisplayCommand(Command):
    '''
    Uses EAFP to perform the displayHistory command in calculator 
    '''
    def execute(self):
        try:
            logging.info("Here is the list of logged calculations:")
            print("Here is the list of logged calculations: ")
            Calculator.displayHistory()
        except Exception as e:
            print("Could not display the list of logged calculations.")
            logging.warning("Could not display the list of logged calculations: %s", repr(e))