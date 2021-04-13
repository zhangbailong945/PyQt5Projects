from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_debugtoolbar import DebugToolbarExtension
from flask_caching import Cache

migrate=Migrate()
db=SQLAlchemy()
session=Session()
debugToolBar=DebugToolbarExtension()
cache=Cache(config={
    "CACHE_TYPE":'redis'
})
def init_ext(app):
    debugToolBar.init_app(app)
    cache.init_app(app)
    session.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)
