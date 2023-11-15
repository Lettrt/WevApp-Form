from fastapi import FastAPI
from mongoengine import connect
from dotenv import load_dotenv
import os
from .routers import router
from .forms import create_initial_templates

load_dotenv()
print(os.getenv('MONGODB_URL'))
connect(host=os.getenv('MONGODB_URL'))

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
def on_startup():
    print(os.getenv('MONGODB_URL'))
    create_initial_templates()
