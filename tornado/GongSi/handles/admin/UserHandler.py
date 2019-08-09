from handles.BaseHandler import BaseHandler
from models.admin.UserModel import UserModel


class UserHandler(BaseHandler):
    '''
    后台管理=》用户处理器
    '''
    def get(self):
        return self.render('admin/user.html',user=UserModel().get_user())

