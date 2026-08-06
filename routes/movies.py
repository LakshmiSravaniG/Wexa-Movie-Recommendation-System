from flask import Blueprint, render_template, request
from services.movie_service import (
    fetch_all_movies,
    fetch_movie,
    search_movie
)

movie_bp = Blueprint("movies", __name__)


@movie_bp.route("/movies")
def movies():
    movies = fetch_all_movies()
    return render_template("movies.html", movies=movies)


@movie_bp.route("/movie/<int:movie_id>")
def movie_details(movie_id):
    movie = fetch_movie(movie_id)

    if movie is None:
        return render_template("error.html", message="Movie not found")

    return render_template("movie_details.html", movie=movie)


@movie_bp.route("/search")
def search():
    keyword = request.args.get("keyword", "")
    movies = search_movie(keyword)
    return render_template("movies.html", movies=movies)