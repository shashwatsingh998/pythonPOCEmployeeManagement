from flask import Flask
from flask_restx import Resource,Api
from inventory.config import Config
from inventory.db import init_db,mongo
from inventory.views import main
from inventory.api_routes import api
from inventory.auth import auth

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)



    app.register_blueprint(main) 
    app.register_blueprint(auth)
    api.init_app(app)
    
    return app


    
