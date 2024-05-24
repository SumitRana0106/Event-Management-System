import os 

# Environment 
ENV = os.getenv("ENV") if os.getenv("ENV")!=None else "DEV"
DB_TYPE= os.getenv("DB_TYPE") if os.getenv("DB_TYPE")!=None else "MONGO"
DB_CONNECTION_URI= os.getenv('DB_CONNECTION_URI') if os.getenv('DB_CONNECTION_URI')!=None else "mongodb://root:root@localhost:27017/"
DB_NAME = os.getenv('DB_NAME') if os.getenv('DB_NAME')!=None else "AppEventsDb"