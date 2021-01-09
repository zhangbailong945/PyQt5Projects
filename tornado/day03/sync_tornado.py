import tornado.web
import tornado.ioloop
import tornado.httpclient

import requests

class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        q=self.get_argument('q')
        #向地址发送请求 https://cn.bing.com/search?q=
        response=requests.get('https://cn.bing.com/search?q=%s'%q)
        print(response.text)
        self.write('同步测试')

def make_app():
    return tornado.web.Application(
        handlers=[
            (r'/index/',IndexHandler),
        ],
    )



if __name__ == "__main__":
    app=make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
