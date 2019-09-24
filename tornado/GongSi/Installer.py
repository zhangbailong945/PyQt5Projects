from MyMongoDb import MyMongoDb
from plugins.common.CommonUtils import CommonUtils
import hashlib


class Installer(object):
    '''
    数据初始化器
    '''

    def __init__(self):
        self.Db = MyMongoDb()
        self.createMenu()

    def createMenu(self):
        '''
        初始化网站菜单
        '''
        collection = "menu"
        data = [
            {"pid": 0, "name": "首页", "status": 1},
            {"pid": 0, "name": "关于我们", "status": 1},
            {"pid": 0, "name": "新闻动态", "status": 1},
            {"pid": 0, "name": "产品中心", "status": 1},
            {"pid": 0, "name": "案例展示", "status": 1},
            {"pid": 0, "name": "荣誉资质", "status": 1},
            {"pid": 0, "name": "技术优势", "status": 1},
            {"pid": 0, "name": "联系我们", "status": 1},
        ]
        if not self.Db.checkCollectionIsExist(collection):
            data = self.Db.insert_many(collection, data)
            if len(data) > 0:
                print('初始化菜单成功！')
            else:
                print('初始化菜单失败！')
        return

    def createFriendlyLinks(self):
        '''
        初始化友情链接
        '''
        collection = "friendlylinks"
        data = [
            {"sitelink": "http://baidu.com", "sitename": "百度", "status": 1},
            {"sitelink": "http://baidu.com", "sitename": "百度", "status": 1},
            {"sitelink": "http://baidu.com", "sitename": "百度", "status": 1},
            {"sitelink": "http://baidu.com", "sitename": "百度", "status": 1},
            {"sitelink": "http://baidu.com", "sitename": "百度", "status": 1},
            {"sitelink": "http://baidu.com", "sitename": "百度", "status": 1},
            {"sitelink": "http://baidu.com", "sitename": "百度", "status": 1},
            {"sitelink": "http://baidu.com", "sitename": "百度", "status": 1},
        ]
        if not self.Db.checkCollectionIsExist(collection):
            data = self.Db.insert_many(collection, data)
            if len(data) > 0:
                print('初始化友情链接成功！')
            else:
                print('初始化友情链接失败！')
        return
    
    def createUserRole(self):
        '''
        初始化用户组
        '''
        collection="role"
        data = [
            {"name_en": "superadmin", "name_cn": "超级管理员", "status": 1},
            {"name_en": "administrator", "name_cn": "管理员", "status": 1},
            {"name_en": "editor", "name_cn": "编辑", "status": 1},
        ]
        if not self.Db.checkCollectionIsExist(collection):
            data = self.Db.insert_many(collection, data)
            if len(data) > 0:
                print('初始化用户组成功！')
            else:
                print('初始化用户组失败！')
        return

    def createUser(self):
        '''
        初始化用户
        '''
        collection="user"
        data = [
            {"name_en": "admin", "name_cn": "admin","password":CommonUtils.md5('admin','123456'),"group":"superadmin", "status": 1},
            {"name_en": "test1", "name_cn": "test1","password":CommonUtils.md5('test1','123456'),"group":"administrator", "status": 1},
            {"name_en": "test2", "name_cn": "test2","password":CommonUtils.md5('test2','123456'),"group":"administrator", "status": 1},
            {"name_en": "test3", "name_cn": "test3","password":CommonUtils.md5('test3','123456'),"group":"administrator", "status": 1},
            {"name_en": "test4", "name_cn": "test4","password":CommonUtils.md5('test4','123456'),"group":"editor", "status": 1},
            {"name_en": "test5", "name_cn": "test5","password":CommonUtils.md5('test5','123456'),"group":"editor", "status": 1},
            {"name_en": "test6", "name_cn": "test6","password":CommonUtils.md5('test6','123456'),"group":"editor", "status": 1},
            {"name_en": "test7", "name_cn": "test7","password":CommonUtils.md5('test7','123456'),"group":"editor", "status": 1},
            {"name_en": "test8", "name_cn": "test8","password":CommonUtils.md5('test8','123456'),"group":"editor", "status": 1},
            {"name_en": "test9", "name_cn": "test9","password":CommonUtils.md5('test9','123456'),"group":"editor", "status": 1},
            {"name_en": "test10", "name_cn": "test10","password":CommonUtils.md5('test10','123456'),"group":"editor", "status": 1},
            {"name_en": "test11", "name_cn": "test11","password":CommonUtils.md5('test11','123456'),"group":"editor", "status": 1},
            {"name_en": "test12", "name_cn": "test12","password":CommonUtils.md5('test12','123456'),"group":"editor", "status": 1},
            {"name_en": "test13", "name_cn": "test13","password":CommonUtils.md5('test13','123456'),"group":"editor", "status": 1},
        ]
        if not self.Db.checkCollectionIsExist(collection):
            data = self.Db.insert_many(collection, data)
            if len(data) > 0:
                print('初始用户组接成功！')
            else:
                print('初始化用户组失败！')
        return

