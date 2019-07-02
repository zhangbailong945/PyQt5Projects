
from handles.BaseHandler import BaseHandler


class AdminHandler(BaseHandler):

    '''
    后台处理器-》主界面
    '''

    def get(self):
        return self.render(
            'admin/index.html'
        )