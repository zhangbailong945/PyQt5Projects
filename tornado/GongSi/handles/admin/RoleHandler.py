from handles.BaseHandler import BaseHandler
from models.admin.RoleModel import RoleModel


class RoleHandler(BaseHandler):
    '''
    后台管理=》用户处理器
    '''
    def get(self):
        url='role'
        name_en=self.get_argument("username","")
        page_num=self.get_argument("page_num",10)
        page_current=self.get_argument("page_current",1)
        #sort_name=self.get_argument("sort_name","")
        #sort_flag=self.get_argument("sort_flag","")
        db_query=dict()
        page_args=dict()

        if len(name_en)>0 and name_en.strip()!="":
            db_query['name_en']=name_en
        
        
        page_args['page_num']=page_num
        page_args['page_current']=page_current
        url_query=dict()
        url_query.update(db_query)
        url_query.update(page_args)