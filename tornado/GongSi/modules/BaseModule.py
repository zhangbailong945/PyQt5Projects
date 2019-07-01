import tornado
from MyMongoDb import MyMongoDb

class BaseModule(tornado.web.UIModule):
    '''
    模块基类
    '''
    def __init__(self,*args,**kwargs):
        super(BaseModule,self).__init__(*args,**kwargs)
        self.dbHelper=MyMongoDb()
    
