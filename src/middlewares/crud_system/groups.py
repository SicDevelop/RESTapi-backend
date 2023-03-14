from sqlalchemy.orm import Session
from models.pydantic_models import Groups
from models.abstract_models import Group
from middlewares.error_handler import error_handler

class GroupsController:
    async def get_groups(self, db: Session) -> dict:
        record = db.query(Groups).all()
        return record
    
    async def get_group_by_short_name(self, db: Session, short_name: str) -> dict:
        record = db.query(Groups).one()
        response = {'short_name': record.short_name, 'full_name': record.full_name}
        return response
    
    async def get_group_by_id(self, db: Session, group_id: str) -> dict:
        record = db.query(Groups).filter(Groups.id == group_id).one()
        response = {'short_name': record.short_name, 'full_name': record.full_name}
        return response
    
    async def add_group(self, group: Group, db: Session) -> None:
        new_group = Groups(
            short_name = group.short_name,
            full_name = group.full_name
        )

        db.add(new_group)
        db.commit()
        print('saved')


        