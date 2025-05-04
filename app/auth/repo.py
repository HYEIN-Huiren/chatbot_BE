from auth.models.entity import User, UserRole, Menu, MenuRole, Role
from sqlalchemy.orm import Session

def loadUserByUserId(db: Session, userId: str):
    user: User = db.query(User).filter_by(userId = userId).first()
    return user

def getUserRole(db: Session, userId: str):
    user: User = db.query(UserRole).filter_by(userId = userId).first()
    return user.roleId

def getMenuList(db: Session, userId: str):
    query = db.query(Menu).select_from(Role).join(UserRole, UserRole.id == Role.id)
    query = query.join(MenuRole, Role.id == MenuRole.roleId)
    query = query.join(Menu, MenuRole.menuId == Menu.menuId)
    query = query.where(UserRole.userId == userId).distinct()

    menus = query.all()
    top = []
    mid = []
    last = []

    for menu in menus:
        menu=menu.__dict__
        del menu['modifyDate'], menu['modifyId']
        del menu['registId'], menu['registDate']
        if not menu.get("parentMenuId"):
            top.append(menu)
        elif menu.get('menuLevel') == "1":
            mid.append(menu)
        else:
            last.append(menu)

    if len(last) != 0:
        menuList = __makeChild(mid, last)
        menuList = __makeChild(top, menuList)
    else:
        menuList = __makeChild(top, mid)
    return menuList

def __makeChild(parent, child):
    import copy
    temp = copy.deepcopy(parent) 
    for menu in temp:
        if menu.get('menuLevel') == '0' or menu.get("active") == 'Y':
            for item in child:
                if item.get("active") == 'Y':
                    if item.get('parentMenuId') == menu.get('menuId'):
                        if menu.get('children'):
                            menu['children'].append(item)
                        else:
                            menu['children'] = [item]
                    if not item.get('children'):
                        item['children'] = None
        if not menu.get('children'):
            menu['children'] = None
    return temp