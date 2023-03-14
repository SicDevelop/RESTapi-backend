from sqlalchemy.orm import Session
from models.pydantic_models import Teachers
from models.abstract_models import Teacher
from middlewares.error_handler import error_handler

class TeacherController:
    async def get_teachers(self, db: Session) -> dict:
        record = db.query(Teachers).all()
        return record
    
    async def get_teacher_by_name(self, db: Session, teacher_name: str) -> dict:
        record = db.query(Teachers).filter(Teachers.first_name == teacher_name).all()
        return record
    
    async def get_teacher_by_last_name(self, db: Session, teacher_last_name: str) -> dict:
        record = db.query(Teachers).filter(Teachers.last_name == teacher_last_name).all()
        return record
    
    async def get_teacher_by_id(self, db: Session, teacher_id: str) -> dict:
        record = db.query(Teachers).filter(Teachers.id == teacher_id).one()
        response = {'first_name': record.first_name, 'last_name': record.last_name, 'middle_name': record.middle_name}
        return response
    
    async def add_teacher(self, db: Session, teacher: Teacher) -> None:
        new_teacher = Teachers(
            first_name = teacher.first_name,
            middle_name = teacher.middle_name,
            last_name = teacher.last_name,
            email = teacher.email
        )
    
        db.add(new_teacher)
        db.commit()
