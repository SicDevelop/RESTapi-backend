from fastapi import APIRouter, Depends
from core.security import verify_password
from database.db import get_db
from sqlalchemy.orm import Session
from middlewares import crud, responses
from middlewares.create_tokens import signJWT
from middlewares.jwt_bearer import jwtBearer
from models.abstract_models import Teacher, Admin, \
                                   AdminInDB, RefreshToken, \
                                   Group, Shedule

router = APIRouter(
    prefix = '/api/admin',
    tags = ['Api for admin'],
    dependencies=[Depends(jwtBearer())],
    responses={404: {"description": "Not found"}},
)

@router.post('/add-teacher')
async def add_teacher(teacher: Teacher, ) -> dict:
    await crud.add_teacher(teacher)
    return responses.OK_RESPONSES['simple']

@router.post('/add-group')
async def add_group() -> dict:
    return {'Hello': 'World!'}

@router.post('/add-shedule')
async def add_shedule() -> dict:
    return {'Hello': 'World!'}
