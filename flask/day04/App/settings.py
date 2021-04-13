import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



def get_db_uri(db_info):
    '''获取数据库驱动'''
    engine=db_info.get('ENGINE') or 'sqlite'
    driver=db_info.get('DRIVER') or ''
    user=db_info.get('USER') or ''
    password=db_info.get('PASSWORD') or ''
    host=db_info.get('HOST') or ''
    port=db_info.get('PORT') or ''
    name=db_info.get('NAME') or ''
    return "{}+{}://{}:{}@{}:{}/{}".format(engine,driver,user,password,host,port,name)


class Config:
    '''基础配置'''
    DEBUG=False
    TESTING=False
    STAGING=False
    PRODUCT=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevelopConfig(Config):
    DEBUG=True
    dbinfo={
        "ENGINE":"mysql",
        "DRIVER":"pymysql",
        "USER":"root",
        "PASSWORD":"root",
        "NAME":"mytest",
        "HOST":"localhost",
        "PORT":"3306"
    }

    SQLALCHEMY_DATABASE_URI=get_db_uri(dbinfo)

class TestingConfig(Config):
    DEBUG=True
    dbinfo={
        "ENGINE":"mysql",
        "DRIVER":"pymysql",
        "USER":"root",
        "PASSWORD":"root",
        "NAME":"mytest",
        "HOST":"localhost",
        "PORT":"3306"
    }

    SQLALCHEMY_DATABASE_URI=get_db_uri(dbinfo)

class StagingConfig(Config):

    dbinfo={
        "ENGINE":"mysql",
        "DRIVER":"pymysql",
        "USER":"root",
        "PASSWORD":"root",
        "NAME":"mytest",
        "HOST":"localhost",
        "PORT":"3306"
    }

    SQLALCHEMY_DATABASE_URI=get_db_uri(dbinfo)

class ProductConfig(Config):

    dbinfo={
        "ENGINE":"mysql",
        "DRIVE":"pymysql",
        "USER":"root",
        "PASSWORD":"root",
        "NAME":"mytest",
        "HOST":"localhost",
        "PORT":"3306"
    }

    SQLALCHEMY_DATABASE_URI=get_db_uri(dbinfo)



envs={
    "default":DevelopConfig,
    "develop":DevelopConfig,
    "testing":TestingConfig,
    'staging':StagingConfig,
    "product":ProductConfig
}