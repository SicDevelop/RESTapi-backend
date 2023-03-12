from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi import FastAPI
from models.pydantic_models import *
from database.db import Base, engine
from routers import public, admin


Base.metadata.create_all(bind=engine)

app: object = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(public.router)
app.include_router(admin.router)

Instrumentator().instrument(app).expose(app)