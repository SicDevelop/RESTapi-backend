
import time
import jwt
from core.config import server_settings


async def token_response(token: str, refresh_token) -> dict:
    return {
        'access token': token, 'refresh_token': refresh_token
    }

async def signJWT(userID: str) -> dict:
    payload_access = {
        'userID': userID,
        'exp': time.time() + (server_settings.ACCESS_SECRET_KEY * 60) * 1000
    }
    payload_refresh = {
        'userID': userID,
        'exp': time.time() + (server_settings.REFRESH_SECRET_KEY * 60) * 1000
    }
    token = jwt.encode(payload_access, server_settings.ACCESS_SECRET_KEY, algorithm='HS256')
    refresh = jwt.encode(payload_refresh, server_settings.REFRESH_SECRET_KEY, algorithm='HS256')
    return await token_response(token, refresh)

async def decodeJWT(token: str) -> dict:
    try:
        try:
            decode_token = jwt.decode(token, server_settings.ACCESS_SECRET_KEY, algorithm='HS256')
            return decode_token if decode_token['exp'] >= time.time() else None
        except:
            decode_token = jwt.decode(token, server_settings.REFRESH_SECRET_KEY, algorithm='HS256')
            return decode_token if decode_token['exp'] >= time.time() else None
    except:
        return {}