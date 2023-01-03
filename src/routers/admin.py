# Private space? WTF...

from fastapi import APIRouter, Depends
from database.db import get_db
from sqlalchemy.orm import Session
from models.abstact_models import Admin, RefreshToken, Teacher, Group, Shedule
from middlewares import crud, create_tokens
from core.security import get_password_hash, verify_password
from middlewares.jwt_bearer import jwtBearer
from middlewares.create_tokens import signJWT, decodeJWT

router = APIRouter(
    prefix = '/api/admin',
    tags = ['API for administrators']
)

@router.post('/register')
async def register(admin: Admin, db: Session = Depends(get_db)) -> dict:
    hashed_password: str = get_password_hash(admin.password)
    return await crud.add_admin(username=admin.username, hashed_password=hashed_password, db=db)

@router.post('/login')
async def login(admin: Admin, db: Session = Depends(get_db)) -> dict:
    user: object = await crud.check_admin(username=admin.username, db=db)
    if not user:
        return {'error': 'user not found!'}
    if not verify_password(admin.password, user.hashed_password):
        return {'error': 'password incorrect'}
    return await signJWT(admin.username)

@router.post('/view',dependencies=[Depends(jwtBearer())])
async def view(admin: Admin):
    return {"hello!"}

@router.post('/refresh_token')
async def refresh(rt: RefreshToken) -> dict:
    user: dict = await decodeJWT(rt.refresh_token)
    return await signJWT(user['userID'])

@router.post('/new_teacher', dependencies=[Depends(jwtBearer())])
async def add_teacher(teacher: Teacher, db: Session = Depends(get_db)):
    return await crud.add_teacher(teacher, db)

@router.post('/new_group',dependencies=[Depends(jwtBearer())])
async def add_group(group: Group, db: Session = Depends(get_db)):
    return await crud.add_group(group, db)

@router.post('/new_shedule',dependencies=[Depends(jwtBearer())])
async def add_shedule(shedule: Shedule, db: Session = Depends(get_db)):
    return await crud.add_shedule(shedule, db)

