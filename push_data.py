import sys
import os 
import json 

from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL = os.getenv('MONGO_DB_URL')

import certifi

ca = certifi.where()

import pandas as pd 
import numpy as np 
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging 
import pymongo

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json(self,filepath):
        try:
            df = pd.read_csv(filepath)
            df.reset_index(drop=True, inplace=True)
            records = list(json.loads(df.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def insert_data_mongodb(self,records,database,collection):
        try:
            self.records = records
            self.database = database
            self.collection = collection

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tls = True, tlsCAFile = ca)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)

            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE  = "Cyril" 
    COLLECTION = "NetworkSecurity"

    network_obj = NetworkDataExtract()
    records = network_obj.csv_to_json(filepath=FILE_PATH)
    print(records)
    network_obj.insert_data_mongodb(records,DATABASE,COLLECTION)
    print(len(records))
