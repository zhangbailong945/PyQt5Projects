from App.ext import db
from App.Models.base import BaseModel

class StudentsModel(db.Model):
    __tablename__='students'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(16))
    
    def add_more(self,students):
        db.session.add_all(students)
        db.session.commit()
    
    def del_stu(self,student):
        db.session.delete(student)
        db.session.commit()