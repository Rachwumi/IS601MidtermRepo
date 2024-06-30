import logging #imports the logging class
from app.commands import Command #imports the command parent class to create child classes of command
from app.calculator import Calculator #imports the Calculator class to make calculator operations

class DeleteCommand(Command):
    def execute(self):
        '''
        Uses EAFP to perform the displayHistory command, so the user can see the available records to choose from, then they choose a record to delete
        '''
        try:
            Calculator.displayHistory()
            pos = input("Please choose a record to delete from the list displayed >>> ")
            Calculator.deleteRecord(int(pos))
            print("History record was deleted")
            logging.info("History record was deleted")
        except Exception as e:
            print("Could not delete history record. Please choose a record displayed.")
            logging.warning("Could not delete history record. Please choose a record displayed: %s", repr(e))