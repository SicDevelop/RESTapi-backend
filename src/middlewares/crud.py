from sqlalchemy.orm import Session
from models.pydantic_models import Teachers, Admins, Groups, Shedules
from models.abstract_models import Teacher, Group, Shedule
from .error_handler import error_handler
from typing import Union

@error_handler
async def get_teachers(db: Session) -> Union[Teachers, None]:
    record = db.query(Teachers).all()
    return record

@error_handler
async def get_groups(db: Session) -> Union[Groups, None]:
    record = db.query(Groups).all()
    return record

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

@error_handler
async def add_shedule(shedule: Shedule, db: Session) -> dict:
    new_shedule = Shedules(**shedule)
    
    db.add(new_shedule)
    db.commit()

