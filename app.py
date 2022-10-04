import os

from flask import Flask
from config.db import init_db
from blueprints import auth_blueprint, book_blueprint, collection_blueprint

def create_app():
    # Construct the core application 
    app = Flask(__name__, instance_relative_config=False)
    
    register_blueprints(app)
    
    return app

def register_blueprints(app):
    app.register_blueprint(auth_blueprint.blueprint, url_prefix='/auth')
    app.register_blueprint(book_blueprint.blueprint, url_prefix='/book')
    app.register_blueprint(collection_blueprint.blueprint, url_prefix='/collection')
    
def start_server():
    app = create_app()
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    if not os.environ.get("PRODUCTION"):
        from dotenv import load_dotenv
        load_dotenv('./.env')
    
    init_db()
    start_server()