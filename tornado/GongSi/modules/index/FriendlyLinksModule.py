
from modules.BaseModule import BaseModule

class FriendlyLinksModule(BaseModule):
    '''
    自定义友情链接模块
    '''

    def render(self,link):
        return self.render_string('index/modules/index/links.html',link=link)
    
    #在<body> 之前添加html代码
    def html_body(self):
        pass
    
    #模块添加js
    def embedded_javascript(self):
        pass
    
    #模块添加css
    def embedded_css(self):
        pass
    
    #模块引入css文件
    def css_files(self):
        pass

    #模块引入css文件
    def javascript_files(self):
        pass