import hashlib
from plugins.config.Config import Config


class CommonUtils(object):
    '''
    工具类
    '''

    @staticmethod
    def md5(username,password):
        '''
        md5 摘要算法 \n
        :param username 账号 \n
        :param password 口令 \n
        :return hashlib.md5(password)
        '''
        md5=hashlib.md5()
        md5_str=username+password+Config('config.ini',2).get_key('salt') #加盐
        md5.update(md5_str.encode('utf-8')) #编码，否则报错
        return md5.hexdigest()

