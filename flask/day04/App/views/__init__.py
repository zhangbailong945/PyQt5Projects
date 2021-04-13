from App.views.blog.index import indexView
from App.views.blog.users import usersView

def init_views(app):
    app.register_blueprint(indexView)
    app.register_blueprint(usersView)
