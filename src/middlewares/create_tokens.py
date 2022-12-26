
import time
import jwt
from core.config import server_settings


async def token_response(token: str, refresh_token):
    return {
        'access token': token, 'refresh_token': refresh_token
    }

async def signJWT(userID: str):
    payload = {
        'userID': userID,
        'exp': time.time() + 1200
    }
    token = jwt.encode(payload, server_settings.ACCESS_SECRET_KEY, algorithm='HS256')
    refresh = jwt.encode(payload, server_settings.REFRESH_SECRET_KEY, algorithm='HS256')
    return await token_response(token, refresh)

async def decodeJWT(token: str):
    try:
        try:
            decode_token = jwt.decode(token, server_settings.ACCESS_SECRET_KEY, algorithm='HS256')
            return decode_token if decode_token['exp'] >= time.time() else None
        except:
            decode_token = jwt.decode(token, server_settings.REFRESH_SECRET_KEY, algorithm='HS256')
            return decode_token if decode_token['exp'] >= time.time() else None
    except:
        return {}