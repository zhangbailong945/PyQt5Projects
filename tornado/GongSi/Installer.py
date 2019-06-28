from MyMongoDb import MyMongoDb


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
