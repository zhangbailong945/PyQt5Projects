from App.views.index import indexView

def init_views(app):
    app.register_blueprint(indexView)
