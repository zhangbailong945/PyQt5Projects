
import re,math

class Pagination:
    '''
    分页类
    '''

    _page_total=1 #总记录数
    _page_num=1 #每页显示条数
    _page_current=1 #当前页
    _page_sum=1 #总页数
    _page_first=1 #首页
    _page_last=1 #尾页
    _page_url='' #当前url
    _page_show=2 #页面显示格式
    _page_skip=0 #mongo skip(num).limit(num)



    def __init__(self,page_total=1,page_num=1,page_current=1,page_url='',page_show=2):
        self._page_url=page_url
        self._page_total=self.is_number(page_total)
        self._page_num=self.is_number(page_num)
        self._page_current=self.is_number(page_current)
        self._page_sum=math.ceil(self._page_total/self._page_num) #分页总数=总记录数/每页显示条数 向上取整
        self._page_show=self.is_number(page_show)
        self._page_url=page_url
        
        if self._page_current==1:
            self._page_skip=0
        else:
            self._page_skip=self._page_current*self._page_num #skip(num) 等于当前页*每页显示数

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
        
    
    def is_number(self,number):
        '''
        判断url分页参数，是否为数字
        '''
        if isinstance(number,int):
            return number
        elif isinstance(number,str):
            pattern=r"^[1-9]\d*$"
            if (re.match(pattern,number)):
                return int(number)
            else:
                return 1
        else:
            return 1
    
    def __page_replace(self,page):
        page=str(page)
        return self._page_url.replace("{page}",page)

    def __page_home(self):
        '''
        首页
        '''
        if self._page_current!=1:
            return "<a class='prev' href='"+self.__page_replace(1)+"'>首页</a>"
        else:
            return ""
    
    def __page_prev(self):
        '''
        上一页
        '''
        if self._page_current!=1:
            return "<a class='prev' href='"+self.__page_replace(self._page_current-1)+"'>上一页</a>"
        else:
            return ""
    
    def __page_next(self):
        '''
        下一页
        '''
        if self._page_current!=self._page_sum:
            return "<a class='next' href='"+self.__page_replace(self._page_current+1)+"'>下一页</a>"
        else:
            return ""
    
    def __page_last(self):
        '''
        尾页
        '''
        if self._page_current!=self._page_sum:
            return "<a class='num' href='"+self.__page_replace(self._page_sum)+"'>尾页</a>"
        else:
            return ""
    
    def show_pages(self):
        page_str="<div>"
        page_str+=self.__page_home()
        page_str+=self.__page_prev()
        if self._page_first>1:
            page_str+="<p>...</p>"
        num=self._page_first
        while(num<=self._page_last):
            if num==self._page_current:
                page_str+="<a class='current' href='"+self.__page_replace(num)+"'>"+str(num)+"</a>"
            else:
                page_str+="<a class='num' href='"+self.__page_replace(num)+"'>"+str(num)+"</a>"
            num+=1
        if self._page_last<self._page_sum:
            page_str+="..."
        page_str+=self.__page_next()
        page_str+=self.__page_last()
        page_str+='</div>'
        return page_str

    
    

if __name__ == "__main__":
    page=Pagination(page_total=1,page_num=1,page_current=1,page_url='{page}',page_show=2)
    print(page.show_pages())
