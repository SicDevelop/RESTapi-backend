import time
import jwt
from core.config import server_settings
from models.abstract_models import Tokens

async def token_response(token: str, refresh_token: str) -> Tokens:
    return Tokens(access_token=token, refresh_token=refresh_token)

async def signJWT(user_id: str) -> dict:
    payload_access: dict = {
        'userID': user_id,
        'exp': time.time() + (int(server_settings.ACCESS_EXPIRE_MINUTES) * 60) * 1000
    }

    payload_refresh: dict = {
        'userID': user_id,
        'exp': time.time() + (int(server_settings.REFRESH_EXPIRE_MINUTES) * 60) * 1000
    }

    token: str = jwt.encode(payload_access, server_settings.ACCESS_SECRET_KEY, algorithm='HS256')
    refresh: str = jwt.encode(payload_refresh, server_settings.REFRESH_SECRET_KEY, algorithm='HS256')
    return await token_response(token=token, refresh_token=refresh)

async def decodeJWT(token: str) -> dict:
    try:
        try:
            decode_token: dict = jwt.decode(token, server_settings.ACCESS_SECRET_KEY, algorithm='HS256')
        except:
            decode_token: dict = jwt.decode(token, server_settings.REFRESH_SECRET_KEY, algorithm='HS256')
        return decode_token if decode_token['exp'] >= time.time() else None
    except:
        return {}
