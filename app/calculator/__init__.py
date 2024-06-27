from app.calculator.history import Calculator_History
from app.calculator.calculation import Calculation
from decimal import Decimal


class Calculator:
    @staticmethod
    def _calculate(x:Decimal, y: Decimal, comp:str) -> Decimal:
            calc = Calculation(x, y, comp)
            Calculator_History.addCalculation(calc)
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

