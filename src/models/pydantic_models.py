from database.db import Base
from sqlalchemy import Column, String, Integer, DateTime, BigInteger

#FIXME: convert id to uuid.
class Teachers(Base):
    __tablename__ = 'Teachers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    email = Column(String)


#FIXME: convert id to uuid.
#FIXME: add unique to username
class Admins(Base):
    __tablename__ = 'Admins'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    hashed_password = Column(String)


class Groups(Base):
    __tablename__ = 'Groups'

    id = Column(Integer, primary_key=True)
    short_name = Column(String)
    full_name = Column(String)


class Shedules(Base):
    __tablename__ = 'Shedules'

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, default=0)
    lesson_start = Column(Integer, default=0, nullable=False)
    name = Column(String)
    teacher_id = Column(Integer)
    dt = Column(BigInteger)

