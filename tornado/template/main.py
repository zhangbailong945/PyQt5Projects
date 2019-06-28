import os.path
import random

import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.web

from tornado.options import define, options
define("port",default=8888,help="run localhost:8888",type=int)

class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render(
            'index.html',
            header_text="头",
            body_text="身",
            footer_text="脚"
        )


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r'/', IndexHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
