from handles.BaseHandler import BaseHandler
from models.admin.UserModel import UserModel


class UserHandler(BaseHandler):
    '''
    后台管理=》用户处理器
    '''
    def get(self):
        name_en=self.get_argument("name_en","")
        page_num=self.get_argument("page_num",10)
        page_current=self.get_argument("page_current",1)
        page_url=self.get_request_url()
        #sort_name=self.get_argument("sort_name","")
        #sort_flag=self.get_argument("sort_flag","")
        query=dict()
        page_args=dict()
        query['name_en']=name_en
        
        page_args['query']=query
        page_args['page_num']=page_num
        page_args['page_current']=page_current
        page_args['page_url']=page_url
        users,page=UserModel().get_user(page_args)
        print(self.get_request_query())

        #print(page.show_pages())
        for user in users:
            print(user['name_en'])
        return self.render('admin/user-list.html',users=users,page=page)

    def get_page_url(self,page_args):
        if self.get_request_query() is None:

        



