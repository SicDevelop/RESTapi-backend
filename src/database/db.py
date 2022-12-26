# Database creator. I call him 'F*cking Asyncronius Monster'.
# !BE***!CAREFUL!****!(FAM)!****!LUFERAC!***BE!

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL: str = f'postgresql://test:test@localhost/testbase'
engine: object = create_engine(DATABASE_URL)
session_local: object = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: object = declarative_base()

#FIXME: add return type.
def get_db():
    database: object = session_local()
    try:
        yield database
    finally:
        database.close()
