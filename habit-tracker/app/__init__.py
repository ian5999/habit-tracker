# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '4714fe5f99e2d391386d1a0cc36a9fe9'

    # Register your blueprints
    from app.routes import main
    from app.auth_routes import auth

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
