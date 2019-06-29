import pymongo
from pymongo import MongoClient


class MyMongoDb(object):
    '''
    pymongo 数据库通用类
    '''
    def __init__(self,address="localhost",port=27017,database='gongsi'):
        self.client = MongoClient(host=address, port=port)
        self.db = self.client[database]
    
    def db_status(self):
        '''
        数据库状态
        '''
        return self.client is not None and self.db is not None
    
    def insert_one(self,collection,data):
        '''
        向某个集合插入一条数据(增)
        '''
        if self.db_status():
            ret=self.db[collection].insert_one(data)
            return ret.inserted_id
        else:
            return None
    
    def insert_many(self,collection,data):
        '''
        向某个集合插入多条(增)
        '''
        if self.db_status():
            ret=self.db[collection].insert_many(data)
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
        if self.db_status():
            return self.db[collection].update_many(data_filter,{"$set",data_revised}).modified_count
        return None
    
    def find(self,collection,condition,column=None):
        '''
        根据条件查询某个集合的数据(查)
        '''
        if self.db_status():
            if column is None:
                return self.db[collection].find(condition)
            else:
                return self.db[collection].find(condition,column)
        else:
            return None
    
    def delete(self,collection,condition):
        '''
        根据条件删除某个集合的数据(删)
        '''
        if self.db_status():
            return self.db[collection].delete_many(filter=condition).delete_count
        return None
    
    def checkCollectionIsExist(self,collection):
        '''
        检查集合是否存在
        '''
        if self.db_status():
            if collection in self.db.list_collection_names():
                return True
            return False
        return False
    
    def __del__(self):
        if not self.db_status():
            self.client.close()

    

