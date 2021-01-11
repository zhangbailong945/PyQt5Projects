import tornado.web
import tornado.websocket
import time
from hashlib import md5
from app.models import init_db,User
from utils.conn import session
from utils.baidu_face import face_register

class InitDbHandler(tornado.web.RequestHandler):

    def get(self):
        init_db()
        self.write('初始化数据库成功.')

class LoginHandler(tornado.web.RequestHandler):

    def get(self):
            error=''
            self.render('login.html',error=error)


    def post(self):
        error=''
        username=self.get_argument('username')
        password=self.get_argument('password')
        if username in ['loach','long'] and password=='123456':
            self.set_cookie('username',username)
            self.render('chat.html')
        else:
            error='账号或密码错误'
            self.render('login.html',error=error)

class ChatHandler(tornado.websocket.WebSocketHandler):

    #连接对象
    user_oneline=[]
    def open(self,*args,**kwargs):
        self.user_oneline.append(self)
        username=self.get_cookie('username')
        send_time=time.strftime('%Y-%m-d %H:%M:%S')
        message=username+',加入聊天室！'
        msgdict=dict()
        msgdict['username']='Administrator'
        msgdict['message']=message
        msgdict['send_time']=send_time
        for user in self.user_oneline:
            user.write_message(msgdict)
    
    def on_message(self,message):
        username=self.get_cookie('username')
        send_time=time.strftime('%Y-%m-d %H:%M:%S')
        msgdict=dict()
        msgdict['username']=username
        msgdict['message']=message
        msgdict['send_time']=send_time
        for user in self.user_oneline:
            user.write_message(msgdict)
    
    def on_close(self):
        username=self.get_cookie('username')
        #退出连接
        self.user_oneline.remove(self)
        send_time=time.strftime('%Y-%m-d %H:%M:%S')
        msgdict=dict()
        msgdict['username']='Administrator'
        msgdict['message']=username+',退出聊天室。'
        msgdict['send_time']=send_time
        for user in self.user_oneline:
            user.write_message(msgdict)


class RegHandler(tornado.web.RequestHandler):

    def get(self):
        error=''
        self.render('reg.html',error=error)
    
    def post(self):
        face_img=self.get_argument('face_img')
        username=self.get_argument('username')
        realname=self.get_argument('realname')
        password=self.get_argument('password')
        if face_img and username and realname and password:
            #注册模型
            user=User()
            user.username=username
            user.realname=realname
            user.password=password
            session.add(user)
            session.commit()
            #百度接口
            img=face_img.split(',')[-1]
            print(img)
            res=face_register(img,user.id)
            if res:
                self.redirect('/login/')
            else:
                session.delete(user)
                session.commit()
                self.redirect('/reg/')
        else:
            error="请填写完整的注册信息"
            self.render('reg.html',error=error)
