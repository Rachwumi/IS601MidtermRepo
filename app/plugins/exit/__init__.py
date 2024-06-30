import sys
import logging
from app.calculator import Calculator 
from app.commands import Command


class ExitCommand(Command):
    def execute(self):
        logging.info("Exiting...")
        Calculator.saveHistory()
        sys.exit("Exiting...")