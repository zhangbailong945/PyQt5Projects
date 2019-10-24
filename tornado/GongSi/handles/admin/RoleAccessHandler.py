from handles.BaseHandler import BaseHandler
from models.admin.RoleModel import RoleModel


class RoleAccessHandler(BaseHandler):
    '''
    后台管理=》用户处理器
    '''
    def get(self):
        return self.render('admin/role-access-edit.html')


        