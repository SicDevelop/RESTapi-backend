from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from middlewares.create_tokens import decodeJWT

class jwtBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True) -> None:
        super(jwtBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> dict:
        credentials: object = await super(jwtBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == 'Bearer':
                raise HTTPException(status_code=403, details='Invalid or expired token.')
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, details='Invalid or expired_token.')

    def verify_jwt(self, token: str) -> bool:
        payload: dict = decodeJWT(token)
        if payload:
            return True
        return False
