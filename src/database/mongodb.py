import pymongo
import os


import certifi
ca = certifi.where()

class MongodbOperation:

    def __init__(self) -> None:
        MONGO_DB_URL = "mongodb+srv://ankur:ankur123@cluster0.ulksw3z.mongodb.net/?retryWrites=true&w=majority"
        self.client = pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=ca)
        self.db_name="SENSOR"

    def insert_many(self,collection_name,records:list):
        self.client[self.db_name][collection_name].insert_many(records)

    def insert(self,collection_name,record):
        self.client[self.db_name][collection_name].insert_one(record)
        
