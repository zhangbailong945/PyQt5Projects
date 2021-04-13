from flask import Flask

from App.ext import init_ext
from App.views import init_view
from App.settings import envs


def create_app(env):
    app=Flask(__name__)
    #数据库URI格式 数据库+驱动://用户名:密码@主机:端口/数据库名
    # app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///sqlite.db"
    # app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:root@localhost:3306/mytest"
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config.from_object(envs.get(env))
    init_ext(app)
    init_view(app=app)
    return app