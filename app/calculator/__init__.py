from app.calculator.history import Calculator_History #imports the history class for history operations
from app.calculator.calculation import Calculation #imports the calculation class to make calculation instances
from app.database import DataHandler #imports the datahandler class for database operations
from decimal import Decimal #imports the decimal class
import logging as log #imports the logging class

class Calculator:
      calc_history = Calculator_History()

      @staticmethod
      def _calculate(x:Decimal, y: Decimal, comp:str) -> Decimal:
            '''
            parameters: x - user inputted number, y - user inputted number, comp - user inputted arithematic
            Creates a calculation instance, stores that instance into the history array, and then calls the public instance method performCalculation in the Calculator_History class
            '''
            calc = Calculation(x, y, comp)
            Calculator.calc_history.addCalculation(calc)
            return calc.performCalculation()

      @staticmethod
      def add(x:Decimal, y:Decimal, com: str):
            '''
            returns the private static method calculate in the Calulator class
            '''
            return Calculator._calculate(x,y,com)
    
      @staticmethod
      def subtract(x:Decimal, y:Decimal, com: str):
            '''
            returns the private static method calculate in the Calulator class
            '''
            return Calculator._calculate(x,y,com)
    
      @staticmethod
      def divide(x:Decimal, y:Decimal, com: str):
            '''
            returns the private static method calculate in the Calulator class
            '''
            return Calculator._calculate(x,y,com)
    
      @staticmethod
      def multiply(x:Decimal, y:Decimal, com: str):
            '''
            returns the private static method calculate in the Calulator class
            '''
            return Calculator._calculate(x,y,com)

      @staticmethod
      def displayHistory():
            '''
            calls the public class method displayList in the Calulator_History class
            '''
            Calculator.calc_history.displayList()
      
      @staticmethod
      def displayLast():
            '''
            returns the calculation value from the public class method getLastCalculation in the Calulator_History class
            '''           
            return Calculator.calc_history.getLastCalculation()

      @staticmethod
      def saveHistory():
            '''
            calls the public class method saveDatabase in the Calulator_History class
            '''
            Calculator.calc_history.saveDatabase()

      @staticmethod
      def clearDatabase():
            '''
            calls the public class method emptyList in the Calulator_History class
            '''
            Calculator.calc_history.emptyList()

      @staticmethod
      def deleteRecord(pos: int):
            '''
            parameter: pos - user input postion in the history array
            calls the public instance method removeCalculation in the Calulator_History class
            '''
            Calculator.calc_history.removeCalculation(pos)

      @staticmethod
      def loadHistory():
            '''
            calls the public instance method assistLoad in the Calulator_History class.
            Once called it displays and logs the total number of loaded calculations and logs the calculations loaded
            '''
            Calculator.calc_history.assistLoad(DataHandler.loadDatabase())
            print('Loaded',len(Calculator.calc_history.log),'previous calculation(s) into the calculator')
            log.info(f'Loaded {len(Calculator.calc_history.log)} calculations into the calculator:')
            for c in Calculator.calc_history.log:
                  log.info(f'{c.x}, {c.y}, {c.comp}')

