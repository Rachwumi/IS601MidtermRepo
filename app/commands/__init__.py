import logging
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """ Look before you leap (LBYL) - Use when its less likely to work
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print(f"No such command: {command_name}")
        """
        if command_name == "menu":
            self.commands[command_name].execute(self.commands)
        elif command_name in self.commands:
            self.commands[command_name].execute()
        else:
            logging.error(f"No such command: {command_name}")
            print(f"No such command: {command_name}")
