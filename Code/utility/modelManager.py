# from .dbmanager import db_client
from .dbmanager import db

class DbBaseModel(object):

    data_to_save:dict = None

    def __init__(self,**args):
        print("In Parent DB model manager class")
        print(args)
        self.data_to_save = args
        for attribute in args.keys():
            self.attribute = args[attribute]

    def save(self):
        print("in parent save method >>")
        print(self.data_to_save)
        return db.save(self.Meta.table_name,self.data_to_save)
    
    def get(self,**args):
        return db.get(self.Meta.table_name,args)
    
    def get_all(self):
        return db.get_all(self.Meta.table_name)