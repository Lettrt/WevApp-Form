from fastapi import FastAPI
from mongoengine import connect
from dotenv import load_dotenv
import os
from .routers import router

load_dotenv()
connect(host=os.getenv('MONODB_URL'))

app = FastAPI()
app.include_router(router)