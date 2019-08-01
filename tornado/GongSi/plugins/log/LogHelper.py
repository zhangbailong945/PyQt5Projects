import os
import time
import logging
import logging.handlers

from enum import Enum



class Levels(Enum):
    '''
    日志级别枚举类
    '''

    NOTSET=logging.NOTSET
    DEBUG=logging.DEBUG
    INFO=logging.INFO
    WARNING=logging.WARNING
    ERROR=logging.ERROR
    CRITICAL=logging.CRITICAL

class AppLogger(object):

    def __init__(self,name=""):
        self.name=name
        self.logger=logging.getLogger(name=self.name)

        #创建日志文件目录
        log_dir="logs"
        if os.path.exists(log_dir) and os.path.isdir(log_dir):
            pass
        else:
            os.mkdir(log_dir)
        #日志文件名
        timestamp=time.strftime("%Y-%m-%d",time.localtime())
        filename="{}.txt".format(timestamp)
        filepath=os.path.join(log_dir,filename)
        #日志文件处理器
        rotatingFileHandler=logging.handlers.RotatingFileHandler(
            filename=filepath,
            maxBytes=1024*1024*2,
            backupCount=2,
            encoding="utf-8"
        )
        #格式化器
        formatter=logging.Formatter(
            "[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s",
            "%Y-%m-%d %H:%M:%S"
        )
        rotatingFileHandler.setFormatter(formatter)
        #控制台
        console=logging.StreamHandler()
        console.setLevel(Levels.NOTSET.value)
        console.setFormatter(formatter)
        #添加内容到文件和控制台
        self.logger.addHandler(rotatingFileHandler)
        self.logger.addHandler(console)
        self.logger.setLevel(Levels.NOTSET.value)
    
    def info(self,message):
        '''正常'''
        self.logger.info(message)
    
    def debug(self,message):
        '''调试'''
        self.logger.debug(message)
    
    def warn(self,message):
        '''警告'''
        self.logger.warn(message)
    
    def error(self,message):
        '''错误'''
        self.logger.error(message)
    
    def critical(self,message):
        '''危险'''
        self.logger.critical(message)
    
    def disable(self):
        '''停用日志'''
        self.logger.disabled=True
    
    def enable(self):
        '''开启日志'''
        self.logger.disabled=False
    
    def exception(self,message):
        self.logger.exception(message)
