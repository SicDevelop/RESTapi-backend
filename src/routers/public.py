from fastapi import APIRouter, Depends
from database.db import get_db
from sqlalchemy.orm import Session
from middlewares import crud, responses
from middlewares.create_tokens import signJWT
from models.abstract_models import Admin
from core.security import get_password_hash, verify_password

router = APIRouter(
    prefix = '/api/v1/public',
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


@router.post('/register')
async def register(admin: Admin, db: Session = Depends(get_db)) -> dict:
    """ Создание тестового админа. Временная функция. """
    hashed_password: str = get_password_hash(admin.password)
    await crud.add_admin(username=admin.username, hashed_password=hashed_password, db=db)
    return responses.OK_RESPONSES['admin_created']

# ======================= TEACHERS =======================
@router.get('/teacher-by-name')
async def get_teacher_by_name(name: str, db: Session = Depends(get_db)):
    return await crud.get_teacher_by_name(db=db, name=name)

@router.get('/teacher-by-last-name')
async def get_teacher_by_last_name(last_name: str, db: Session = Depends(get_db)):
    return await crud.get_teacher_by_last_name(db=db, last_name=last_name)

@router.get('/teachers')
async def get_teachers(db: Session = Depends(get_db)) -> list:
    """ Получение списка преподавателей """
    return await crud.get_teachers(db=db)

# ======================= GROUPS =======================
@router.get('/groups')
async def get_groups(db: Session = Depends(get_db)) -> list:
    """ Получение списка групп """
    return await crud.get_groups(db=db)

@router.get('/group-by-short-name')
async def get_group_by_short_name(short_name: str, db: Session = Depends(get_db)) -> dict:
    return await crud.get_group_by_short_name(short_name=short_name, db=db)

# ======================= SHEDULE =======================
@router.get('/shedule-by-group-id')
async def get_shedule_by_group(group_id: int, db: Session = Depends(get_db), today: bool=True) -> list:
    """ Получение расписания по группе в QueryParams """
    if today is True:
        return await crud.get_today_shedule_by_group_id(db=db, group_id=group_id)
    else:
        return await crud.get_tomorrow_shedule_by_group_id(db=db, group_id=group_id)

@router.get('/shedule')
async def get_shedule(db: Session = Depends(get_db), today: bool = True) -> list:
    """ Получение расписания всех групп """
    if today is True:
        return await crud.get_today_all_shedule(db=db)
    else:
        return await crud.get_tomorrow_all_shedule(db=db)

@router.get('/shedule-by-teacher')
async def get_shedule_by_teacher_id(teacher_id: int, db: Session = Depends(get_db), today: bool = True) -> list:
    """ Получение расписания по ID преподавателя """
    if today is True:
        return await crud.get_today_shedule_by_teacher_id(db=db, teacher_id=teacher_id)
    else:
        return await crud.get_tomorrow_shedule_by_teacher_id(db=db, teacher_id=teacher_id)
 

@router.get('/update-avaliable')
async def update_is() -> dict:
    """ Проверка на то, обновил-ли расписание диспетчер """
    return {'Hello': 'World!'}

