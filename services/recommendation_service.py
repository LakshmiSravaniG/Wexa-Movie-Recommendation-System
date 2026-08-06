from database.queries import recommend_movies


def get_recommendations(user_id):
    """
    Return recommended movies for a user.
    """
    return recommend_movies(user_id)