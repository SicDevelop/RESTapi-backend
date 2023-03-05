from pydantic import BaseSettings
try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    print('Cannot load dotenv')

class DatabaseSettings(BaseSettings):
    DB_HOST: str
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str


class ServerSettings(BaseSettings):
    ACCESS_SECRET_KEY: str
    REFRESH_SECRET_KEY: str
    ACCESS_EXPIRE_MINUTES: str
    REFRESH_EXPIRE_MINUTES: str

db_settings = DatabaseSettings()
server_settings = ServerSettings()
