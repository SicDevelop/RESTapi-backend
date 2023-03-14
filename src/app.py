from fastapi import FastAPI
from models.pydantic_models import *
from database.db import Base, engine

from apps.v1.routers import public
from apps.v1.routers import operator


Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def index():
    return {'message': 'hello'}


api_v1 = FastAPI()
api_v1.include_router(public.router)
api_v1.include_router(operator.router)

app.mount("/api/v1", api_v1)