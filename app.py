from flask import Flask
from config import Config

# Import Blueprints
from routes.home import home_bp
from routes.movies import movie_bp
from routes.users import user_bp
from routes.recommendation import recommendation_bp


def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(movie_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(recommendation_bp)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)