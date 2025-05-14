from pydantic import BaseModel
from datetime import datetime

class Book(BaseModel):
    title: str
    author: str
    year: int
    genre: str
    read: bool = False

class ArchivedBook(BaseModel):
    title: str
    author: str
    archived_at: datetime

# class Movie(BaseModel):
#     title: str
#     director: str
#     year: int
#     genre: str
#     watched: bool = False

# class Show(BaseModel):
#     title: str
#     creator: str
#     year: int
#     genre: str
#     Season: int
#     is_watched: bool = False