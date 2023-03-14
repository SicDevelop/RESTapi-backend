from collections.abc import Generator
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import db_settings

DATABASE_URL: str = f'postgresql://{db_settings.DB_USERNAME}:{db_settings.DB_PASSWORD}@db/{db_settings.DB_NAME}'
engine: object = create_engine(DATABASE_URL)
session_local: object = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: object = declarative_base()

def get_db() -> Generator:
    database: object = session_local()
    try:
        yield database
    finally:
        database.close()
