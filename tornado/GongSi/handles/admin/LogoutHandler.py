from handles.BaseHandler import BaseHandler


class LogoutHandler(BaseHandler):

    def get(self):
        if (self.get_argument("logout",None)):
            self.clear_cookie("username")
            self.redirect("/login")