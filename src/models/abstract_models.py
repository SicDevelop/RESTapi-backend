# Okay. This is podium..
# $-<>-$-<>-$-<>-$-<>-$-<>-$
from pydantic import BaseModel
from typing import Union

from sqlalchemy import DateTime

class Teacher(BaseModel):
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    middle_name: Union[str, None] = None
    email: Union[str, None] = None


class Admin(BaseModel):
    username: Union[str, None] = None
    password: str


class AdminInDB(BaseModel):
    username: Union[str, None] = None
    hashed_password: Union[str, None] = None


class RefreshToken(BaseModel):
    refresh_token: str


class Group(BaseModel):
    short_name: str
    full_name: str

class AboutLesson(BaseModel):
    name: str
    teacher: str

class Lessons(BaseModel):
    zero: AboutLesson
    one: AboutLesson
    two: AboutLesson
    three: AboutLesson
    four: AboutLesson
    five: AboutLesson
    size: AboutLesson
    dt: str

class Shedule(BaseModel):
    name: str
    lessons: Lessons
