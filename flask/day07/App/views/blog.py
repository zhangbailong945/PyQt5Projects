from flask import Blueprint,render_template,request,make_response,Response,session
from App.models.blog import BlogModel


blogView=Blueprint('blog',__name__)

@blogView.route('/blog/createDb/')
def createDb():
    blog=BlogModel()
    blog.save()
    return 'create blog success!'


@blogView.route('/blog/login/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('/blog/login.html')
    elif request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        print(username)
        if username=='admin' and password=='admin':
            session['admin']=username
            response=Response('%s,登录成功!'%username)
            return response
        else:
            return render_template('/blog/login.html')
    else:
        return render_template('/blog/login.html')


@blogView.route('/blog/index/')
def index():
    list=[i for i in range(10)]
    return render_template('blog/index.html',list=list,a=5,b=3)

@blogView.route('/blog/user/')
def user():
    return render_template('users/user_register.html',title='用户注册')

@blogView.route('/blog/user2/')
def user2():
    list=[i for i in range(10)]
    return render_template('users/user_register2.html',title='用户注册',list=list,msg='helloworld')