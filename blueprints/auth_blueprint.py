import flask
from controllers import auth_controller

blueprint = flask.Blueprint('auth', __name__)

blueprint.add_url_rule(
    '/register',
    view_func=auth_controller.register_user,
    methods=['POST']
)

