import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
## Provides set of roots certificates commonly used by python libraries that is used to make secure HTTP connection


from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

ca=certifi.where() ## This line retrieve the path to the bundle of certificates. ca => Certificate authorities

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
            
    def csv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)

            records=list(json.loads(data.T.to_json()).values())

            return records

        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def insert_data_mongodb(self,records,database,collections):
        try:
            self.database = database
            self.collections = collections
            self.records = records
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)

            self.database = self.mongo_client[self.database]

            self.collections = self.database[self.collections]

            self.collections.insert_many(self.records)

            return (len(self.records))
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)

if __name__=="__main__":
    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE="MANAN"
    COLLECTION="NetworkData"
    network_obj=NetworkDataExtract()
    RECORDS=network_obj.csv_to_json_convertor(FILE_PATH)
    no_of_records = network_obj.insert_data_mongodb(RECORDS,DATABASE,COLLECTION)

    print(no_of_records)