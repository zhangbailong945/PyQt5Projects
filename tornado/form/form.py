import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import os.path

from tornado.options import define, options

#定义端口
define("port", default=8888, help="run on the given port", type=int)

#主页请求拦截器
class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('index.html')


#表单请求拦截器
class PoemPageHandler(tornado.web.RequestHandler):

    def post(self):
        name = self.get_argument('name')
        age = self.get_argument('age')
        sex = self.get_argument('sex')
        hobbys = self.get_arguments('hobbys')
        self.render('poem.html', name=name, age=age, sex=int(sex), hobbys=hobbys)


if __name__ == "__main__":
    app = tornado.web.Application(
        handlers=[
            (r'/', IndexHandler),
            (r'/poem', PoemPageHandler)
        ],
        template_path=os.path.join(os.path.dirname(__file__), 'templates')
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
