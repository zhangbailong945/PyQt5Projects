from handles.BaseHandler import BaseHandler


class LogoutHandler(BaseHandler):
    '''
    后台处理器-》注销
    '''

    def get(self):
        if (self.get_argument("logout",None)):
            self.clear_cookie("username")
            self.redirect("/login")