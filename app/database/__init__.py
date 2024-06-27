import os
import pandas as pd
import logging as log

class DataHandler:
    _absdatapath = ""

    @staticmethod
    def loadDatabase():
        return
    
    @staticmethod
    def saveDatabase(calcList):
        return
    
    @staticmethod
    def clearDatabase():
        return

    def setPath(path):
        DataHandler._absdatapath = os.path.abspath(path)
    
    def getPath():
        return DataHandler._absdatapath