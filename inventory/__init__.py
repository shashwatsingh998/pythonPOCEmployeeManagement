from flask import Flask
from inventory.config import Config
from inventory.db import init_db
from inventory.views import main
from inventory.auth import auth

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)

    app.register_blueprint(main) 
    app.register_blueprint(auth)

    return app
