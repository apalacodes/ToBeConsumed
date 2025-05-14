
from fastapi import APIRouter, HTTPException , Request
from schemas import Book
from typing import List

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter()
books = []

@router.get("/api/books", response_model=List[Book])
def get_books():
    return books

@router.post("/api/books")
def add_book(book: Book):
    books.append(book)
    return book

@router.put("/api/books/{title}")
def mark_as_read(title: str):
    for book in books:
        if book.title.lower() == title.lower():
            book.read = True  
            return {"message": "Book marked as read"}
    raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/api/books/{title}")
def delete_book(title: str):
    for i, book in enumerate(books):
        if book.title.lower() == title.lower():
            del books[i]
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")

@router.get("/to_be_read", response_class=HTMLResponse)
async def to_be_read_page(request: Request):
    return templates.TemplateResponse("to_be_read.html", {
        "request": request,
        "books": books
    })