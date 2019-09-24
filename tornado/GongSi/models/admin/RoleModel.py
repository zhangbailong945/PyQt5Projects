from plugins.db.MongoHelper import MongoHelper
from handles.Pagintaion import Pagination


class RoleModel(MongoHelper):

    def __init__(self):
        super(RoleModel,self).__init__()
        self.col="role"
    
    def get_role(self,args):
        query=args['query']
        colum=None
        page_total=self.count(self.col)
        page_current=args['page_current']
        page_num=args['page_num']
        page_url=args['page_url']
        page=Pagination(page_total=page_total,page_num=page_num,page_current=page_current,page_url=page_url,page_show=2)
        return self.find(page,self.col,query,colum),page
