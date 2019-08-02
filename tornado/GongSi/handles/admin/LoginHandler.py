from handles.BaseHandler import BaseHandler


class LoginHandler(BaseHandler):

    def get(self):
        return self.render('admin/login.html')
    
    def post(self):
        username=self.get_argument("username")
        password=self.get_argument("password")
        print(11111)
        print(username)
        print(password)
        self.set_secure_cookie("username",username)
        return self.redirect("/welcome")