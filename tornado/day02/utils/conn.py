
#pymongo://localhost:27017

import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



db_url='mysql+pymysql://root:root@localhost:3306/tornado'

#建立连接
engine=create_engine(db_url)
#模型与数据库进行关联的基类
Base=declarative_base(bind=engine)


#创建回话
DbSession=sessionmaker(bind=engine)
session=DbSession()