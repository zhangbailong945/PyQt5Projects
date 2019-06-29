import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define,options
from Installer import Installer
from MyMongoDb import MyMongoDb

define("port",default=8888,help="run localhost:8888 on browser!",type=int)


class Application(tornado.web.Application):
    def __init__(self):
        self.installer=Installer()
        self.installer.createMenu()
        self.installer.createFriendlyLinks()
        handlers = [
            (r"/", IndexHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
            ui_modules={
            'FriendlyLinks':FriendlyLinksModule,
            'Menu':MenuModule,
            }
        )

        
        tornado.web.Application.__init__(self, handlers, **settings)




class FriendlyLinksModule(tornado.web.UIModule):
    '''
    自定义友情链接模块
    '''

    def render(self,link):
        return self.render_string('modules/index/links.html',link=link)
    
    #在<body> 之前添加html代码
    def html_body(self):
        return ""
    
    #模块添加js
    def embedded_javascript(self):
        return "document.write(\"hi!\")"
    
    #模块添加css
    def embedded_css(self):
        return "body {background-color:#F5F5F5}"
    
    #模块引入css文件
    def css_files(self):
        return "static/css/style.css"

    #模块引入css文件
    def javascript_files(self):
        return "static/js/jquery.js"


class MenuModule(tornado.web.UIModule):
    '''
    主页菜单模块
    '''

    def render(self,menu):
        return self.render_string('modules/index/menu.html',menu=menu)


#主页拦截器
class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.dbHelper=MyMongoDb()
        self.myMenus=self.getMenus()
        self.myLinks=self.getLinks()
        self.treeData(self.myLinks)
        self.render(
            'index.html',
            myMenus=self.myMenus,
            myLinks=self.myLinks, 
        )
    
    def getMenus(self):
        '''
        获取菜单集合
        '''
        collection='menu'
        condition={"status":1}
        return self.dbHelper.find(collection,condition)
    
    def getLinks(self):
        '''
        获取友情链接集合
        '''
        collection='friendlylinks'
        condition={"status":1}
        return self.dbHelper.find(collection,condition)
    
    def treeData(self,list,pid=0):
        childList=[]
        for d in list:
            if d['pid']==pid:
                childList.append(d)



    



if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server=tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
