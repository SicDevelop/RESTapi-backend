from fastapi import APIRouter, Depends
from database.db import get_db
from sqlalchemy.orm import Session
from middlewares.crud import CrudController
from middlewares.create_tokens import signJWT
from models.abstract_models import Admin
from core.security import get_password_hash, verify_password
from middlewares import responses
router = APIRouter(
    prefix='/public'
)

crud = CrudController()

@router.post('/login', tags=['Authorize'])
async def login(admin: Admin, db: Session = Depends(get_db)) -> dict:
    """ Авторизация для получения токенов """
    user: object = await crud.check_admin(username=admin.username, db=db)
    if not user:
        return responses.ERROR_RESPONSES['user_not_found']
    if not verify_password(admin.password, user.hashed_password):
        return responses.ERROR_RESPONSES['access_denied']
    return await signJWT(admin.username)


@router.post('/register', tags=['Authorize'])
async def register(admin: Admin, db: Session = Depends(get_db)) -> dict:
    """ Создание тестового админа. Временная функция. """
    hashed_password: str = get_password_hash(admin.password)
    await crud.add_admin(username=admin.username, hashed_password=hashed_password, db=db)
    return responses.OK_RESPONSES['admin_created']

# <================== Teachers =================>
@router.get('/teachers', tags=['Teachers'])
async def teachers(db: Session = Depends(get_db)):
    return await crud.get_teachers(db=db)

@router.get('/tacher-by-id', tags=['Teachers'])
async def teacher_by_id(teacher_id: int, db: Session = Depends(get_db)):
    return await crud.get_teacher_by_id(db=db, teacher_id=str(teacher_id))

@router.get('/teachers-by-name', tags=['Teachers'])
async def teachers_by_name(teacher_name: str, db: Session = Depends(get_db)):
    return await crud.get_teacher_by_name(db=db, teacher_name=teacher_name)

@router.get('/teachers-by-last-name', tags=['Teachers'])
async def teachers_by_last_name(teacher_last_name: str, db: Session = Depends(get_db)):
    return await crud.get_teacher_by_last_name(db=db, teacher_last_name=teacher_last_name)


# <================== Groups =================>
@router.get('/groups', tags=['Groups'])
async def groups(db: Session = Depends(get_db)):
    return await crud.get_groups(db=db)

@router.get('/group-by-id', tags=['Groups'])
async def group_by_id(group_id: int, db: Session = Depends(get_db)):
    return await crud.get_group_by_id(db=db, group_id=str(group_id))

@router.get('/groups-by-short-name', tags=['Groups'])
async def groups_by_short_name(group_short_name: str, db: Session = Depends(get_db)):
    return await crud.get_group_by_short_name(db=db, group_short_name=group_short_name)


# <================== Schedule =================>
@router.get('/schedules', tags=['Schedule'])
async def schedules(db: Session = Depends(get_db), today: bool = True):
    if today:
        return await crud.get_today_all_shedule(db=db)
    return await crud.get_tomorrow_all_shedule(db=db)

@router.get('/schedule-by-group-id', tags=['Schedule'])
async def schedule_by_group_id(group_id: int, db: Session = Depends(get_db), today: bool = True):
    if today:
        return await crud.get_today_shedule_by_group_id(db=db, group_id=str(group_id))
    return await crud.get_tomorrow_shedule_by_group_id(db=db, group_id=str(group_id))

@router.get('/schedule-by-teacher-id', tags=['Schedule'])
async def schedule_by_teacher_id(teacher_id: int, db: Session = Depends(get_db), today: bool = True):
    if today:
        return await crud.get_today_shedule_by_teacher_id(db=db, teacher_id=str(teacher_id))
    return await crud.get_tomorrow_shedule_by_teacher_id(db=db, teacher_id=str(teacher_id))

@router.get('/schedule-by-timestamp', tags=['Schedule'])
async def schedule_by_timestamp(timestamp: int, db: Session = Depends(get_db)):
    return {'Hello': 'World!'}
