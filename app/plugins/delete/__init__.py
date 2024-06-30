import logging
from app.commands import Command
from app.calculator import Calculator

class DeleteCommand(Command):
    def execute(self):
        try:
            Calculator.displayHistory()
            pos = input("Please choose a record to delete from the list displayed >>> ")
            Calculator.deleteRecord(int(pos))
            print("History record was deleted")
            logging.info("History record was deleted")
        except Exception as e:
            print("Could not delete history record. Please choose a record displayed.")
            logging.warning("Could not delete history record. Please choose a record displayed: %s", repr(e))