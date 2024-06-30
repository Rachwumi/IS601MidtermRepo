import logging
from abc import ABC, abstractmethod #import abstractmethod to create Inheritance classes

class Command(ABC):
    '''
    Parent class used to create other command children classes
    '''
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        '''
        CommandHandler constructor
        '''
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        '''
        add the key and value pair to the commands dictionary
        '''
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """ 
        Implements LBYL to handle user input, and calls the appropriate execution
        """
        if command_name == "menu":
            self.commands[command_name].execute(self.commands)
        elif command_name in self.commands:
            self.commands[command_name].execute()
        else:
            logging.error(f"No such command: {command_name}")
            print(f"No such command: {command_name}")
