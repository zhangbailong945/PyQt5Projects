import pymongo
from pymongo import MongoClient

class MongoHelper(object):

    def __init__(self,mongodb_config):
        self.__connect=None
        self.__mongodb_config=mongodb_config
        self.__reconnect()
    
    def __connect_mongo(self,mongodb_config):
        host=mongodb_config['host']
        port=mongodb_config['port']
        user=mongodb_config['user']
        pwd=mongodb_config['pwd']
        db_name=mongodb_config['db_name']

        #认证连接MONGODB方式
        client=MongoClient(host,int(port))
        db_handler=client[db_name]
        db_handler.authenticate(user,pwd)
        return db_handler
    
    def __reconnect(self):
        try:
            self.__connect=self.__connect_mongo(self.__mongodb_config)
            return self.__connect
        except Exception as ex:
            print(ex)
        return None
    
    def get_db_connect(self):
        if self.__connect:
            return self.__connect
        else:
            return self.__reconnect()
    
    def get_collection(self,col_name):
        col_handler=None
        if self.__connect:
            col_handler=self.__connect[col_name]
        else:
            col_handler=None
        return col_handler



if __name__ == "__main__":
    mongodb_config={
        "host":'localhost',
        "port":'27017',
        "user":'admin',
        "pwd":'password',
        "db_name":'test'
    }

    dbHelper=MongoHelper(mongodb_config)
    table=dbHelper.get_collection("goods")
    for good in table.find():
        print(good)

    