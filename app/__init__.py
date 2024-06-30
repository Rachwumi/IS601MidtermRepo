import os
import pkgutil
import importlib
import sys
import importlib
from app.database import DataHandler
from app.commands import Command
from app.commands import CommandHandler 
from dotenv import load_dotenv
import logging
import logging.config

class App:
    def __init__(self): #The App Constructor used to buiild and load different variables used in the background
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.load_datapaths()
        self.command_handler = CommandHandler()

    def configure_logging(self):
        '''
        Method used to set the logging configuration with LBYL. 
        If the file exists then it configures with the file, if it doesn't exist then it makes a basic configuration.
        '''
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        '''
        Method used to load the environment variables from the environment file
        '''
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings
    
    def load_datapaths(self):
        '''
        Method uses EAFP to load the datapath for database handling into the DataHandler static class
        '''
        try:
            DataHandler.setDir(self.get_dataDir())
            DataHandler.setFile(self.get_dataFile())
            DataHandler.setPath()
            logging.info(f"loaded the datapath.")
        except:
            logging.error("Unexpeceted Error occurred while loading the data path, please check the environment variables")
    
    def get_dataDir(self, env_var: str = 'PANDAS_DIR'):
        '''
        Returns the value stored for the pandas directory in the environment file
        '''
        return self.settings.get(env_var, None)

    def get_dataFile(self, env_var: str = 'PANDAS_FILE'):
        '''
        Returns the value stored for the pandas file in the environment file
        '''
        return self.settings.get(env_var, None)

    def load_plugins(self):
        '''
        Method uses EAFP and LBYL to dynamically get the plugins from the plugin directory and store them into 
        '''
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.error(f"Error importing plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        '''
        Method is used to store the plugin commands from the package and the command given 
        '''
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                # Command names are now explicitly set to the plugin's folder name
                self.command_handler.register_command(plugin_name, item())
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")  

    def start(self):
        '''
        Method uses the REPL design to run multiple user commands and executes the operation necessary based on the command given.
        Before running REPL, it provides a menu of the commands available and loads any of the previous calculations stored in the database 
        '''
        self.load_plugins()
        self.command_handler.execute_command("menu")
        self.command_handler.execute_command("load")
        print("Application started. Type 'exit' to exit.")
        logging.info("Application started. Type 'exit' to exit.")
        try:
            while True:
                cmd_input = input(">>> ").strip()
                try:
                    self.command_handler.execute_command(cmd_input)
                except KeyError:  # Assuming execute_command raises KeyError for unknown commands
                    logging.error(f"Unknown command: {cmd_input}")
                    sys.exit(1)  # Use a non-zero exit code to indicate failure or incorrect command.
        except KeyboardInterrupt:
            logging.info("Application interrupted and exiting gracefully.")
            sys.exit(0)  # Assuming a KeyboardInterrupt should also result in a clean exit.
        finally:
            logging.info("Application shutdown.")