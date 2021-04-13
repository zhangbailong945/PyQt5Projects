from flask import Blueprint,request,render_template,make_response,Response,abort,session
from App.models import User
indexView=Blueprint('indexView',__name__)

@indexView.route('/',methods=['GET','POST','DELETE'])
def index():
    return 'index'


@indexView.route('/create/')
def create():
    user=User()
    user.save()
    return 'create success!'

@indexView.route('/sendrequest/',methods=['GET','POST','DELETE','PUT','PATCH'])
def send_request():
    print(request.args)
    print(type(request.args))
    print(request.form)
    print(type(request.form))
    return 'send success!'

@indexView.route('/getresponse/')
def get_response():
    # result=render_template('hello.html')
    # print(result)
    # print(type(result))
    # response=make_response('<h1>ssss</h1>')
    # response=Response('<h2>hello</h2>')
    # return response
    abort(401)


@indexView.errorhandler(401)
def handle_error(error):
    print(error)
    print(type(error))
    return 'what'

@indexView.route('/login/',methods=['GET','POST'])
def login():
    if request.method=="GET":
        return render_template('login.html')
    elif request.method=='POST':
        name=request.form.get('name')
        response=Response('登录成功%s'%name)
        # response.set_cookie('username',username)
        session['name']=name
        return response

@indexView.route('/mine/')
def mine():
    # username=request.cookies.get('username')
    name=session.get('name')
    print(session)
    print(type(session))
    return '%s,欢迎回来!'%name