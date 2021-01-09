## 格式化输出 reprlib

import reprlib
print(reprlib.repr(set('abcsfsafasfafsagadasdfaas')))


## 复杂打印 pprint

import pprint
t=[[[['black','cyan'],'white',['green','red'],[['magenta','yellow'],'blue']]]]
print(pprint.pprint(t,width=30)) 


## textwrap 格式化文本段落
import textwrap

doc="""
 this is method is just like fill()
 a list a be was duke 
 sss
"""

print(textwrap.fill(doc,width=40))


## 特定地域文化相关数据格式
import locale
#locale.setlocale(locale.LC_ALL,'English States.1252')


## 字符串模板
from string import Template
t=Template('${village} folk send $$10 to $cause.')
str1=t.safe_substitute(village='Zhangsan',cause='open')
print(type(str1))
print(str1)


## Template的子类可以自定义边界
import time,os.path
photofiles=['img_1074.jpg','img_1076.jpg','img_1077.jpg']
class BatchRename(Template):
    delimiter="%"

fmt=input('Enter rename style(%d-date %-seqnum %-format):')

t=BatchRename(fmt)
date=time.strftime('%d%b%y')
for i,filename in enumerate(photofiles):
    base,ext=os.path.splitext(filename)
    newname=t.substitute(d=date,n=i,f=ext)
    print('{0}-->{1}'.format(filename,newname))
