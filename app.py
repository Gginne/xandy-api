from flask import Flask, request, jsonify


def create_app():
    app = Flask(__name__)
    
    # Register server routes
    
    # Register middlewares
    
    # Exception handlers
    
    return app

def start_server():
    
    app = create_app()
    app.run(host='0.0.0.0', port=105)
    
    
if __name__ == '__main__':
    start_server()