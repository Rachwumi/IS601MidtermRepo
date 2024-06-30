import logging
from app.commands import Command
from app.calculator import Calculator

class ClearCommand(Command):
    def execute(self):
        try:
            Calculator.clearDatabase()
            print("Calculation history and database were cleared")
            logging.info("Calculation history and database were cleared")
        except Exception as e:
            print("Could not clear calculation history and database.")
            logging.warning("Could not clear calculation history and database: %s", repr(e))