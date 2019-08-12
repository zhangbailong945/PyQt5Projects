import tornado

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    '''
    请求处理器 基类
    '''

    @property
    def dbHelper(self):
        '''
        数据库操作者
        '''
        return self.application.db
    
    def status_error(self,status_code,**kwargs):
        '''
        请求错误处理
        '''
        if status_code==400:
            error="400:Bad Request!"
            self.render(
                'error.html',
                error=error,
                home_title=options.home_title
            )
        if status_code==405:
            error="405:Method Not Allowed!"
            self.render(
                "error.html",
                error=error,
                home_title=options.home_title
            )
        if status_code==404:
            error="404:Page Not Found!"
            self.render(
                "error.html",
                error=error,
                home_title=options.home_title
            )

    def get_current_user(self):
        '''
        当前登录用户
        '''
        return self.get_secure_cookie('username')

    def get_current_user_roles(self):
        username=self.get_current_user()
        if username:
            pass
    
    