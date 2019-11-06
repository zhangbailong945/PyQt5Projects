import requests
import re
import time
import hashlib


def get_page(url):
    print('Get %s'%url)
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.content
    except Exception:
        pass


def parse_index(res):
    obj=re.compile('<a href="/detail/(.*?)"',re.S)
    detail_urls=obj.findall(res.decode('utf-8'))
    for detail_url in detail_urls:
        if not detail_url.startswith('http'):
            detail_url='http://www.xiaohua.com/detail/'+detail_url
        yield detail_url


def parse_detail(res):
    obj=re.compile('<p class="fonts">(.*?)</p>')
    res=obj.findall(res.decode('utf-8'))
    print('res:%s'%res)
    if len(res)>0:
        dunzi=res[0]
        return dunzi
    else:
        print('no word!')


def main():
    index_url='https://www.xiaohua.com/duanzi?page={0}'
    for i in range(1):
        index_page=get_page(index_url.format(i,))
        detail_urls=parse_index(index_page)
        print(detail_urls)
        text=list()
        for detail_url in detail_urls:
            detail_page=get_page(detail_url)
            txt=parse_detail(detail_page)
            text.append(txt)
    print(text)

if __name__ == "__main__":
    main()








