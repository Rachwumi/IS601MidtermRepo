import logging
from app.commands import Command
from app.calculator import Calculator

class DisplayCommand(Command):
    def execute(self):
        try:
            logging.info("Here is the list of logged calculations:")
            print("Here is the list of logged calculations: ")
            Calculator.displayHistory()
        except Exception as e:
            print("Could not display the list of logged calculations.")
            logging.warning("Could not display the list of logged calculations: %s", repr(e))