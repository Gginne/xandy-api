import flask
from controllers import collection_controller

blueprint = flask.Blueprint('collections', __name__)

blueprint.add_url_rule(
    '/create',
    view_func=collection_controller.create_collection,
    methods=['POST']
)

blueprint.add_url_rule(
    '/<string:collection_id>/add',
    view_func=collection_controller.add_book,
    methods=['POST']
)
