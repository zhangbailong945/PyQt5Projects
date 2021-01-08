import tornado
from tornado import ioloop
from tornado import web
from tornado.options import define,options,parse_command_line
from pymongo import MongoClient
import os
define('port',default=8888,type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello tornado')

    def post(self):
        self.write('post tornado')


class Day1Handler(tornado.web.RequestHandler):

    def get(self,year,month,day):
        self.write('%s年%s月%s日'%(year,month,day))

class Day2Handler(tornado.web.RequestHandler):

    def get(self,year,month,day):
        self.write('%s年%s月%s日'%(year,month,day))

class EntryHandler(tornado.web.RequestHandler):

    def initialize(self):
        print('initialize')
        self.client=MongoClient('mongodb://localhost:27017')
        self.db=self.client.db1
    
    def prepare(self):
        print('prepare')
        self.write('准备工作')

    def get(self):
        collection=self.db.emp
        results=collection.find()
        for res in results:
            print(res)
        self.write('查询数据')


    def finish(self):
        print('on_finshed')
        if self.client:
            print('close')
            self.client.close()

class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('index.html')

def make_app():
    return tornado.web.Application(
        handlers=[
            (r'/',MainHandler),
            (r'/day1/(\d{4})/(\d{2})/(\d{2})/',Day1Handler),
            (r'/day2/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/',Day2Handler),
            (r'/entry_point/',EntryHandler),
            (r'/index/',IndexHandler),
        ],
        template_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'templates').replace('\\','/'),
    )

if __name__=='__main__':
    parse_command_line()
    #启动
    app=make_app()
    app.listen(options.port)
    #循环监听IO实例
    tornado.ioloop.IOLoop.current().start()