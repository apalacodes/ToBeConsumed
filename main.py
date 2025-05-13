from fastapi import FastAPI , Request
from routers import books, movies

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="ToBeConsumed",
    description="A simple app to track books, movies, and shows you want to consume.",
    version="1.0"
)
# -------------------new-------------------
# Mount static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")

# --------------------------------------------

app.include_router(books.router, prefix="/books", tags=["books"])
# app.include_router(movies.router, prefix="/movies")

# @app.get("/api/welcome")
# def read_welcome():
#     return {"message": "Welcome to ToBeConsumed!"}

# Landing page route
@app.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    return templates.TemplateResponse("landing.html", {"request": request})

@app.get("/index", response_class=HTMLResponse)
async def landing(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
