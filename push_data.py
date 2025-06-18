# import os 
# import sys
# import json

# from dotenv import load_dotenv
# load_dotenv()

# MONGO_DB_URL=os.getenv("MONGO_DB_URL")
# print(MONGO_DB_URL)

# import certifi
# ca = certifi.where()


# import pandas as pd
# import numpy as np
# import pymongo
# from networksecurity.exception.exception import NetworksecurityException
# from networksecurity.logging.logger import logging

# class NetworkDataExtract():
#     def __init__(self):
#         try:
#             pass
#         except Exception as e:
#             raise NetworksecurityException(e,sys)
        

#     def cv_to_json_convertor(self,file_path):
#         try:
#             data=pd.read_csv(file_path)
#             data.reset_index(drop=True,inplace=True)
#             # records=list(json.load(data.T.to_json()).values()
#             records = json.loads(data.to_json(orient='records'))

#             return records
        
#         except Exception as e:
#             raise NetworksecurityException(e,sys)
        
#     def insert_data_mongodb(self,records,database,collection):
#         try:
#             self.database=database
#             self.collection=collection
#             self.records=records

#             self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
#             self.database=self.mongo_client[self.database]

#             self.collectionself.database[self.collection]
#             self.collection.insert_many(self.records)
#             return(len(self.records))
#         except Exception as e:
#             raise NetworksecurityException(e,sys)
        
# if __name__=="__main__":
#     FILE_PATH="Network_Data\Phising_Detection_Dataset.csv"
#     DATABASE="RAHUL YADAV"
#     collection="NetworkData"
#     networkobj=NetworkDataExtract()
#     records=networkobj.cv_to_json_convertor(file_path=FILE_PATH)
#     print(records)
#     no_of_records=networkobj.insert_data_mongodb(records,DATABASE,collection)
#     print(no_of_records)



import os
import sys
import json
import pandas as pd
import pymongo
import certifi
from dotenv import load_dotenv

from networksecurity.exception.exception import NetworksecurityException
from networksecurity.logging.logger import logging

load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print("MongoDB URL:", MONGO_DB_URL)

class NetworkDataExtract:
    def __init__(self):
        pass

    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = json.loads(data.to_json(orient='records'))
            return records
        except Exception as e:
            raise NetworksecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=certifi.where())
            db = self.mongo_client[database]
            coll = db[collection]
            coll.insert_many(records)
            return len(records)
        except Exception as e:
            raise NetworksecurityException(e, sys)

if __name__ == "__main__":
    FILE_PATH = "Network_Data/Phising_Detection_Dataset.csv"
    DATABASE = "RAHUL_YADAV"
    COLLECTION = "NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(f"First Record: {records[0]}")
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, COLLECTION)
    print(f"Inserted {no_of_records} records.")
