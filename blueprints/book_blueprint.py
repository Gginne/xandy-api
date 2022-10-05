import flask
from controllers import book_controller

blueprint = flask.Blueprint('books', __name__)

blueprint.add_url_rule(
    '/upload',
    view_func=book_controller.upload_book,
    methods=['POST']
)

blueprint.add_url_rule(
    '/search',
    view_func=book_controller.search_books,
    methods=['GET']
)

blueprint.add_url_rule(
    '/<string:book_id>/read',
    view_func=book_controller.read_book,
    methods=['GET']
)
