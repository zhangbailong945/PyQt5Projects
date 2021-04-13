from flask import Flask
from App.settings import envs
from App.ext import init_ext
from App.views import init_views

def create_app(env):
    app=Flask(__name__)
    app.config.from_object(envs.get(env))
    init_ext(app)
    init_views(app=app)
    return app