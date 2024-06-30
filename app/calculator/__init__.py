from app.calculator.history import Calculator_History
from app.calculator.calculation import Calculation
from app.database import DataHandler
from decimal import Decimal
import logging as log

class Calculator:
      calc_history = Calculator_History()

      @staticmethod
      def _calculate(x:Decimal, y: Decimal, comp:str) -> Decimal:
            calc = Calculation(x, y, comp)
            Calculator.calc_history.addCalculation(calc)
            return calc.performCalculation()

      @staticmethod
      def add(x:Decimal, y:Decimal, com: str):
            return Calculator._calculate(x,y,com)
    
      @staticmethod
      def subtract(x:Decimal, y:Decimal, com: str):
            return Calculator._calculate(x,y,com)
    
      @staticmethod
      def divide(x:Decimal, y:Decimal, com: str):
            return Calculator._calculate(x,y,com)
    
      @staticmethod
      def multiply(x:Decimal, y:Decimal, com: str):
            return Calculator._calculate(x,y,com)

      @staticmethod
      def displayHistory():
            Calculator.calc_history.displayList()
      
      @staticmethod
      def displayLast():
            return Calculator.calc_history.getLastCalculation()

      @staticmethod
      def saveHistory():
            Calculator.calc_history.saveDatabase()

      @staticmethod
      def clearDatabase():
            Calculator.calc_history.emptyList()

      @staticmethod
      def deleteRecord(pos):
            Calculator.calc_history.removeCalculation(pos)

      @staticmethod
      def loadHistory():
            Calculator.calc_history.assistLoad(DataHandler.loadDatabase())
            print('Loaded',len(Calculator.calc_history.log),'previous calculation(s) into the calculator')
            log.info(f'Loaded {len(Calculator.calc_history.log)} calculations into the calculator:')
            for c in Calculator.calc_history.log:
                  log.info(f'{c.x}, {c.y}, {c.comp}')

