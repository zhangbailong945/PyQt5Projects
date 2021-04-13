from App.ext import db
from App.Models.base import BaseModel

class Animals(BaseModel):

    __abstract__=True

    __tablename__='animals'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    a_name=db.Column(db.String(32),unique=True)

    def __init__(self):
        super().__init__()


class Dogs(Animals):

    __tablename__='dogs'

    d_legs=db.Column(db.Integer,default=4)

    def __init__(self):
        super().__init__()


class Cats(Animals):

    __tablename__='cats'
    c_eat=db.Column(db.String(32),default='fish')

    def __init__(self):
        super().__init__()

class Customer(BaseModel):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    c_name=db.Column(db.String(16))
    address=db.relationship('Address',backref='Customer',lazy=True)

class Address(BaseModel):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    a_position=db.Column(db.String(128))
    a_customer_id=db.Column(db.Integer,db.ForeignKey(Customer.id))