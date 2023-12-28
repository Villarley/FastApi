from fastapi import FastAPI, Body, Path, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional
from jwtManager import CreateToken, ValidateToken
from fastapi.security import HTTPBearer
app = FastAPI()

app.title = "FirstApp"

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        print(auth.credentials)
        data = ValidateToken(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Unauthorized")
class User(BaseModel):
    email:str
    password:str
class Movie(BaseModel):
    id: Optional[int] = None
    Title:str = Field(min_length=5, max_length=15)
    Overview: str = Field(min_length=50, max_length=100)
    Year: int = Field(le=2022)
    Rating: float = Field(ge=1, le=10)
    Category: str = Field(min_length=50, max_length=100)
movies = [
    {
        "id": 1,
        "Title": "Avatar",
        "Overview": "ajkflhdljhkjshgfgdhj",
        "Year": 2023,
        "Rating": 7.8,
        "Category": "Action",
    },
    {
        "id": 2,
        "Title": "Avatar",
        "Overview": "ajkflhdljhkjshgfgdhj",
        "Year": 2022,
        "Rating": 7.8,
        "Category": "Fiction",
    },
    {
        "id": 3,
        "Title": "Avatar",
        "Overview": "ajkflhdljhkjshgfgdhj",
        "Year": 2021,
        "Rating": 7.8,
        "Category": "Comedia",
    },
    {
        "id": 4,
        "Title": "Avatar",
        "Overview": "ajkflhdljhkjshgfgdhj",
        "Year": 2024,
        "Rating": 7.8,
        "Category": "Romance",
    },
]
@app.post("/login", tags=['Auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "123":
        token: str = CreateToken(user.dict())
        return JSONResponse(content=token)
@app.get('/')
def message():
    return HTMLResponse("<h1>Hello world</h1>")
@app.get('/movies', tags=['movies'], dependencies=[Depends(JWTBearer())])
def getMovies():
    return JSONResponse(content = movies)
@app.get('/movies/{id}', tags=['movies'])
def getMovie(id: int = Path(ge=1, le=2000)):
    for movie in movies:
        if movie["id"] == id:
            return JSONResponse(content=movie)
    return []
@app.get('/movies/', tags=['movies'])
def searchMovie(category: str, year:int):
    for movie in movies:
        if movie["Category"] == category and movie["Year"] == year:
            return movie
    return []
@app.post('/movies/', tags=['movies'])
def createMovie(movie: Movie):
    movies.append(movie)
    return movies[len(movies)-1]
@app.put('/movies/{id}', tags=['movies'])
def updateMovie(id: int, movie: Movie):
    for movie in movies:
        if movie["id"] == id:
            movie["Title"] = movie.Title
            movie["Overview"] = movie.Overview
            movie["Year"] = movie.Year
            movie["Rating"] = movie.Rating
            movie["Category"] = movie.Category
            return movie

@app.delete('/movies/{id}', tags=['movies'])
def deleteMovie(id: int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
        return movies
    return []

