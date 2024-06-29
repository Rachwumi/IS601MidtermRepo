import logging
from app.commands import Command
from app.calculator import Calculator

class SaveCommand(Command):
    def execute(self):
        try:
            Calculator.saveHistory()
            logging.info("Calculation History was saved and stored into the database")
        except Exception as e:
            print("Could not save and store the calculation history.")
            logging.warning("Could not save and store the calculation history: %s", repr(e))