from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor,Executor

def gcd(pair):
    a,b=pair
    low=min(a,b)
    for i in range(low,0,-1):
        if a%i==0 and b%i==0:
            return i

numbers=[
    (1234,4422),
    (58,39),
    (2,9),
    (12,36)
]

import time

if __name__ == "__main__":
    '''
    start=time.time()
    results=list(map(gcd,numbers))
    end=time.time()
    print('Took %.3f seconds.'%(end-start))
    print(results)
    '''
    #Took 0.001 seconds.

    #多线程版
    '''
    
    start=time.time()
    pool=ThreadPoolExecutor(max_workers=2)
    results=list(pool.map(gcd,numbers))
    end=time.time()
    print('Took %.3f seconds.'%(end-start))
    print(results)
    '''
    #Took 0.010 seconds.

    #多进程版
    start=time.time()
    pool=ProcessPoolExecutor(max_workers=2)
    results=list(pool.map(gcd,numbers))
    end=time.time()
    print('Took %.3f seconds.'%(end-start))
    print(results)
    #Took 0.296 seconds.


