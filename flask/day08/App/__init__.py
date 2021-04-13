from flask import Flask
from App.Views import init_views
from App.settings import envs
from App.ext import init_ext
import os

env=os.environ.get('develop') or 'default'

def create_app(env):
    app=Flask(__name__)
    app.config.from_object(envs.get(env))
    init_ext(app)
    init_views(app=app)

    return app