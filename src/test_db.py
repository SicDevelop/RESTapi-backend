from models.pydantic_models import *
from database.db import get_db

k = get_db()
print(k)
