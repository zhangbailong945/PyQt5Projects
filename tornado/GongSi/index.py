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
from handles.admin.UserHandler import UserHandler
from handles.admin.RoleHandler import RoleHandler
from handles.admin.RoleAccessHandler import RoleAccessHandler

define("port",default=8888,help="run localhost:8888 on browser!",type=int)


class Application(tornado.web.Application):
    '''系统'''


    def __init__(self):
        self.installer=Installer()
        self.installer.createMenu()
        self.installer.createFriendlyLinks()
        self.installer.createUserRole()
        self.installer.createUser()

        #网站路由
        indexs=[
            (r"/", IndexHandler),
            (r'/about',AboutHandler),
        ]
        #后台路由
        admins=[
            (r"/admin",AdminHandler),
            (r"/admin/index",AdminHandler),
            (r"/admin/welcome",WelcomeHandler),
            (r"/admin/login",LoginHandler),
            (r"/admin/logout",LogoutHandler),
            (r"/admin/user",UserHandler),
            (r"/admin/role",RoleHandler),
            (r"/admin/role_access",RoleAccessHandler)

        ]

        handlers=indexs+admins

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
            cookie_secret='6de683f6e8f038f62863fe27a17573e5',
            xsrf_cookies=True,
            login_url="/admin/login",
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
    
