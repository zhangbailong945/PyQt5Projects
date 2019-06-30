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
            (r'/about',AboutHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
            ui_modules={
            'FriendlyLinks':FriendlyLinksModule,
            'Menus':MenuModule,
            }
        )

        
        tornado.web.Application.__init__(self, handlers, **settings)




class FriendlyLinksModule(tornado.web.UIModule):
    '''
    自定义友情链接模块
    '''

    def render(self,link):
        return self.render_string('index/modules/index/links.html',link=link)
    
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
        return "css/style.css"

    #模块引入css文件
    def javascript_files(self):
        return "js/jquery.js"

class AboutHandler(tornado.web.RequestHandler):

    def get(self):
        self.render(
            'index/about.html'
        )


class MenuModule(tornado.web.UIModule):
    '''
    主页->菜单模块
    '''
    def __init__(self,*args,**kwargs):
        super(MenuModule,self).__init__(*args,**kwargs)
        self.dbHelper=MyMongoDb()

    def getMenus(self):
        '''
        获取菜单集合
        '''
        collection='menu'
        condition={"status":1}
        return self.dbHelper.find(collection,condition)

    def initLevelMenu(self,menuData,id,level=0):
        '''
        @params MenuData 菜单集合 \n
        @params id 菜单ID \n
        @params level 菜单层级 \n
        '''
        menuList=[]
        for menu in menuData:
            if menu['pid']==id:
                menu['level']=level
                menu['childMenu']=self.initLevelMenu(menuData,menu['_id'],level+1)
                menuList.append(menu)
        return menuList

    def render(self):
        menuData=self.getMenus()
        menus=self.initLevelMenu(menuData,0,0)
        html=""
        for menu in menus:
            html+='<li class=""><a href="" class="topa">'+menu["name"]+'</a>'
            if len(menu['childMenu'])>0:
                html+=self.getChild(menu['childMenu'])
                html+="</li>"
            else:
                html+='<ul style="display:none"></ul></li>'
        return html
    
    def getChild(self,menus):
        html="<ul class='drop-menu'>"
        for menu in menus:
            html+='<li class=""><a href="javascript:;" class="topa">'+menu["name"]+'</a>'
            if len(menu['childMenu'])>0:
                html+=self.getChild(menu['childMenu'])
                html+="</li>"
            else:
                html+='<ul style="display:none"></ul></li>'
        html+="</ul>"
        return html
            




class IndexHandler(tornado.web.RequestHandler):
    '''
    主页拦截器
    '''

    def get(self):
        self.dbHelper=MyMongoDb()
        self.myLinks=self.getLinks()
        self.render(
            'index/index.html',
            myLinks=self.myLinks, 
        )
    
    
    def getLinks(self):
        '''
        获取友情链接集合
        '''
        collection='friendlylinks'
        condition={"status":1}
        return self.dbHelper.find(collection,condition)
    
    



    



if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server=tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
