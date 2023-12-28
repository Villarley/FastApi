from models.movie import Movie as MovieModel
from schemas.movie import Movie
class MovieService():
    def __init__(self, db) -> None:
        self.db =db
    def getMovies(self):
        result = self.db.query(MovieModel).all()
        return result
    def getMovie(self, id:int):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result
    def getMovieByCategory(self, category:str):
        result = self.db.query(MovieModel).filter(MovieModel.category == category).first()
        return result
    def createMovie(self, movie: Movie):
        newMovie = MovieModel(**movie.dict())
        self.db.add(newMovie)
        self.db.commit()
    def updateMovie(self, id:int, movie:Movie):
        existingMovie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        existingMovie.Title = movie.Title
        existingMovie.Overview = movie.Overview
        existingMovie.Year = movie.Year
        existingMovie.Rating = movie.Rating
        existingMovie.Category = movie.Category
        self.db.commit()
    def deleteMovie(self, movie: Movie):
        self.db.delete(movie)
        self.db.commit()
        