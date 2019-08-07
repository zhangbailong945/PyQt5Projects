import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define,options
from Installer import Installer
from MyMongoDb import MyMongoDb
from modules.index.MenuModule import MenuModule
from modules.index.FriendlyLinksModule import FriendlyLinksModule
from handles.index.IndexHandler import IndexHandler
from handles.index.AboutHandler import AboutHandler


from handles.admin.AdminHandler import AdminHandler
from handles.admin.WelcomeHandler import WelcomeHandler
from handles.admin.LoginHandler import LoginHandler
from handles.admin.LogoutHandler import LogoutHandler

define("port",default=8888,help="run localhost:8888 on browser!",type=int)


class Application(tornado.web.Application):


    def __init__(self):
        self.installer=Installer()
        self.installer.createMenu()
        self.installer.createFriendlyLinks()

        indexs=[
            (r"/", IndexHandler),
            (r'/about',AboutHandler),
        ]

        admins=[
            (r"/admin",AdminHandler),
            (r"/welcome",WelcomeHandler),
            (r"/login",LoginHandler),
            (r"/logout",LogoutHandler)
        ]

        handlers=indexs+admins

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
            cookie_secret='6de683f6e8f038f62863fe27a17573e5',
            xsrf_cookies=True,
            login_url="/login",
            ui_modules={
            'FriendlyLinks':FriendlyLinksModule,
            'Menus':MenuModule,
            }
        )
        self.db=MyMongoDb()
        tornado.web.Application.__init__(self, handlers, **settings)
        

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server=tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
