from plugins.db.MongoHelper import MongoHelper
from plugins.config.Config import Config

class UserModel(MongoHelper):
    '''
    用户model
    '''

    def __init__(self):
        super(UserModel,self).__init__()
        self.col='user'
    
    def get_user(self):
        return self.get_collection(self.col)