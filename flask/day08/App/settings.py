import os,datetime

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_db_uri(db_info):
    engine=db_info.get('ENGINE') or ''
    driver=db_info.get('DRIVER') or ''
    user=db_info.get('USER') or ''
    password=db_info.get('PASSWORD') or ''
    host=db_info.get('HOST') or ''
    port=db_info.get('PORT') or ''
    name=db_info.get('NAME') or ''
    return "{}+{}://{}:{}@{}:{}/{}".format(engine,driver,user,password,host,port,name)

class Config:
    DEBUG=True
    TESTING=False
    DEVELOP=False
    SECRET_KEY='loach'
    PERMANENT_SESSION_LIFETIME=datetime.timedelta(14)
    SQLALCHEMY_TRACK_MODIFICATIONS=False


class DevelopConfig(Config):
    DEVELOP=True
    db_info={
        'ENGINE':'mysql',
        'DRIVER':'pymysql',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'localhost',
        'PORT':3306,
        'NAME':'mytest'
    }
    SQLALCHEMY_DATABASE_URI=get_db_uri(db_info)



envs={
    'develop':DevelopConfig,
    'default':DevelopConfig
}