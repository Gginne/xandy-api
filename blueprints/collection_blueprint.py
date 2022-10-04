import flask
from controllers import collection_controller

blueprint = flask.Blueprint('collection', __name__)

blueprint.add_url_rule(
    '/create',
    view_func=collection_controller.create_collection,
    methods=['POST']
)
