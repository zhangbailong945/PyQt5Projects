from App.Views.users import usersView
from App.Views.students import stuView
from App.Views.animals import animalsView

def init_views(app):
    app.register_blueprint(usersView)
    app.register_blueprint(stuView)
    app.register_blueprint(animalsView)