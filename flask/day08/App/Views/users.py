from flask import Blueprint,request,Response,render_template
from App.Models.users import UsersModel

usersView=Blueprint('usersView',__name__)

@usersView.route('/')
def index():
    return render_template('/users/index.html')


@usersView.route('/users/create/')
def create():
    user=UsersModel()
    user.save()
    return Response('<h1>成功创建用户表!</h1>')
    