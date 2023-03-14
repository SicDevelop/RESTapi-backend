from fastapi import FastAPI
from apps.v1 import v1
from models.pydantic_models import *
from database.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def index():
    return {'message': 'hello'}


app.mount("/api/v1", v1.app)