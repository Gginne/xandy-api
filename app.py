import os

from flask import Flask
from config.db import init_db

def create_app():
    """ Construct the core application """
    app = Flask(__name__, instance_relative_config=False)
    return app

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