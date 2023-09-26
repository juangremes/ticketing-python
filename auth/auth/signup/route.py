from flask import Blueprint

signup_blueprint = Blueprint('signup', __name__)


@signup_blueprint.route('/signup', methods=['POST'])
def signup():
    # Your implementation for /api/users/signup
    return "Current Sign Up Route!!!"
