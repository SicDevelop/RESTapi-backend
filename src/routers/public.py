# Public router! OKAY AM ON PUBLIC! AM A STAR!

from fastapi import APIRouter, Depends
from database.db import get_db
from sqlalchemy.orm import Session
from models.pydantic_models import Teachers


router = APIRouter(
    prefix = '/api/public',
    tags = ['Public API']
)

@router.get('/teachers')
async def teachers(db: Session = Depends(get_db)) -> Teachers:
    return {'content': 'teachers'}
