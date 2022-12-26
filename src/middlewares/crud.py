# *0.__.0*. This is a space.... *.0.

from sqlalchemy.orm import Session
from models.pydantic_models import Teachers, Admins, Groups, Shedules
from models.abstact_models import Teacher, Group, Shedule
from typing import Union



# PUBLIC
async def get_teachers(db: Session) -> Union[Teachers, None]:
    try:
        record = db.query(Teachers).all()
        return record
    except Exception as ex:
        return {'error', ex}


async def get_groups(db: Session) -> Union[Groups, None]:
    try:
        record = db.query(Groups).all()
        return record
    except Exception as ex:
        return {'error', ex}


# ADMIN
#FIXME: remove {} from function to another file.
async def add_admin(username: str, hashed_password: str, db: Session) -> None:
    try:
        admin = Admins(
            username=username,
            hashed_password=hashed_password
        )
        db.add(admin)
        db.commit()
        return {'content': 'Done!'}
    except Exception as ex:
        return {'error': ex}

async def check_admin(username: str, db: Session) -> Admins:
    try:
        admin = db.query(Admins).filter(Admins.username == username).first()
        return admin
    except:
        return

async def add_teacher(teacher: Teacher, db: Session) -> dict:
    try:
        new_teacher = Teachers(
            first_name = teacher.first_name,
            middle_name = teacher.middle_name,
            last_name = teacher.last_name,
            email = teacher.email
        )

        db.add(new_teacher)
        db.commit()
        return {'content': 'Done!'}
    except Exception as ex:
        return {'error': ex}

async def add_group(group: Group, db: Session) -> dict:
    try:
        new_group = Groups(
            short_name = group.short_name,
            full_name = group.full_name
        )

        db.add(new_group)
        db.commit()
        return {'content': 'Done!'}
    except Exception as ex:
        return {'error': ex}

async def add_shedule(shedule: Shedule, db: Session) -> dict:
    try:
        new_shedule = Shedules(
            para_id = shedule.para_id,
            group_id = shedule.group_id
        )

        db.add(new_shedule)
        db.commit()
        return {'content': 'Done!'}
    except Exception as ex:
        return {'error': ex}