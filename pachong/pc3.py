from concurrent.futures import ThreadPoolExecutor
import queue
import requests
import re
import time
import hashlib
from threading import current_thread

p=ThreadPoolExecutor(10)

def get_page(url):
    print("%s Get %s:"%(current_thread().getName(),url))
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.content
    except Exception as e:
        print(e)

#抓取首页信息
def parse_index(res):
    print('%s parse index'%current_thread().getName())
    res=res.result()
    obj=re.compile('<a href="/detail/(.*?)"',re.S)
    detail_urls=obj.findall(res.decode('utf-8'))
    for detail_url in detail_urls:
        if not detail_url.startswith('http'):
            detail_url='http://www.xiaohua.com/detail/'+detail_url
        p.submit(get_page,detail_url).add_done_callback(parse_detail)

def parse_detail(res):
    print('%s parse detail '%current_thread().getName())
    print('go parse_detail')
    res=res.result()
    obj=re.compile('<p class="fonts">(.*?)</p>')
    res=obj.findall(res.decode('utf-8'))
    print('res:%s'%res)
    if len(res)>0:
        with open('duanzi.txt','a') as f:
            f.write('%s\n'%res[0])


def main():
    index_url='https://www.xiaohua.com/duanzi?page={0}'
    for i in range(2):
        p.submit(get_page,index_url.format(i,)).add_done_callback(parse_index)

if __name__ == "__main__":
    main()


