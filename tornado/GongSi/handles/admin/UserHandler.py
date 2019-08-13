from handles.BaseHandler import BaseHandler
from models.admin.UserModel import UserModel


class UserHandler(BaseHandler):
    '''
    后台管理=》用户处理器
    '''
    def get(self):
        username=self.get_argument("username","")
        page_num=self.get_argument("page_num",10)
        page_current=self.get_argument("page_current",1)
        page_url=self.get_request_url()
        #sort_name=self.get_argument("sort_name","")
        #sort_flag=self.get_argument("sort_flag","")
        args=dict()
        args['username']=username
        args['page_num']=page_num
        args['page_current']=page_current
        args['page_url']=page_url
        return self.render('admin/user-list.html',user=UserModel().get_user(args))



