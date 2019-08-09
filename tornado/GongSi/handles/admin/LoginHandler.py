from handles.BaseHandler import BaseHandler


class LoginHandler(BaseHandler):
    '''
    后台处理器-》登录
    '''

    def get(self):
        return self.render('admin/login.html')
    
    def post(self):
        username=self.get_argument("username")
        password=self.get_argument("password")
        if username=='admin' and password=='admin':
            self.set_secure_cookie("username",username)
            return self.redirect("/admin")
        else:
            return self.redirect("/login")