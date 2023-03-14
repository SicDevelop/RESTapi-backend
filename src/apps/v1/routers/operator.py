from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.security import verify_password
from database.db import get_db
from middlewares.crud import CrudController
from middlewares import responses, utils
from middlewares.create_tokens import signJWT
from middlewares.jwt_bearer import jwtBearer
from models.abstract_models import Teacher, Admin, AdminInDB, RefreshToken, \
                                   Group, Schedule

crud = CrudController()

router = APIRouter(
    prefix='/private',
    dependencies=[Depends(jwtBearer())]
)


# <================== Teachers =================>
@router.post('/add-teacher', tags=['Teachers'])
async def add_teacher(teacher: Teacher, db: Session = Depends(get_db)):
    await crud.add_teacher(teacher=teacher, db=db)
    return {'done': 'qwe'}

@router.put('/edit-teacher', tags=['Teachers'])
async def edit_teacher(teacher: Teacher, teacher_id: int, db: Session = Depends(get_db)):
    return {'qwe': 'qwe'}

@router.delete('/delete_teacher', tags=['Teachers'])
async def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    return {'sfg': 'ewr'}

# <================== Groups  =================>
@router.post('/add-group', tags=['Groups'])
async def add_group(group: Group, db: Session = Depends(get_db)):
    await crud.add_group(db=db, group=group)
    return {'save': 'save'}

@router.put('/edit-group', tags=['Groups'])
async def edit_group(group: Group, group_id: int, db: Session = Depends(get_db)):
    return {'ssdf': 'sdf'}

@router.delete('/delete-group', tags=['Groups'])
async def delete_group(group_id: int, group: Group, db: Session = Depends(get_db)):
    return {'qwe': 'qwe'}

# <================== Schedules =================>
@router.post('/add-schedule', tags=['Schedule'])
async def add_schedule(group_id: int, schedule: Schedule, db: Session = Depends(get_db)):
    await crud.add_schedule(schedule=schedule, group_id=group_id, db=db)
    return {'save': 'save'}

@router.put('/edit-schedule', tags=['Schedule'])
async def edit_schedule(schedule: Schedule, schedule_id: int, db: Session = Depends(get_db)):
    return {'qwe': 'qwe'}

@router.delete('/edit-schedule', tags=['Schedule'])
async def delete_schedule(schedule_id: int, db: Session = Depends(get_db)):
    return {'qwe': 'qwe'}