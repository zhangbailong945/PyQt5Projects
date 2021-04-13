from App.ext import db
from App.Models.base import BaseModel

class UsersModel(db.Model):

    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(22))
    gender=db.Column(db.Integer)
