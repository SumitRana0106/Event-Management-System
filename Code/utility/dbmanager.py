from pymongo import MongoClient

class MongoManager:
    client = None

    def __init__(self,uri,db_name):
        if uri is not None:
            self.client = MongoClient(uri)
        else:
            raise Exception("Incorrect db connection string !!")
        
        self.client_db = self.client[db_name]
    
    def __str__(self):
        return self.client

    
    def save(self,collection, row_dict):
        res = self.client_db[collection].insert_one(row_dict)
        return res
    
    def get(self,collection,args):
        res = self.client_db[collection].find_one(args)
        return res
    
    def get_all(self,collection):
        res = self.client_db[collection].find({})
        return list(res)
    
    def __del__(self):
        pass


class ElasticDbManager:
    pass


# Db Manager initialization
db_client = None

def dbManager(db_type,**args):
    global db_client
    if db_type == "MONGO":
        db_client = MongoManager(args['uri'],args['db'])
        return db_client


from Config import *

print("uri: ", DB_CONNECTION_URI)
# # DB manager
db = dbManager(DB_TYPE,uri=DB_CONNECTION_URI,db=DB_NAME)
print("Database Initiation : " )
