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
    print(e.enforce('alice', 'data1', 'read'))
    print(e.get_roles_for_user('alice'))