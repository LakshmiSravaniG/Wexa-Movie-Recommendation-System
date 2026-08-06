from database.queries import (
    get_all_users,
    get_user_by_id
)


def fetch_all_users():
    """
    Return all users.
    """
    return get_all_users()


def fetch_user(user_id):
    """
    Return a single user.
    """
    return get_user_by_id(user_id)