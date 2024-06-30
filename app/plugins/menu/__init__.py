import logging #imports the logging class
from app.commands import Command #imports the command parent class to create child classes of command

class MenuCommand(Command):
    '''
    Uses EAFP to print the commands listed in the command dictionary
    '''
    def execute(self, commands):
        result = 'Here is the Menu of available commands: '
        for i in commands:
            result += i+', '
        print(result[:-2])
        logging.info(result[:-2])