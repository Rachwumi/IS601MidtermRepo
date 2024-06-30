import logging
from app.commands import Command
from app.calculator import Calculator

class LoadCommand(Command):
    def execute(self):
        try:
            Calculator.loadHistory()
            logging.info("Calculation History was retrieved and loaded")
        except Exception as e:
            print("Could not retrieve and load the calculation history.")
            logging.warning("Could not retrieve and load the calculation history: %s", repr(e))