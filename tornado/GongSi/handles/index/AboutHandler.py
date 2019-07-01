
from handles.BaseHandler import BaseHandler


class AboutHandler(BaseHandler):

    def get(self):
        self.render(
            'index/about.html'
        )