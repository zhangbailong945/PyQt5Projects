#数据特性
#1、列表

l1=list()
a=[2,3,4]
b=(5,6)
l1.append(1)
print(l1)
l1.extend(a)
print(l1)
l1.extend(b)
print(l1)

l1.insert(0,0)
print(l1)
l1.remove(0)
print(l1)

#l1.pop(0)
#print(l1)

#l1.clear()
#print(l1)

print(l1.index(1))

print(l1.count(1))

l1.reverse()
print(l1)

l2=l1.copy()

del l1
print(l2)

#列表作为栈使用(后进先出)
stack1=[2,4,5]
stack1.append(6)
stack1.append(7)
print(stack1)
print(stack1.pop())

#列表作为队列使用(先进先出)
from collections import deque

queue=deque([1,2,3,4,5])
queue.append(6)
queue.append(7)
print(queue)
print(queue.popleft())


#列表推导式
squares=[]
for x in range(10):
    squares.append(x**2)
print(x) #for 变量中的x有副作用，还能存在
print(squares)

squares1=list(map(lambda  n: n**2,range(10)))
print(squares1)
#print(n) 

squares2=[y**2 for y in range(10)]
print(squares2)
#print(y)


#嵌套的列表推导式
matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
squares3=[[row[i] for row in matrix] for i in range(4)]
print(squares3)


#删除列表元素
del squares[2:3]  #删除第二个元素
del squares[:] #清空列表 等他 squares.clear()
del squares  #删除列表变量



## 元组和序列
#元组是序列的的一种标准序列类型,不可改变值
#一个元组由几个被隔开的值组成
tuple1=1,2,3,4
print(type(tuple1))

#空元组
tuple2=()

#只有一个元素的元组
tuple3=(1,)
#或者
tuple4=1,



## 集合
#集合不重复元素组成的无序的集
#{}和set() 可以创建集合 但是空集合只能用set()

set1={'zhang','bai','bai','long','long'}
print(set1)

#集合推导式
set2={x for x in 'abracadabra' if x not in 'abc'}
print(set2)


## 字典
##字典是一个键值对的集合，键必须是唯一的。一对花括号可以创建字典。
# del 删除一个键值对
# list(d) 返回该字典中所有键的列表
#sorted(d) 倒序

dict1={'name':'zhangsan','age':25,'sex':'male'}
print(dict1)
print(list(dict1))  #返回键列表
print(sorted(dict1)) #返回倒序键列表


#字典循环
#items() 可以同时取出键和值
for k,v in dict1.items():
    print(k,v)

#enumerate(d) 可以取出索引和键
for k,v in enumerate(dict1):
    print(k,v)


#将两个相同数目的序列一起循环
dict2=['name','age','sex']
dict3=['zhangsan',25,'male']
for k,v in zip(dict2,dict3):
    print(k,v)


#reversed() 函数 逆向循环
for i in reversed(range(10)):
    print(i)