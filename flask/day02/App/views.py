
def init_route(app):

   @app.route('/')
   def index():
      return 'hello'
   
   @app.route('/hello')
   def hello():
      return 'hello a gui'
   
   @app.route('/hi')
   def hi():
      return 'what hi?'
