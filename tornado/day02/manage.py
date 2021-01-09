import os
import tornado.web
import tornado.ioloop
from tornado.options import define,options,parse_command_line

from app.views import IndexHandler,XindexHandler,DbHandler,DropHandler,AddStuHandler,AddMultiStuHandler,QueryStuHandler


define('port',default=8000,type=int)

def make_app():
    return tornado.web.Application(
        handlers=[
            (r'/',IndexHandler), 
            (r'/xindex/',XindexHandler),
            (r'/init_db/',DbHandler),
            (r'/drop_db/',DropHandler),
            (r'/add_stu/',AddStuHandler),
            (r'/add_more_stu/',AddMultiStuHandler),
            (r'/query_stu/',QueryStuHandler),
        ],
        template_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'templates').replace('\\','/'),
        static_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'static').replace('\\','/'),
    )

if __name__ == "__main__":
    parse_command_line()
    #生成application对象
    app=make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()