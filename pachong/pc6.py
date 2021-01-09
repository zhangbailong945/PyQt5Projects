from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor,as_completed

from urllib.request import urlopen
import re

urls=[
    'https://www.baidu.com',
    'https://www.sina.com',
    'https://www.hupu.com',
    'https://www.taobao.com'
]


def load_url(url,timeout):
    with urlopen(url,timeout=timeout) as conn:
        return conn.read()

with ThreadPoolExecutor(max_workers=4) as tpool:
    future_to_url={tpool.submit(load_url,url,60):url for url in urls}
    for future in as_completed(future_to_url):
        url=future_to_url[future]
        try:
            data=future.result()
            obj=re.compile('<title>(.*?)</title>')
            title=obj.findall(data.decode('utf-8'))
            if len(title)>0:
                title=title[0]
            else:
                title=None
        except Exception as exc:
            print('%r generated an exception:%s'%(url,exc))
        else:
            print('%r title is %s '%(url,title))