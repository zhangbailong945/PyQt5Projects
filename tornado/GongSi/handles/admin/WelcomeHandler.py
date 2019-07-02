from handles.BaseHandler import BaseHandler

class WelcomeHandler(BaseHandler):

    '''
    后台处理器-》欢迎页面
    '''

    def get(self):
        return self.render(
            'admin/welcome.html'
        )