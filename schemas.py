from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    year: int
    genre: str
    is_read: bool = False

class Movie(BaseModel):
    title: str
    director: str
    year: int
    genre: str
    is_watched: bool = False

class Show(BaseModel):
    title: str
    creator: str
    year: int
    genre: str
    Season: int
    is_watched: bool = False