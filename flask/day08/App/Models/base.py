from App.ext import db


class BaseModel(db.Model):
    '''数据库基类 Sqlalchemy db'''

    __abstract__=True

    def __init__(self):
        self.db=db
    
    def save(self):
        '''创建表对象'''
        self.db.create_all()
    
    def add(self):
        '''新增表记录'''
        self.db.session.add(self)
        self.db.session.commit()