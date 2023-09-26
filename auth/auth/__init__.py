from flask import Flask


def create_app():
    app = Flask(__name__)

    # Register blueprints
    from .current_user.route import current_user_blueprint

    app.register_blueprint(current_user_blueprint, url_prefix='/api/users')

    return app
