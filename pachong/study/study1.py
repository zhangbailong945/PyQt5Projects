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