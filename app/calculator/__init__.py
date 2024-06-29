from app.calculator.history import Calculator_History
from app.calculator.calculation import Calculation
from app.database import DataHandler
from decimal import Decimal


class Calculator:
    calc_history = Calculator_History()

    @staticmethod
    def _calculate(x:Decimal, y: Decimal, comp:str) -> Decimal:
            calc = Calculation(x, y, comp)
            Calculator.calc_history.addCalculation(calc)
            print("Log size during calculate: ",len(Calculator.calc_history.log))
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
    def saveHistory():
          Calculator.calc_history.saveDatabase()

    @staticmethod
    def loadHistory():
          Calculator.calc_history.assistLoad(DataHandler.loadDatabase())
          print('Loaded ', len(Calculator.calc_history.log), ' calculations into the calculator:')
          for c in Calculator.calc_history.log:
            print(c.x,c.y,c.comp)