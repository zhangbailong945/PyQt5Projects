import configparser,os


def getConfigPath(filename):
    '''
    获取*.ini文件
    '''
    return os.path.join(os.path.abspath(os.path.join(os.getcwd(),".")),filename)

class Config(object):
    '''
    *.ini文件 解析类
    '''

    def __init__(self,filename,section):
        '''
        :param filename：文件名称 \n
        :param section:属于文件的第几个section int
        '''
        self.section=section
        self.configParser=configparser.ConfigParser()
        #读取
        self.configParser.read(getConfigPath(filename),encoding='utf-8')
    
    def get_key(self,arg):
        '''
        获取属性内容 静态方法\n
        :param arg:属性名称 \n
        :return:属性的值
        '''
        parameter=self.configParser.get(self.configParser.sections()[self.section],arg)
        return parameter


