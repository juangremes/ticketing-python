from flask import Flask


def create_app():
    app = Flask(__name__)

    # Register blueprints
    from .current_user.route import current_user_blueprint
    from .signin.route import signin_blueprint
    from .signout.route import signout_blueprint
    from .signup.route import signup_blueprint

    app.register_blueprint(current_user_blueprint, url_prefix='/api/users')
    app.register_blueprint(signin_blueprint, url_prefix='/api/users')
    app.register_blueprint(signout_blueprint, url_prefix='/api/users')
    app.register_blueprint(signup_blueprint, url_prefix='/api/users')

    return app
