from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    year: int
    genre: str
    read: bool = False

class Movie(BaseModel):
    title: str
    director: str
    year: int
    genre: str
    watched: bool = False

# class Show(BaseModel):
#     title: str
#     creator: str
#     year: int
#     genre: str
#     Season: int
#     is_watched: bool = False