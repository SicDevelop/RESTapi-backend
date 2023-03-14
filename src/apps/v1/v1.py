from fastapi import FastAPI
from .routers import public
from .routers import operator

app = FastAPI()
app.include_router(public.router)
app.include_router(operator.router)