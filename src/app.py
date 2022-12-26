# Main, Start, Entrypoint > my names.
# (-)-(-)-(-)-(-)-(-)-(-)-(-)-(-)-(-)

from fastapi import FastAPI

from models.pydantic_models import *
from database.db import Base, engine
from routers import public, admin


Base.metadata.create_all(bind=engine)

app: object = FastAPI()
app.include_router(public.router)
app.include_router(admin.router)
