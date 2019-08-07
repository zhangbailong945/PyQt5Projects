from handles.BaseHandler import BaseHandler

import tornado.web

class WelcomeHandler(BaseHandler):

    '''
    后台处理器-》欢迎页面
    '''
    @tornado.web.authenticated
    def get(self):
        return self.render(
            'admin/welcome.html',
            username=self.current_user
        )