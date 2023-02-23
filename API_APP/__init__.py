from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from API_APP.config import Config
from flask_migrate import Migrate
db=SQLAlchemy()
migrate=Migrate()

config_class=Config
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app)
    
    # with app.app_context():
        # from API_APP import models
        # db.create_all()
        # from API_APP.routes import main
    return app
