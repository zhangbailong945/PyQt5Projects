import casbin
import os

from mongodb_adapter.adapter import Adapter
from mongodb_adapter.adapter import CasbinRule

def get_enforcer(model=None,adapter=None,enable_log=False):
    
    return casbin.Enforcer(
        model,
        adapter,
        enable_log
    )

def get_model():
    return os.path.join(os.path.dirname(__file__)+"/rbac","rbac_model.conf").replace("\\","/")

def get_adapter():
    #return os.path.join(os.path.dirname(__file__)+"/rbac","rbac_policy.csv").replace("\\","/")
    adapter=Adapter(dbname='gongsi',host='localhost',port=27017)
    return adapter

if __name__ == "__main__":
    model=get_model()
    print(model)
    adapter=Adapter(dbname='gongsi',host='localhost',port=27017)
    e=get_enforcer(model,adapter)
    #测试策略是否存在
    #print(e.enforce('admin', 'index', 'get'))
    #输出用户的角色列表
    #print(e.get_roles_for_user('admin'))
    #print(e.add_policy('zhangsan','index','post'))

    #print(e.enforce('admin', 'index', 'post'))
    #adapter=get_adapter()
    #adapter.add_policy(sec=None,ptype='g',rule=['viewer','index','get'])
    #e.add_policy('viewer','index','post') #ok

    print(e.get_all_roles()) #ok

    #print(e.add_policy('zhangsan','index','post'))

    