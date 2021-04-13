from App.Models.animals import Animals,Cats,Dogs,Customer,Address
from flask import Blueprint,render_template,request,Response
from sqlalchemy import text,and_,or_,not_
import random
from App.ext import cache

animalsView=Blueprint('animalsView', __name__)

@animalsView.route('/animals/index/')
def index():
    return Response('<h1>animals</h1>')

@animalsView.route('/animals/addCat/')
def addCat():
    cat=Cats()
    cat.a_name='加菲猫'
    cat.c_eat='骨头'
    cat.add()
    return Response('add a dog successed!')


@animalsView.route('/animals/addDog/')
def addDog():
    dog=Dogs()
    dog.d_legs=4
    dog.a_name='傻狗'
    dog.add()
    return Response('add a cat successed!')


@animalsView.route('/animals/addDogs/')
def addDogs():
    for i in range(20):
        dog=Dogs()
        dog.a_name='二哈%d'%random.randrange(10000)
        dog.add()

    return Response('add more dogs successed!')

@animalsView.route('/animals/getCatsById/')
def getCatsById():
    # cats=Cats.query.filter(Cats.id.__lt__(2)).all()
    # cats=Cats.query.filter(Cats.a_name.startswith('大'))
    # cats=Cats.query.filter(Cats.a_name.endswith('器猫'))
    # cats=Cats.query.filter(Cats.id.in_([1,2,3]))
    # cats=Cats.query.filter(Cats.a_name.like('%菲猫'))
    cats=Cats.query.order_by('id').offset(1).limit(4)
    print(cats)
    print(type(cats))
    return render_template('/animals/cats.html',cats=cats)

@animalsView.route('/animals/getdogs/')
def getDogs():
    page=request.args.get('page',default=1,type=int)
    per_page=request.args.get('per_page',default=4,type=int)
    dogs=Dogs.query.offset(per_page*(page-1)).limit(per_page)

    return render_template('/animals/dogs.html',dogs=dogs)


@animalsView.route('/animals/pages/')
def get_dogs_pages():
    page=request.args.get('page',default=1,type=int)
    per_page=request.args.get('per_page',default=4,type=int)
    
    dogs=Dogs.query.offset(per_page*(page-1)).limit(per_page)
    pagination=Dogs.query.paginate(page=page,per_page=per_page)
    return render_template('/animals/dogs.html',dogs=dogs,pagination=pagination,per_page=per_page)


@animalsView.route('/animals/getcatsfilterby/')
def get_cats_filter_by():
    cats=Cats.query.filter_by(id=5)
    return render_template('/animals/cats.html',cats=cats)

@animalsView.route('/animals/addCustomer/')
def addCustomer():
    customer=Customer()
    customer.c_name='剁手党%d'%random.randrange(100)
    customer.add()
    return Response('添加客户成功!')


@animalsView.route('/animals/addAddress/')
def addAddress():
    address=Address()
    address.a_position='地址%d'%random.randrange(100)
    address.a_customer_id=Customer.query.order_by(text("-id")).first().id
    address.add()
    return Response('添加地址成功!%s'%address.a_position)


@animalsView.route('/animals/getcustomer/')
def getCusotmer():
    a_id=request.args.get('a_id',type=int)
    address=Address.query.get_or_404(a_id)
    customer=Customer.query.get(address.a_customer_id)
    return customer.c_name


@animalsView.route('/animals/getaddress/')
def getAddress():
    c_id=request.args.get('c_id',type=int)
    customer=Customer.query.get(c_id)
    # address=Address.query.filter_by(a_customer_id=c_id)
    address=customer.address
    print(type(address))
    return render_template('/animals/address.html',address=address)

@animalsView.route('/animals/getaddresswithcon/')
@cache.cached(timeout=60)
def get_address_with_con():
    # address=Address.query.filter(Address.a_customer_id.__eq__(2)).filter(Address.a_position.endswith('4'))
    # address=Address.query.filter(and_(Address.a_customer_id.__eq__(1),Address.a_position.endswith('4')))
    # address=Address.query.filter(or_(Address.a_customer_id.__eq__(1),Address.a_position.endswith('4')))
    address=Address.query.filter(not_(or_(Address.a_customer_id.__eq__(1),Address.a_position.endswith('4'))))
    print('从数据库查下')
    return render_template('/animals/address.html',address=address)