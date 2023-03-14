from sqlalchemy.orm import Session
from models.pydantic_models import Shedules
from models.abstract_models import Schedule
from middlewares.error_handler import error_handler
from middlewares.date_module import Today, Tomorrow


class TodayScheduleController:
    async def get_today_shedule_by_group_id(self, db: Session, group_id: str) -> dict:
        start = Today().get_start_day_timestamp()
        end = Today().get_end_day_timestamp()
        record = db.query(Shedules).filter(Shedules.group_id == group_id, Shedules.dt>start,Shedules.dt<end).all()
        return record

    async def get_today_all_shedule(self, db: Session) -> dict:
        start = Today().get_start_day_timestamp()
        end = Today().get_end_day_timestamp()
        record = db.query(Shedules).filter(Shedules.dt>start, Shedules.dt<end).all()
        return record

    async def get_today_shedule_by_teacher_id(self, db: Session, teacher_id: int) -> dict:
        start = Today().get_start_day_timestamp()
        end = Today().get_end_day_timestamp()
        record = db.query(Shedules).filter(Shedules.teacher_id==teacher_id, Shedules.dt>start, Shedules.dt<end).all()
        return record
    

class TomorrowScheduleController:
    async def get_tomorrow_shedule_by_group_id(self, db: Session, group_id: str) -> dict:
        start = Tomorrow().get_tomorrow_start()
        end = Tomorrow().get_tomorrow_end()
        record = db.query(Shedules).filter(Shedules.group_id == group_id, Shedules.dt>start,Shedules.dt<end).all()
        return record
    
    async def get_tomorrow_all_shedule(self, db: Session) -> dict:
        start = Tomorrow().get_tomorrow_start()
        end = Tomorrow().get_tomorrow_end()
        record = db.query(Shedules).filter(Shedules.dt>start,Shedules.dt<end).all()
        return record

    async def get_tomorrow_shedule_by_teacher_id(self, db: Session, teacher_id: int) -> dict:
        start = Tomorrow().get_tomorrow_start()
        end = Tomorrow().get_tomorrow_end()
        record = db.query(Shedules).filter(Shedules.teacher_id==teacher_id, Shedules.dt>start, Shedules.dt<end).all()
        return record


class ScheduleController(TodayScheduleController, TomorrowScheduleController):
    async def add_shedule(self, shedule_start: int, shedule_dt: int, lesson_name: str, group_id: int, teacher_id: int, db: Session) -> dict:
        shedule = Shedules(
            lesson_start = shedule_start, group_id = group_id,
            dt = int(shedule_dt), name = lesson_name, teacher_id = teacher_id
        )
        db.add(shedule)
        db.commit()