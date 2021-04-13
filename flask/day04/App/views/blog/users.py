from flask import Blueprint,render_template
from App.models.users import models,UsersModel
usersView=Blueprint('usersView',__name__)

@usersView.route('/blog/user/create')
def create():
    models.create_all()
    return 'created success!'

@usersView.route('/blog/user/drop')
def drop():
    models.drop_all()
    return 'drop success!'