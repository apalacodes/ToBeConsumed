# from fastapi import APIRouter, HTTPException
# from schemas import Movie

# router = APIRouter()
# movies = []

# @router.get("/")
# def get_movies():
#     return movies

# @router.post("/")
# def add_movie(movie: Movie):
#     movies.append(movie)
#     return movie

# @router.get("/{title}")
# def get_movie(title: str):
#     for movie in movies:
#         if movie.title.lower() == title.lower():
#             return movie
#     raise HTTPException(status_code=404, detail="Movie not found")


