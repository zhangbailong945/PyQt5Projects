import tornado

from tornado import ioloop
from tornado import web
from tornado.options import options,define,parse_command_line

define('port',default=8000,type=int)
from datetime import datetime,timedelta
class MainHandler(web.RequestHandler):

    def get(self):
        self.write('hello world!')
        name=self.get_argument('name')
        self.write(name)
    
    def post(self):
        name=self.get_argument('name')
        self.write(name)

class ResHandler(web.RequestHandler):

    def get(self):
        self.write('welcome res page!')
        name=self.get_argument('resname')
        self.write(name)
        self.set_status(200)
        token_time=datetime.now()+timedelta(days=1)
        self.set_cookie('token','123456',expires=token_time)
        self.set_cookie('name','zhangsan',expires_days=1)
        # self.clear_cookie('name')
        # self.clear_all_cookies()
        #self.redirect('/?name=234')
    
    def post(self):
        self.write('welcome res post page!')
        name=self.get_argument('resname')
        self.write(name)

class Days1Handler(web.RequestHandler):

    def get(self,year,month,day):
        self.write('%s年%s月%s日'%(year,month,day))

class Days2Handler(web.RequestHandler):

    def get(self,year,month,day):
        self.write('%s年%s月%s日'%(year,month,day))

def make_app():
    return tornado.web.Application(handlers=[
        (r'/',MainHandler),
        (r'/res/',ResHandler),
        (r'/days1/(\d{4})/(\d{2})/(\d{2})/',Days1Handler),
        (r'/days2/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/',Days2Handler)
    ])


if __name__ == "__main__":
    parse_command_line()
    app=make_app()
    server=tornado.httpserver.HTTPServer(app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()