from flask import Flask
from inventory.config import Config
from inventory.db import init_db
from inventory.views import main
from inventory.auth import auth

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    #TODO Store this as an enviornment variable since this needs to be hidden for git push
    app.secret_key='shashwat'

    init_db(app)

    app.register_blueprint(main) 
    app.register_blueprint(auth)

    return app
