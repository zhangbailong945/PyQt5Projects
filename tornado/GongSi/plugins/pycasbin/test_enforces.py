import casbin
import os

def get_enforcer(model=None,adapter=None,enable_log=False):
    return casbin.Enforcer(
        model,
        adapter,
        enable_log
    )

def get_model():
    return os.path.join(os.path.dirname(__file__)+"/rbac","rbac_model.conf").replace("\\","/")

def get_adapter():
    return os.path.join(os.path.dirname(__file__)+"/rbac","rbac_policy.csv").replace("\\","/")

if __name__ == "__main__":
    e=get_enforcer(get_model(),get_adapter())
    #测试策略是否存在
    print(e.enforce('zhangsan', 'index', 'get'))
    #输出用户的角色列表
    print(e.get_roles_for_user('admin'))
    #print(e.add_policy('zhangsan','index','post'))

    print(e.enforce('zhangsan', 'index', 'post'))

    