from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from flask_bootstrap import Bootstrap


db=SQLAlchemy()
migrate=Migrate()
session=Session()
bootStrap=Bootstrap()


def init_ext(app):
    bootStrap.init_app(app)
    session.init_app(app)
    db.init_app(app=app)
    migrate.init_app(app,db)
