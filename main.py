from fastapi import FastAPI
from routers import books, movies

app = FastAPI()
app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(movies.router, prefix="/movies", tags=["movies"])

@app.get("/")
def read_root():
    return {"message": "Welcome to ToBeConsumed!"}
