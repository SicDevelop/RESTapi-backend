# Public router! OKAY AM ON PUBLIC! AM A STAR!

from fastapi import APIRouter, Depends
from database.db import get_db
from sqlalchemy.orm import Session
from models.pydantic_models import Teachers
from middlewares import crud

router = APIRouter(
    prefix = '/api/public',
    tags = ['Public API']
)

@router.get('/teachers')
async def teachers(db: Session = Depends(get_db)) -> Teachers:
    return await crud.get_teachers(db=db)

@router.get('/groups')
async def groups(db: Session = Depends(get_db)) -> Teachers:
    return await crud.get_groups(db=db)

@router.get('/get_shedule')
async def get_shedule(group: str, datetime: int = 0, db: Session = Depends(get_db)) -> None:
    pass
    #return await crud.
