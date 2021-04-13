from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session


models=SQLAlchemy()
migrate=Migrate()
session=Session()


def init_ext(app):
    session.init_app(app=app)
    #Session(app=app)
    models.init_app(app=app)
    migrate.init_app(app,models)



