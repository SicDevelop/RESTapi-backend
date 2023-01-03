# All configuration variables from environment here.
# -._._.-._._.-._._.-._._-._._.-._._._->

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class DatabaseSettings(BaseSettings):
    DB_HOST: str
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str

class ServerSettings(BaseSettings):
    ACCESS_SECRET_KEY: str
    REFRESH_SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_MINUTES: int

db_settings = DatabaseSettings()
server_settings = ServerSettings()
