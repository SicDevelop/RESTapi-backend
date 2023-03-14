from sqlalchemy.orm import Session
from models.pydantic_models import Admins

class AdminController:
    async def check_admin(self, db: Session, username: str) -> Admins:
        admin = db.query(Admins).filter(Admins.username == username).first()
        return admin
    
    async def add_admin(self, db: Session, hashed_password: str, username: str):
        admin = Admins(
            username=username,
            hashed_password=hashed_password
        )
        db.add(admin)
        db.commit()
