from flask import Blueprint,render_template,redirect,url_for,request

indexView=Blueprint('indexView',__name__)


@indexView.route('/index/')
@indexView.route('/',methods=['GET','POST','DELETE'])
def index():
    return 'index'

@indexView.route('/users/<int:id>/')
def users(id):
    print(id)

    print(type(id))
    return 'users API'

@indexView.route('/getinfo/<string:token>/')
def get_info(token):
    print(token)
    print(type(token))
    return 'get Success'

@indexView.route('/getpath/<path:address>/')
def get_path(address):
    print(address)
    print(type(address))
    return 'get address'

@indexView.route('/getuuid/<uuid:uu>/')
def get_uuid(uu):
    print(uu)
    print(type(uu))
    return 'uuid'

@indexView.route('/getany/<any(a,b):an>/')
def get_any(an):
    print(an)
    print(type(an))
    return 'any'

@indexView.route('/redirect/')
def red():
    return redirect(url_for('indexView.get_any',an='a'))

@indexView.route('/getrequest/',methods=['GET','POST','DELETE','PUT'])
def get_request():
    print(request.host)
    print(request.url)
    if request.method=='GET':
        return 'get success'
    elif request.method=='POST':
        return 'post success'
    elif request.method=='DELETE':
        return 'delete success'
    else:
        return '%s Not Support'%request.method
    return 'Requrest'

def init_views(app):
    app.register_blueprint(indexView)

