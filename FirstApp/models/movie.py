from config.database import Base
from sqlalchemy import Column, Integer, String, Float
class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    Title = Column(String)
    Overview = Column(String)
    Year = Column(Integer)
    Rating = Column(Float)
    Category = Column(String)