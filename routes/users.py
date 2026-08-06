from flask import Blueprint, render_template
from services.user_service import (
    fetch_all_users,
    fetch_user
)

user_bp = Blueprint("users", __name__)


@user_bp.route("/users")
def users():
    users = fetch_all_users()
    return render_template("users.html", users=users)


@user_bp.route("/user/<int:user_id>")
def user_profile(user_id):

    user = fetch_user(user_id)

    if user is None:
        return render_template("error.html", message="User not found")

    return render_template("user_profile.html", user=user)