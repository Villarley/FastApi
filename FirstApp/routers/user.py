from fastapi import APIRouter
from fastapi.responses import JSONResponse
from jwtManager import CreateToken
from schemas.user import User


UserRouter = APIRouter()
@UserRouter.post("/login", tags=['Auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "123":
        token: str = CreateToken(user.dict())
        return JSONResponse(content=token)