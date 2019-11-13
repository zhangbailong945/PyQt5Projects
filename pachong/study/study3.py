## 模块

from fibo import fibo1,fibo2
'''
with open('txt.txt','w') as f:
    f.write('ssss')
'''
with open('txt.txt','r') as f:
    print(f.read())

import json

json_data=json.dumps([1,'zhangsan','list'])
f=open('json.txt','w')
json.dump([1,'zhangsan','list'],f)
f.close()
print(json_data)

f2=open('json.txt','r')
json1=json.load(f2)
print('json1:%s'%json1)
f2.close()