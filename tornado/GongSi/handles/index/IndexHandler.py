from handles.BaseHandler import BaseHandler


class IndexHandler(BaseHandler):
    '''
    主页拦截器
    '''

    def get(self):
        self.myLinks=self.getLinks()
        self.render(
            'index/index.html',
            myLinks=self.myLinks, 
        )
    
    
    def getLinks(self):
        '''
        获取友情链接集合
        '''
        collection='friendlylinks'
        condition={"status":1}
        return self.dbHelper.find(collection,condition)
    