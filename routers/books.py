
from fastapi import APIRouter, HTTPException
from schemas import Book

router= APIRouter()

bookl=[]

@router.get("/")
def get_book():
    return bookl

@router.post("/")
def add_book(book: Book):
    bookl.append(book)
    return book

@router.get("/{title}")
def get_book(title: str):
    for book in bookl:
        if book.title.lower() == title.lower():
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# from fastapi import APIRouter, HTTPException
# from schemas import Book

# router = APIRouter()

# book_list = []

# @router.get("/")
# def get_books():
#     return [
#         {
#             "title": book.title,
#             "author": book.author,
#             "status": "Read" if book.read else "To be read"
#         }
#         for book in book_list
#     ]

# @router.post("/")
# def add_book(book: Book):
#     for b in book_list:
#         if b.title.lower() == book.title.lower():
#             raise HTTPException(status_code=400, detail="Book already in the list.")
#     book_list.append(book)
#     return {"message": "Book added to the list", "book": book}

# @router.get("/{title}")
# def get_book(title: str):
#     for book in book_list:
#         if book.title.lower() == title.lower():
#             return {
#                 "title": book.title,
#                 "author": book.author,
#                 "status": "Read" if book.read else "To be read"
#             }
#     raise HTTPException(status_code=404, detail="Book not found")

# @router.delete("/{title}")
# def remove_book(title: str):
#     for i, book in enumerate(book_list):
#         if book.title.lower() == title.lower():
#             removed = book_list.pop(i)
#             return {"message": "Book removed from the list", "book": removed}
#     raise HTTPException(status_code=404, detail="Book not found")