from pydantic import BaseModel, Field
class Movie(BaseModel):
    # id: Optional[int] = None
    Title:str = Field(min_length=5, max_length=15)
    Overview: str = Field(min_length=5, max_length=100)
    Year: int = Field(le=2022)
    Rating: float = Field(ge=1, le=10)
    Category: str = Field(min_length=5, max_length=100)