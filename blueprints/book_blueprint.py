import flask
from controllers import book_controller

blueprint = flask.Blueprint('book', __name__)

blueprint.add_url_rule(
    '/upload',
    view_func=book_controller.upload_book,
    methods=['POST']
)

blueprint.add_url_rule(
    '/<string:book_id>/read',
    view_func=book_controller.read_book,
    methods=['GET']
)