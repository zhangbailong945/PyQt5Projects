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