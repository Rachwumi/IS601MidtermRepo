import sys #imports the system class
import logging #imports the logging class
from app.calculator import Calculator #imports the Calculator class to make calculator operations
from app.commands import Command #imports the command parent class to create child classes of command


class ExitCommand(Command):
    '''
    performs the saveHistory command, in calculator, before exiting the program
    '''
    def execute(self):
        logging.info("Exiting...")
        Calculator.saveHistory()
        sys.exit("Exiting...")