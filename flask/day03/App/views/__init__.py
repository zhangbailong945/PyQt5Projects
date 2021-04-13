from App.views.blog.index import index

def init_view(app):
    app.register_blueprint(index)