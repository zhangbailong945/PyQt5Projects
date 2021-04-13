from flask import Blueprint,request,render_template

usersView=Blueprint('usersView',__name__)

@usersView.route('/users/index/')
def index():
    return render_template('/users/index.html')