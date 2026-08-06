from database.graph import graph


# -------------------------------
# Get All Movies
# -------------------------------
def get_all_movies():

    query = """
    MATCH (m:Movie)
    RETURN
        m.movieId AS movieId,
        m.title AS title,
        m.year AS year,
        m.genre AS genre
    ORDER BY title
    """

    return graph.execute_query(query)


# -------------------------------
# Get Movie By ID
# -------------------------------
def get_movie_by_id(movie_id):

    query = """
    MATCH (m:Movie {movieId:$movie_id})
    RETURN
        m.movieId AS movieId,
        m.title AS title,
        m.year AS year,
        m.genre AS genre
    """

    data = graph.execute_query(
        query,
        {"movie_id": movie_id}
    )

    if data:
        return data[0]

    return None


# -------------------------------
# Search Movies
# -------------------------------
def search_movies(keyword):

    query = """
    MATCH (m:Movie)
    WHERE toLower(m.title)
          CONTAINS
          toLower($keyword)

    RETURN
        m.movieId AS movieId,
        m.title AS title,
        m.year AS year,
        m.genre AS genre
    ORDER BY title
    """

    return graph.execute_query(
        query,
        {"keyword": keyword}
    )


# -------------------------------
# Get All Users
# -------------------------------
def get_all_users():

    query = """
    MATCH (u:User)
    RETURN
        u.userId AS userId,
        u.name AS name
    ORDER BY name
    """

    return graph.execute_query(query)


# -------------------------------
# Get User By ID
# -------------------------------
def get_user_by_id(user_id):

    query = """
    MATCH (u:User {userId:$user_id})
    RETURN
        u.userId AS userId,
        u.name AS name
    """

    data = graph.execute_query(
        query,
        {"user_id": user_id}
    )

    if data:
        return data[0]

    return None


# -------------------------------
# Recommendation
# -------------------------------
def recommend_movies(user_id):

    query = """
    MATCH (u:User {userId:$user_id})-[:WATCHED]->(:Movie)<-[:WATCHED]-(other:User)

    MATCH (other)-[:WATCHED]->(rec:Movie)

    WHERE NOT EXISTS {
        MATCH (u)-[:WATCHED]->(rec)
    }

    RETURN
        DISTINCT rec.movieId AS movieId,
        rec.title AS title,
        rec.genre AS genre,
        rec.year AS year
    LIMIT 10
    """

    return graph.execute_query(
        query,
        {"user_id": user_id}
    )