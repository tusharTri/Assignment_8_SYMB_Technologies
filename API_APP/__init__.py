from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from API_APP.config import Config
db=SQLAlchemy()
api=Api()

config_class=Config
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    api.init_app(app)
    with app.app_context():
        from API_APP import routes
        db.create_all()
    

    return app
        