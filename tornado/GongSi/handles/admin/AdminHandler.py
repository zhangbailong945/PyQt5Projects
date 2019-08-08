import tornado

from handles.BaseHandler import BaseHandler
from plugins.config.Config import Config

class AdminHandler(BaseHandler):

    '''
    后台处理器-》主界面
    '''
    @tornado.web.authenticated
    def get(self):
        return self.render(
            'admin/index.html',
            username=self.current_user,
            sitename=Config('config.ini',1).get_key('sitename')
        )