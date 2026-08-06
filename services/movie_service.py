from database.queries import (
    get_all_movies,
    get_movie_by_id,
    search_movies
)


def fetch_all_movies():
    """
    Return all movies.
    """
    return get_all_movies()


def fetch_movie(movie_id):
    """
    Return a single movie by ID.
    """
    return get_movie_by_id(movie_id)


def search_movie(keyword):
    """
    Search movies by title.
    """
    return search_movies(keyword)