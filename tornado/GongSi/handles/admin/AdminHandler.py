import tornado

from handles.BaseHandler import BaseHandler

class AdminHandler(BaseHandler):

    '''
    后台处理器-》主界面
    '''
    @tornado.web.authenticated
    def get(self):
        return self.render(
            'admin/index.html',
            username=self.current_user
        )