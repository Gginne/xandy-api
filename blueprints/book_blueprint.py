import flask
from controllers import book_controller

blueprint = flask.Blueprint('book', __name__)

blueprint.add_url_rule(
    '/upload',
    view_func=book_controller.upload_book,
    methods=['POST']
)