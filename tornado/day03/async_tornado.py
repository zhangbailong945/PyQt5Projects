
import tornado.web
import tornado.ioloop
import tornado.httpclient
import tornado.gen

class IndexHandler(tornado.web.RequestHandler):
    
    async def get(self):
        q=self.get_argument('q')
        client=tornado.httpclient.AsyncHTTPClient()
        try:
            response=await client.fetch('https://cn.bing.com/search?q=%s'%q)
            self.write('异步测试')
        except Exception as e:
            print('Error:%s'%e)
        else:
            print(response)

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