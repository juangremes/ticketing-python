from flask import Blueprint

current_user_blueprint = Blueprint('current_user', __name__)


@current_user_blueprint.route('/current_user')
def current_user():
    # Your implementation for /api/users/current_user
    return "Current User Route!!!"
