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
        '''
           Uses LBYL and EAFP to see if the database directory needs to be created.
           Once checked and created/found the database variable gets set and the database is returned
        '''
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
        '''
           Uses EAFP to store the values from the history array into the database
        '''        
        try:
            DataHandler._database = pd.DataFrame(calcList, columns = ['num1', 'num2', 'computation'])
            DataHandler._database.to_csv(DataHandler._absdatapath, index=False)
            log.info("Calculations were saved to the database.")
            print("Calculations were saved to the database.")
        except Exception as e:
            log.error('%s', repr(e))
    
    @staticmethod
    def clearDatabase():
        '''
           Clears the database
        '''
        DataHandler._database.iloc[0:0]
        DataHandler._database.to_csv(DataHandler._absdatapath, index=False)

    @staticmethod
    def setDir(dir):
        '''
        Sets the database directory gathered from the environment variable
        '''
        DataHandler._absdatadir = dir

    @staticmethod
    def setFile(file):
        '''
        Sets the database file name gathered from the environment variable
        '''
        DataHandler._absdatafile = file

    @staticmethod
    def setPath():
        '''
        Sets the database file path and creates the absolute path from that path
        '''
        temp = os.path.join(DataHandler._absdatadir,DataHandler._absdatafile)
        DataHandler._absdatapath = os.path.abspath(temp)
    
    @staticmethod
    def getPath():
        '''
        returns the database absolute path
        '''
        return DataHandler._absdatapath
    
    @staticmethod
    def setDatabase():
        '''
           Uses EAFP tostore the database in the database variable
        '''          
        try:
            DataHandler._database = pd.read_csv(DataHandler._absdatapath)
        except Exception as e:
            log.warning('Database could not be set or found: %s', repr(e))