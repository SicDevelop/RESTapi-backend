from sqlalchemy.orm import Session
from models.pydantic_models import Teachers, Admins, Groups, Shedules
from models.abstract_models import Teacher, Group, Shedule
from .error_handler import error_handler
from typing import Union
from middlewares.date_module import Today, Tomorrow

# ======================= TEACHERS =======================
@error_handler
async def get_teachers(db: Session) -> dict:
    record = db.query(Teachers).all()
    return record

@error_handler
async def get_teacher_by_name(db: Session, name: str) -> dict:
    record = db.query(Teachers).filter(Teachers.first_name == name).all()
    return record

@error_handler
async def get_teacher_by_last_name(db: Session, last_name: str) -> dict:
    record = db.query(Teachers).filter(Teachers.last_name == last_name).all()
    return record

async def get_teacher_by_id(db: Session, id: str) -> dict:
    record = db.query(Teachers).filter(Teachers.id == id).one()
    response = {'first_name': record.first_name, 'last_name': record.last_name, 'middle_name': record.middle_name}

# ======================= SHEDULE =======================
async def get_today_shedule_by_group_id(db: Session, group_id: str) -> dict:
    start = Today().get_start_day_timestamp()
    end = Today().get_end_day_timestamp()
    record = db.query(Shedules).filter(Shedules.group_id == group_id, Shedules.dt>start,Shedules.dt<end).all()
    return record

async def get_tomorrow_shedule_by_group_id(db: Session, group_id: str) -> dict:
    start = Tomorrow().get_tomorrow_start()
    end = Tomorrow().get_tomorrow_end()
    record = db.query(Shedules).filter(Shedules.group_id == group_id, Shedules.dt>start,Shedules.dt<end).all()
    return record

async def get_today_all_shedule(db: Session) -> dict:
    start = Today().get_start_day_timestamp()
    end = Today().get_end_day_timestamp()
    record = db.query(Shedules).filter(Shedules.dt>start, Shedules.dt<end).all()
    return record

async def get_tomorrow_all_shedule(db: Session) -> dict:
    start = Tomorrow().get_tomorrow_start()
    end = Tomorrow().get_tomorrow_end()
    record = db.query(Shedules).filter(Shedules.dt>start,Shedules.dt<end).all()
    return record

async def get_today_shedule_by_teacher_id(db: Session, teacher_id: int) -> dict:
    start = Today().get_start_day_timestamp()
    end = Today().get_end_day_timestamp()
    record = db.query(Shedules).filter(Shedules.teacher_id==teacher_id, Shedules.dt>start, Shedules.dt<end).all()
    return record

async def get_tomorrow_shedule_by_teacher_id(db: Session, teacher_id: int) -> dict:
    start = Tomorrow().get_tomorrow_start()
    end = Tomorrow().get_tomorrow_end()
    record = db.query(Shedules).filter(Shedules.teacher_id==teacher_id, Shedules.dt>start, Shedules.dt<end).all()
    return record

async def add_shedule(shedule_start: int, shedule_dt, lesson_name, group_id, teacher_id, db: Session) -> dict:

    shedule = Shedules(
        lesson_start = shedule_start, group_id = group_id,
        dt = int(shedule_dt), name = lesson_name, teacher_id = teacher_id
    )
    db.add(shedule)
    db.commit()


# ======================= GROUPS =======================
@error_handler
async def get_groups(db: Session) -> list:
    record = db.query(Groups).all()
    response = []
    for i in record:
        group = {'short_name': i.short_name, 'full_name': i.full_name}
        response.append(group)
    return response

@error_handler
async def get_group_by_short_name(db: Session, short_name) -> dict:
    record = db.query(Groups).one()
    response = {'short_name': record.short_name, 'full_name': record.full_name}
    return response

@error_handler
async def add_admin(username: str, hashed_password: str, db: Session) -> None:
    admin = Admins(
        username = username,
        hashed_password = hashed_password
    )

    db.add(admin)
    db.commit()

@error_handler
async def add_teacher(teacher: Teacher, db: Session) -> dict:
    new_teacher = Teachers(
        first_name = teacher.first_name,
        middle_name = teacher.middle_name,
        last_name = teacher.last_name,
        email = teacher.email
    )
    
    db.add(new_teacher)
    db.commit()

@error_handler
async def check_admin(username: str, db: Session) -> Admins:
    admin = db.query(Admins).filter(Admins.username == username).first()
    return admin

@error_handler
async def add_group(group: Group, db: Session) -> dict:
    new_group = Groups(
        short_name = group.short_name,
        full_name = group.full_name
    )

    db.add(new_group)
    db.commit()