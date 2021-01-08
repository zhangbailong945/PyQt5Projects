import tornado.web

from app.models import create_db,drop_db,Student
from utils.conn import session


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('index.html')


class XindexHandler(tornado.web.RequestHandler):

    def get(self):
        items=['java','php','python']
        self.render('index.html',items=items,items2=items)


class DbHandler(tornado.web.RequestHandler):

    def  get(self):
        create_db()
        self.write('创建表成功')

class DropHandler(tornado.web.RequestHandler):

    def get(self):
        drop_db()
        self.write('删除表成功')
    
class AddStuHandler(tornado.web.RequestHandler):

    def post(self):
        stu=Student()
        stu.s_name='小明'
        session.add(stu)
        session.commit()
        self.write('新增数据成功')

class AddMultiStuHandler(tornado.web.RequestHandler):

    def post(self):
        stus=[]
        for i in range(10):
            stu=Student()
            stu.s_name='小明——%d'%i
            stus.append(stu)
        session.add_all(stus)
        session.commit()
        self.write('新增多条数据成功')

class QueryStuHandler(tornado.web.RequestHandler):

    def get(self):
        #stu=session.query(Student).filter(Student.s_name=='小明').all()
        stu=session.query(Student).filter_by(s_name='小明').all()
        print(stu)
        self.write('查询数据成功')
    
    def delete(self):
        #第一种session.delete
        stu=session.query(Student).filter(Student.s_name=='小明').first()
        if stu:
            session.delete(stu)
            session.commit()
        
        #第二种delete()
        session.query(Student).filter(Student.s_name=='小明——0').delete()
        session.commit()
        self.write('数据已删除')
    
    def patch(self):
        #第一种
        stu=session.query(Student).filter(Student.s_name=='小明——1').first()
        if stu:
            stu.s_name='小花0'
            session.add(stu)
            session.commit()
        
        session.query(Student).filter(Student.s_name=='小花0').update({'s_name':'小明——1'})
        session.commit()


        self.write('修改数据成功')
