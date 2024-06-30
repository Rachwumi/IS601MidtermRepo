from app.calculator.arithematic import add, subtract, divide, multiply #imports the arithematic class to class the calculation methods
from decimal import Decimal

class Calculation:

    def __init__(self, x: Decimal, y: Decimal, comp: str):
        '''
        This is the calculation constructor, used to create calculation instances
        '''
        self.x = x
        self.y = y
        self.comp = comp

    
    def performCalculation(self):
        '''
        returns the calculation of the two numbers based on the class variable comp
        '''        
        if self.comp == 'add':
            return add(self.x, self.y)
        elif self.comp == 'subtract':
            return subtract(self.x, self.y)
        elif self.comp == 'multiply':
            return multiply(self.x, self.y)
        else:
            return divide(self.x, self.y)



