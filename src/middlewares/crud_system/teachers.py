from sqlalchemy.orm import Session
from models.pydantic_models import Teachers
from models.abstract_models import TeacherInDB, Teacher
from middlewares.error_handler import error_handler
from typing import List

class TeacherController:
    async def get_teachers(self, db: Session) -> List[dict]:
        record = [teacher.__dict__ for teacher in db.query(Teachers).all()]
        return record
    
    async def get_teacher_by_name(self, db: Session, teacher_name: str) -> List[TeacherInDB]:
        record = [teacher.__dict__ for teacher in db.query(Teachers).filter(Teachers.first_name == teacher_name).all()]
        return record
    
    async def get_teacher_by_last_name(self, db: Session, teacher_last_name: str) -> List[TeacherInDB]:
        record = [teacher.__dict__ for teacher in db.query(Teachers).filter(Teachers.last_name == teacher_last_name).all()]
        return record
    
    async def get_teacher_by_id(self, db: Session, teacher_id: str) -> TeacherInDB:
        record = db.query(Teachers).filter(Teachers.id == teacher_id).one()
        response = TeacherInDB(
            id=record.id,
            first_name=record.first_name,
            last_name=record.last_name,
            middle_name=record.middle_name,
            email=record.email)
        return response
    
    async def add_teacher(self, db: Session, teacher: Teacher) -> List[Teacher]:
        new_teacher = Teachers(
            first_name = teacher.first_name,
            middle_name = teacher.middle_name,
            last_name = teacher.last_name,
            email = teacher.email
        )

        db.add(new_teacher)
        db.commit()
        return await self.get_teacher_by_last_name(db=db, teacher_last_name=teacher.last_name)

    async def edit_teacher(self, db: Session, teacher: Teacher, teacher_id: int) -> TeacherInDB:
        db.query(Teachers).filter(Teachers.id==teacher_id).update(teacher.dict())
        db.commit()
        return await self.get_teacher_by_id(teacher_id=teacher_id, db=db)
    
    async def delete_teacher(self, db: Session, teacher_id: int) -> None:
        db.query(Teachers).filter(Teachers.id==teacher_id).delete()
        db.commit()