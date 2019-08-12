
import math

class Pagination:
    '''
    分页类
    '''

    _page_total=None #总记录数
    _page_num=None #每页显示条数
    _page_current=None #当前页
    _page_sum=None #总页数
    _page_first=None #首页
    _page_last=None #尾页
    _page_url=None #当前url
    _page_show=None #页面显示格式
    _page_skip=1 #mongo skip(num).limit(num)



    def __init__(self,page_total=1,page_num=1,page_current=1,page_url=None,page_show=2):
        self._page_total=int(page_total)
        self._page_num=int(page_num)
        self._page_current=int(page_current)
        self._page_sum=math.ceil(self._page_total/self._page_num) #分页总数=总记录数/每页显示条数 向上取整

        if self._page_total<0:
            self._page_total=0

        if self._page_current<1:
            self._page_current=1

        if self._page_sum<1:
            self._page_sum=1
        
        if self._page_current>self._page_sum:
            self._page_current=self._page_sum
        
        self.skip=(self._page_current-1)*page_num
        self._page_first=self._page_current-self._page_show
        self._page_last=self._page_current+self._page_show

        if self._page_first<1:
            self._page_last=self._page_last+(1-self._page_first)
            self._page_first=1

        if self._page_last>self._page_sum:
            self._page_first=self._page_first-(self._page_last-self._page_sum)
            self._page_last=self._page_sum
        
        if self._page_first<1:
            self._page_first=1
        
    
    def is_num(self,number):
        if isinstance(int(number),int):
            return number
        return 1

