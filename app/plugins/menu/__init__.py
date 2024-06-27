import logging
from app.commands import Command

class MenuCommand(Command):
    def execute(self, commands):
        result = 'Here is the Menu of available commands: '
        for i in commands:
            result += i+', '
        print(result[:-2])
        logging.info(result[:-2])