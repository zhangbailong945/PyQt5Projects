from modules.BaseModule import BaseModule

class MenuModule(BaseModule):
    '''
    主页->菜单模块
    '''

    def getMenus(self):
        '''
        获取菜单集合
        '''
        collection='menu'
        condition={"status":1}
        return self.dbHelper.find(collection,condition)

    def initLevelMenu(self,menuData,id,level=0):
        '''
        @params MenuData 菜单集合 \n
        @params id 菜单ID \n
        @params level 菜单层级 \n
        '''
        menuList=[]
        for menu in menuData:
            if menu['pid']==id:
                menu['level']=level
                menu['childMenu']=self.initLevelMenu(menuData,menu['_id'],level+1)
                menuList.append(menu)
        return menuList

    def render(self):
        menuData=self.getMenus()
        menus=self.initLevelMenu(menuData,0,0)
        html=""
        for menu in menus:
            html+='<li class=""><a href="" class="topa">'+menu["name"]+'</a>'
            if len(menu['childMenu'])>0:
                html+=self.getChild(menu['childMenu'])
                html+="</li>"
            else:
                html+='<ul style="display:none"></ul></li>'
        return html
    
    def getChild(self,menus):
        '''
        递归 子菜单
        '''
        html="<ul class='drop-menu'>"
        for menu in menus:
            html+='<li class=""><a href="javascript:;" class="topa">'+menu["name"]+'</a>'
            if len(menu['childMenu'])>0:
                html+=self.getChild(menu['childMenu'])
                html+="</li>"
            else:
                html+='<ul style="display:none"></ul></li>'
        html+="</ul>"
        return html