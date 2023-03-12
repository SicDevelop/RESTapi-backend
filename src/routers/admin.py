from fastapi import APIRouter, Depends
from core.security import verify_password
from database.db import get_db
from sqlalchemy.orm import Session
from middlewares import crud, responses, utils
from middlewares.create_tokens import signJWT
from middlewares.jwt_bearer import jwtBearer
from models.abstract_models import Teacher, Admin, \
                                   AdminInDB, RefreshToken, \
                                   Group, Shedule

router = APIRouter(
    prefix = '/api/v1/admin',
    tags = ['Api for admin'],
    dependencies=[Depends(jwtBearer())],
    responses={404: {"description": "Not found"}},
)

# ==== TEACHERS ====>
@router.post('/add-teacher')
async def add_teacher(teacher: Teacher, db: Session = Depends(get_db)) -> dict:
    await crud.add_teacher(teacher, db=db)
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
async def add_shedule(group_id: int, shedule: Shedule, db:Session=Depends(get_db)) -> dict:
    group_name: str = shedule.name
    shedule = shedule.dict()
    dt = int(shedule['lessons']['dt'])
    del shedule['lessons']['dt']
    for i in shedule['lessons'].keys():
        try:
            name = shedule['lessons'][i]['name']
            if name != "string":
                teacher = shedule['lessons'][i]['teacher']
                shedule_start = utils.chooser(i)
                await crud.add_shedule(group_id=group_id, shedule_start=shedule_start, shedule_dt=dt, lesson_name=name, teacher_id=teacher, db=db)
        except Exception as ex:
            print(ex)
    
    return {"status": "done!"}

@router.post('/edit-shedule')
async def edit_shedule(group_id: int, shedule: Shedule) -> dict:
    return {'Hello': 'World!'}

"""
{
  "name": "3пр1",
  "lessons": {
    "zero": {
      "name": "МДК 01.01",
      "teacher": "Антипин"
    },
    "one": {
      "name": "МДК 01.02",
      "teacher": "Михайлов"
    },
    "two": {
      "name": "МДК 01.03",
      "teacher": "Дагестан"
    },
    "three": {
      "name": "МДК 01.04",
      "teacher": "Япония"
    },
    "four": {
      "name": "string",
      "teacher": "string"
    },
    "five": {
      "name": "string",
      "teacher": "string"
    },
    "size": {
      "name": "string",
      "teacher": "string"
    },
    "dt": "string"
  }
}
"""