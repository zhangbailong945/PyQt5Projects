#brak continue else
'''
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,'equals',x,'*',n//x)
            'break
    else:
        print(n,'is a prime number')
'''


'''
for n in range(2,20):
    if n % 2 ==0:
        print(n,'is even number!')
        continue
    print('found a number',n)

'''

#def() 


def f(a,L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def f2(a,L=None):
    if L is None:
        L=[]
    L.append(a)
    return L

print(f2(1))
print(f2(2))
print(f2(3))


## /之前仅限位置， /之后为位置或者其他参数 *之后为仅限关键字参数
def def1(a,b):
    return a*b

print(def1(1,3))

## * 之后的形参 仅限关键字
def def2(*,b):
    print(b)

print(def2(b=3))


args1=[3,6]
print(list(range(*args1)))

def def3(a:int,b:int)->int:
    return a+b

print(def3(3,5))


def4=lambda x:x+2

print(def4(2))


#总结
'''
1.正式形参 def f1(a):
2.参数默认值 def f2(a=1):
3.关键字参数 def f3(a,name='zhansan',age=25)
4.元组参数 def f4(a,*args)
5.字典参数 def f5(a,*args,**kwargs)
6.特殊参数 如果函数定义中未使用 /和* ，则参数可以按位置或按关键字传递函数
7. /之前必须是仅限位置参数，/之后可以是位置或者关键字
8.要将形参标记为仅限关键字，则在参数列表的第一个形参之前放置*


'''