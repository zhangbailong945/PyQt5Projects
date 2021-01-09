
def fibo1(n):
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
    return

def fibo2(n):
    result=[]
    a,b=0,1
    while a<n:
        result.append(a)
        a,b=b,a+b
    return result


if __name__=="__main__":
    import sys
    str1='  zhangsan '
    print(str1.zfill(5))
