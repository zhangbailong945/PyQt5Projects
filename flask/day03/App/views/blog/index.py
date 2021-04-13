from flask import Blueprint,render_template
from App.models import models,User
index=Blueprint('index',__name__)

@index.route('/')
def main():
    # return 'blog index'
    return render_template('blog/index.html',msg='php')


@index.route('/blog/createdb/')
def createdb():
    models.create_all()
    return 'create successed!'

@index.route('/blog/adduser/')
def adduser():
    user=User()
    user.username='loach'
    # models.session.add(user)
    # models.session.commit()
    user.save()
    return 'add user successed!'

@index.route('/blog/dropuser/')
def dropuser():
    models.drop_all()
    return 'drop user successed!'