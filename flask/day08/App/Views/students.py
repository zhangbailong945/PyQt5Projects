from flask import Blueprint,request,Response,render_template,url_for
from App.Models.students import StudentsModel
import random

stuView=Blueprint('stuView',__name__,url_prefix='/stu')

@stuView.route('/index/')
def index():
    return render_template('/students/index.html')


@stuView.route('/students/create/')
def create():
    stuModel=StudentsModel()
    stuModel.create()
    return Response('创建学生表成功!')


@stuView.route('/students/add/')
def add():
    stuModel=StudentsModel()
    stuModel.name="小明%d"%random.randrange(100000)
    stuModel.add()
    return Response('添加成功!')

@stuView.route('/students/add_more/')
def add_more():
    students=[]
    for i in range(5):
        stuModel=StudentsModel()
        stuModel.name="小明%d"%random.randrange(100000)
        students.append(stuModel)
    StudentsModel().add_more(students)
    return Response('添加5个学生成功!')


@stuView.route('/students/get/')
def get_student():
    # stuModel=StudentsModel.query.first()
    # stuModel=StudentsModel.query.get_or_404(20)
    stuModel=StudentsModel.query.get(20)
    print(stuModel)
    return 'get success'

@stuView.route('/students/get_all/')
def get_all():
    students=StudentsModel.query.all()
    # for stu in students:
    #     print(stu.name)
    return render_template('/students/list.html',students=students)

@stuView.route('/students/del_stu/')
def del_stu():
    student=StudentsModel.query.first()
    StudentsModel().del_stu(student)
    return 'delete student success!'

@stuView.route('/students/update_stu/')
def update_stu():
    student=StudentsModel.query.first()
    student.name='李四'
    student.add()
    return 'update stu success!'

@stuView.route('/students/redir/')
def redir():
    url=url_for('stuView.get_student',id=3)
    return url