from fastapi import APIRouter
from fastapi import Path, Depends
from fastapi.responses import JSONResponse
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from config.database import Session
from services.movie import MovieService
from schemas.movie import Movie

MovieRouter = APIRouter()

@MovieRouter.get('/movies', tags=['movies'], dependencies=[Depends(JWTBearer())])
def getMovies():
    db = Session()
    result = MovieService(db).getMovies()
    return JSONResponse(content = jsonable_encoder(result))
@MovieRouter.get('/movies/{id}', tags=['movies'])
def getMovie(id: int = Path(ge=1, le=2000))->Movie:
    db = Session()
    result = MovieService(db).getMovie(id)
    if not result:
        JSONResponse(status_code=404, content={"message":"Not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
@MovieRouter.get('/movies/', tags=['movies'])
def searchMovie(category: str):
    db = Session()
    result = MovieService(db).getMovieByCategory(category)
    if not result:
        JSONResponse(status_code=404, content={"message":"Not found"})
    return JSONResponse(content=jsonable_encoder(result))
@MovieRouter.post('/movies/', tags=['movies'])
def createMovie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).createMovie(movie)
    return JSONResponse(content={"message":"The movie has been aded"})
@MovieRouter.put('/movies/{id}', tags=['movies'])
def updateMovie(id: int, movie: Movie):
    db = Session()
    existing_movie = MovieService(db).getMovie(id)
    if not existing_movie:
        return JSONResponse(status_code=404, content={"message": "Not found"})
    MovieService(db).updateMovie(id, movie)
    return JSONResponse(content={"message": "The movie has been updated"})



@MovieRouter.delete('/movies/{id}', tags=['movies'])
def deleteMovie(id: int):
    db = Session()
    movie = MovieService(db).getMovie(id)
    if not movie:
        return JSONResponse(status_code=404, content={"message": "Not found"})
    MovieService(db).deleteMovie(movie)
    return JSONResponse(content={"message": "The movie has been deleted"})