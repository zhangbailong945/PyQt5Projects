import time
from concurrent.futures import ThreadPoolExecutor

def wait_on_b():
    time.sleep(5)
    print(b.result(0))
    return 5

def wait_on_a():
    time.sleep(5)
    print(a.result())
    return 6

tpool=ThreadPoolExecutor(max_workers=2)

a=tpool.submit(wait_on_b)


b=tpool.submit(wait_on_a)