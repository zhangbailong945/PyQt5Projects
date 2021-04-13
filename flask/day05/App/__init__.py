from flask import Flask
from App.views import init_views
from App.ext import init_ext
from App.settings import envs

def create_app(env):
    app=Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////test.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config.from_object(envs.get(env))
    init_ext(app)
    init_views(app=app)
    return app
