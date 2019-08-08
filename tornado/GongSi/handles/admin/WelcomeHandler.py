from handles.BaseHandler import BaseHandler

from plugins.config.Config import Config
import tornado.web

class WelcomeHandler(BaseHandler):

    '''
    后台处理器-》欢迎页面
    '''
    @tornado.web.authenticated
    def get(self):
        return self.render(
            'admin/welcome.html',
            username=self.current_user,
            system=self.get_config()
        )
    
    def get_config(self):
        '''
        获取系统基本信息
        '''
        system=dict()
        system['sitename']=Config('config.ini',1).get_key('sitename')
        system['version']=Config('config.ini',1).get_key('version')
        system['author']=Config('config.ini',1).get_key('author')
        system['author_website']=Config('config.ini',1).get_key('author_website')
        return system



        