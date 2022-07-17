from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import init_db

db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app

def start_server():
    app = create_app()
    app.run(host='0.0.0.0', port=105)
    

if __name__ == '__main__':
    init_db()
    start_server()