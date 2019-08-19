menus=[
    {'id':1,'name':'菜单1','pid':0},
    {'id':2,'name':'菜单2','pid':0},
    {'id':3,'name':'菜单3','pid':0},
    {'id':4,'name':'菜单4','pid':0},
    {'id':5,'name':'菜单1-1','pid':1},
    {'id':6,'name':'菜单1-2','pid':1},
    {'id':7,'name':'菜单2-1','pid':2},
    {'id':8,'name':'菜单3-1','pid':3},
    {'id':9,'name':'菜单3-2','pid':3},
    {'id':10,'name':'菜单4-1','pid':4},
]

def initMenu(menuData,id,level=0):
    '''
    @params MenuData 菜单集合 \n
    @params id 菜单ID \n
    @params level 菜单层级 \n
    '''
    menuList=[]
    for menu in menuData:
        if menu['pid']==id:
            menu['level']=level
            menu['childMenu']=initMenu(menuData,menu['_id'],level+1)
            menuList.append(menu)
    return menuList

import re
def is_number(number):
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


if __name__ == "__main__":
    #allmenus=initMenu(menus,0,0)
    #a="01112"
    #print(is_number(a))
    '''
    pattern=r'^page_current=[1-9]\d*$'
    url='/user?page_num=10&page_current=1'
    url_replace='page_current=21'
    print(re.sub(r'page_current=[1-9]\d*',url_replace,url))
    if re.match(pattern,url):
        print(1111)
    '''



    