import configparser,os

def getConfigPath(filename):
    return os.path.join(os.path.abspath(os.path.join(os.getcwd(),".")),filename)

class Config(object):

    def __init__(self,filename,section):
        '''
        :param filename：文件名称 \n
        :param section:属于文件的第几个section int
        '''
        self.section=section
        self.configParser=configparser.ConfigParser()
        #读取
        self.configParser.read(getConfigPath(filename))
    
    def get_Config(self,arg):
        '''
        获取属性内容 \n
        :param arg:属性名称 \n
        :return:属性的值
        '''
        parameter=self.configParser.get(self.configParser.sections()[self.section],arg)
        return parameter

if __name__ == "__main__":
    config=Config('config.ini',0)
    print(config.get_Config('host'))

