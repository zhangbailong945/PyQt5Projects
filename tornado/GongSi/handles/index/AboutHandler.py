
from handles.BaseHandler import BaseHandler


class AboutHandler(BaseHandler):
    
    '''
    关于我们
    '''

    def get(self):
        self.render(
            'index/about.html'
        )