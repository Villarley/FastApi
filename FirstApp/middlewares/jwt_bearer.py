from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from jwtManager import CreateToken, ValidateToken

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        print(auth.credentials)
        data = ValidateToken(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Unauthorized")