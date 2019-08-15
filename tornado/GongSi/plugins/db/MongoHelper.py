import pymongo
from pymongo import MongoClient
from plugins.config.Config import Config

class MongoHelper(object):

    def __init__(self):
        self.__connect=None
        self.__mongodb_config=self.get_mongodb_config()
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

    def get_mongodb_config(self):
        mongodb_config=dict()
        mongodb_config['host']=Config('config.ini',0).get_key('host')
        mongodb_config['port']=Config('config.ini',0).get_key('port')
        mongodb_config['user']=Config('config.ini',0).get_key('user')
        mongodb_config['pwd']=Config('config.ini',0).get_key('password')
        mongodb_config['db_name']=Config('config.ini',0).get_key('db_name')
        return mongodb_config

    
    def __reconnect(self):
        '''
        建立连接
        '''
        try:
            self.__connect=self.__connect_mongo(self.__mongodb_config)
            return self.__connect
        except Exception as ex:
            print(ex)
        return None
    
    def get_db_connect(self):
        '''
        连接mongodb
        '''
        if self.__connect:
            return self.__connect
        else:
            return self.__reconnect()
    
    def get_collection(self,col_name):
        '''
        获取集合 \n
        :param col_name 集合名字 \n
        :return collection 集合
        '''
        col_handler=None
        if self.__connect:
            col_handler=self.__connect[col_name]
        else:
            col_handler=None
        return col_handler

    def insert_one(self,collection,data):
        '''
        向某个集合插入一条数据(增)
        '''
        if self.__connect:
            ret=self.__connect[collection].insert_one(data)
            return ret.inserted_id
        else:
            return None
    
    def insert_many(self,collection,data):
        '''
        向某个集合插入多条(增)
        '''
        if self.__connect:
            ret=self.__connect[collection].insert_many(data)
            return ret.inserted_ids
        else:
            return None
    
    def update(self,collection,data):
        '''
        更新某个集合的数据(改)
        '''
        data_filter={}
        data_revised={}
        for key in data.keys():
            data_filter[key]=data[key][0]
            data_revised[key]=data[key][1]
        if self.__connect:
            return self.__connect[collection].update_many(data_filter,{"$set",data_revised}).modified_count
        return None
    
    def find(self,page,collection,condition,column=None):
        '''
        根据条件查询某个集合的数据(查)
        '''
        if self.__connect:
            if column is None:
                print(page._page_skip)
                return list(self.__connect[collection].find(condition).skip(page._page_skip).limit(page._page_num))
            else:
                print(page._page_skip)
                return list(self.__connect[collection].find(condition,column).skip(page._page_skip).limit(page._page_num))
        else:
            return None
    
    def delete(self,collection,condition):
        '''
        根据条件删除某个集合的数据(删)
        '''
        if self.__connect:
            return self.__connect[collection].delete_many(filter=condition).delete_count
        return None

    def count(self,collection):
        '''
        返回集合总数
        '''
        if self.__connect:
            return self.__connect[collection].find().count()
        return None


'''
if __name__ == "__main__":
    mongodb_config={
        "host":'localhost',
        "port":'27017',
        "user":'admin',
        "pwd":'password',
        "db_name":'test'
    }

    dbHelper=MongoHelper()
    table=dbHelper.get_collection("goods")
    for good in table.find():
        print(good)
    print(db.find("ut", {}).count())
    print(db.update("ut", {"password": ["aaaa", "bbbb"]}))
    print(db.find("ut", {}, {"password": 1, "username": 1}).count())

'''  