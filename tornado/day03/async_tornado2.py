
import tornado.web
import tornado.ioloop
import tornado.httpclient
import tornado.gen

class IndexHandler(tornado.web.RequestHandler):

     @tornado.web.gen.coroutine    
     def get(self):
        q=self.get_argument('q')
        client=tornado.httpclient.AsyncHTTPClient()
        response=yield client.fetch('https://cn.bing.com/search?q=%s'%q)
        print(response)
        self.write('异步测试')

def make_app():
    return tornado.web.Application(
        handlers=[
            (r'/index/',IndexHandler)
        ]
    )

if __name__ == "__main__":
    app=make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()