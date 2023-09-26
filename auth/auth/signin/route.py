from flask import Blueprint

signin_blueprint = Blueprint('signin', __name__)


@signin_blueprint.route('/signin', methods=['POST'])
def signin():
    # Your implementation for /api/users/signin
    return "Current Sign In Route!!!"
