# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '4714fe5f99e2d391386d1a0cc36a9fe9'
    
    # Import your blueprints
    from app.auth_routes import auth
    from app.routes import main

    # Register them (without a URL prefix unless desired)
    app.register_blueprint(auth)
    app.register_blueprint(main)

    return app
