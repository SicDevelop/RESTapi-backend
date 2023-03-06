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

# ==== TEACHERS ====>
@router.post('/add-teacher')
async def add_teacher(teacher: Teacher, ) -> dict:
    await crud.add_teacher(teacher)
    return responses.OK_RESPONSES['simple']

@router.post('/edit-teacher')
async def edit_teacher(teacher: Teacher, teacher_id: int) -> dict:
    return {'Hello': 'World!'}

@router.post('/delete-teacher')
async def delete_teacher(teacher_id: int) -> dict:
    return {'Hello': 'World!'}

# ==== GROUPS ====>
@router.post('/add-group')
async def add_group(group: Group) -> dict:
    return {'Hello': 'World!'}

@router.post('/edit-group')
async def edit_group(group_id: int, group: Group) -> dict:
    return {'Hello': 'World!'}

@router.post('/remove-group')
async def remove_group(group_id: int) -> dict:
    return {'Hello': 'World!'}

# ==== SHEDULE ====>
@router.post('/add-shedule')
async def add_shedule(group_id: int, shedule: Shedule) -> dict:
    return {'Hello': 'World!'}

@router.post('/edit-shedule')
async def edit_shedule(group_id: int, shedule: Shedule) -> dict:
    return {'Hello': 'World!'}

