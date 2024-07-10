from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import MovieRouter
from routers.user import UserRouter
app = FastAPI()
app.add_middleware(ErrorHandler)
app.include_router(MovieRouter)
app.include_router(UserRouter)
app.title = "FirstApp"

Base.metadata.create_all(bind=engine)


