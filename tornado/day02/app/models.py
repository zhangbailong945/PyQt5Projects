
from utils.conn import Base
from sqlalchemy import Column,String,Integer
from utils.conn import Base

def create_db():
    Base.metadata.create_all()

def drop_db():
    Base.metadata.drop_all()

class Student(Base):

    id=Column(Integer,primary_key=True,autoincrement=True)
    s_name=Column(String(10),unique=True,nullable=False)
    s_age=Column(Integer,default=18)

    __tablename__='student'

