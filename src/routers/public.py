from fastapi import APIRouter, Depends
from database.db import get_db
from sqlalchemy.orm import Session
from middlewares import crud, responses
from middlewares.create_tokens import signJWT
from models.abstract_models import Admin
from core.security import get_password_hash, verify_password

router = APIRouter(
    prefix = '/api',
    tags = ['Public router']
)

@router.post('/login')
async def login(admin: Admin, db: Session = Depends(get_db)) -> dict:
    """ Авторизация для получения токенов """
    user: object = await crud.check_admin(username=admin.username, db=db)
    if not user:
        return responses.ERROR_RESPONSES['user_not_found']
    if not verify_password(admin.password, user.hashed_password):
        return responses.ERROR_RESPONSES['access_denied']
    return await signJWT(admin.username)

# REMOVE AT PROD.
@router.post('/register')
async def register(admin: Admin, db: Session = Depends(get_db)) -> dict:
    """ Создание тестового админа. Временная функция. """
    hashed_password: str = get_password_hash(admin.password)
    await crud.add_admin(username=admin.username, hashed_password=hashed_password, db=db)
    return {'done': 'status'}

@router.get('/teachers')
async def get_teachers(db: Session = Depends(get_db)) -> dict:
    """ Получение списка преподавателей """
    return await crud.get_teachers(db=db)

@router.get('/groups')
async def get_groups(db: Session = Depends(get_db)) -> dict:
    """ Получение списка групп """
    return await crud.get_groups(db=db)

@router.get('/shedule-by-group')
async def get_shedule_by_group(db: Session = Depends(get_db)) -> dict:
    """ Получение расписания по группе в QueryParams """
    return {'Hello': 'World!'}

@router.get('/shedule')
async def get_shedule(db: Session = Depends(get_db)) -> dict:
    """ Получение расписания всех групп """
    return {'Hello': 'World!'}

@router.get('/shedule-by-teacher')
async def get_shedule_by_teacher(db: Session = Depends(get_db)) -> dict:
    """ Получение расписания по фамилии преподавателя """
    return {'Hello': 'World!'}
 
@router.get('/update-avaliable')
async def update_is() -> dict:
    """ Проверка на то, обновил-ли расписание диспетчер """
    return {'Hello': 'World!'}

