from fastapi import FastAPI 
from app.views import root as rootRouter
from utility.dbmanager import dbManager
import os



# fast app initiation
app = FastAPI()

# Views manager
app.include_router(rootRouter)
