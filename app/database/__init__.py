import os
import pandas as pd
import logging as log

class DataHandler:
    _absdatadir = ""
    _absdatafile = ""
    _absdatapath = ""
    _database = ""

    @staticmethod
    def loadDatabase():
        try:
            if not os.path.exists(DataHandler._absdatadir):
                os.makedirs(DataHandler._absdatadir)
                DataHandler.setDatabase()
                return DataHandler._database
            else:
                DataHandler.setDatabase()
                return DataHandler._database
        except Exception as e:
            log.error('%s', repr(e))
    
    @staticmethod
    def saveDatabase(calcList):
        try:
            DataHandler._database = pd.DataFrame(calcList, columns = ['num1', 'num2', 'computation'])
            DataHandler._database.to_csv(DataHandler._absdatapath, index=False)
        except Exception as e:
            log.error('%s', repr(e))
    
    @staticmethod
    def clearDatabase():
        DataHandler._database.iloc[0:0]
        DataHandler._database.to_csv(DataHandler._absdatapath, index=False)

    @staticmethod
    def setDir(dir):
        DataHandler._absdatadir = dir

    @staticmethod
    def setFile(file):
        DataHandler._absdatafile = file

    @staticmethod
    def setPath():
        temp = os.path.join(DataHandler._absdatadir,DataHandler._absdatafile)
        DataHandler._absdatapath = os.path.abspath(temp)
    
    @staticmethod
    def getPath():
        return DataHandler._absdatapath
    
    @staticmethod
    def setDatabase():
        try:
            DataHandler._database = pd.read_csv(DataHandler._absdatapath)
        except Exception as e:
            log.warning('Database could not be set or found: %s', repr(e))