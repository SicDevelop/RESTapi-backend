from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from middlewares.create_tokens import decodeJWT

class jwtBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(jwtBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials = await super(jwtBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == 'Bearer':
                raise HTTPException(status_code=403, details='Invalid of Expired token')
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, details='Invalid of Expired token')
    
    def verify_jwt(self, token):
        isTokenValid = False
        payload = decodeJWT(token)
        if payload:
            isTokenValid = True
        return isTokenValid
