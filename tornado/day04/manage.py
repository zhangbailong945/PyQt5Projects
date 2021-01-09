import tornado.web
import tornado.ioloop
from tornado.options import options,define,parse_command_line
from app.views import InitDbHandler,LoginHandler,ChatHandler,RegHandler

import os

define('port',default=8888,type=int)

def make_app():
    return tornado.web.Application(
        handlers=[
            (r'/init_db/',InitDbHandler),
            (r'/login/',LoginHandler),
            (r'/chat/',ChatHandler),
            (r'/reg/',RegHandler),
        ],
        template_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'templates').replace('\\','/'),
        static_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'static').replace('\\','/'),
    )


if __name__ == "__main__":
    parse_command_line()
    app=make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()