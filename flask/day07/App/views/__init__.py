from App.views.blog import blogView
from App.views.users import usersView

def init_views(app):
    app.register_blueprint(blogView)
    app.register_blueprint(usersView)