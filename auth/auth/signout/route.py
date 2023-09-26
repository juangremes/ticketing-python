from flask import Blueprint

signout_blueprint = Blueprint('signout', __name__)


@signout_blueprint.route('/signout', methods=['POST'])
def signout():
    # Your implementation for /api/users/signout
    return "Current Sign Out Route!!!"
