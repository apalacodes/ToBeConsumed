from fastapi import FastAPI , Request
from routers import books 

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="ToBeConsumed",
    description="A simple app to track books, movies, and shows you want to consume.",
    version="1.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

# --------------------------------------------

app.include_router(books.router, prefix="/books", tags=["books"])
# app.include_router(movies.router, prefix="/movies", tags=["movies"])

@app.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    return templates.TemplateResponse("landing.html", {"request": request})

@app.get("/index", response_class=HTMLResponse)
async def landing(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/to_be_read", response_class=HTMLResponse)
async def to_be_read_page(request: Request):
    return templates.TemplateResponse("to_be_read.html", {"request": request})

@app.get("/to_be_read", response_class=HTMLResponse)
async def to_be_read_page(request: Request):
    return templates.TemplateResponse("to_be_read.html", {"request": request, "books": books})

# @app.get("/to_be_watched", response_class=HTMLResponse)
# async def to_be_watched_page(request: Request):
#     return templates.TemplateResponse("to_be_watched.html", {"request": request, "movies": movies})
