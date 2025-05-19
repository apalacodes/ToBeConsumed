from fastapi import APIRouter
from schemas import ArchivedBook
from typing import List

router = APIRouter()
archived_books: List[ArchivedBook] = []

@router.get("/api/books")
def get_archived_books():
    return archived_books

@router.post("/api/books")
def add_archived_book(book: ArchivedBook):
    archived_books.append(book)
    return book