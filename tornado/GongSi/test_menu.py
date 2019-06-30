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


if __name__ == "__main__":
    allmenus=initMenu(menus,0,0)
    