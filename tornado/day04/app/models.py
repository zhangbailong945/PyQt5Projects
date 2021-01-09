import sqlalchemy

from datetime import datetime
from sqlalchemy import Column,Integer,String,DateTime
from utils.conn import Base

def init_db():
    Base.metadata.create_all()

class User(Base):
    
    __tablename__="user"
    id=Column(Integer,primary_key=True,autoincrement=True)
    username=Column(String(20),unique=True,nullable=False)
    realname=Column(String(20),unique=True,nullable=False)
    password=Column(String(32),unique=True,nullable=True)
    create_time=Column(DateTime,default=datetime.now())

