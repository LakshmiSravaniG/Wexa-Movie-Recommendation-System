from flask import Blueprint, render_template
from services.recommendation_service import get_recommendations

recommendation_bp = Blueprint("recommendation", __name__)


@recommendation_bp.route("/recommend/<int:user_id>")
def recommendation(user_id):

    recommendations = get_recommendations(user_id)

    return render_template(
        "recommendations.html",
        recommendations=recommendations,
        user_id=user_id
    )