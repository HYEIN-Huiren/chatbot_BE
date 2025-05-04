from pydantic import BaseModel
from pydantic import BaseModel
# from common.models import CommonModel

class LoginRequest(BaseModel):
    userId: str = "admin"
    password: str = "123456"

class Menu(BaseModel):
    parentMenuId: str | None
    menuLevel: str
    menuId: str
    menuNm: str
    menuUrl: str | None
    ssrMenuUrl: str | None
    children: list | None

class Token(BaseModel):
    refreshToken: str | None

# class UserRole(CommonModel):
#     userId: str
#     roleId: str

# getter
class Menu(BaseModel):
    __menuId: str
    __menuName: str
    __menuUrl: str
    __menuLevel: str
    __parentmMenuId: str

    def __init__(self, menuId: str, menuName: str, menuUrl: str, menuLevel: str, parentMenuId: str):
        super().__init__()
        self.__menuId = menuId
        self.__menuName = menuName
        self.__menuUrl = menuUrl
        self.__menuLevel = menuLevel
        self.__parentmMenuId = parentMenuId
    
    @property
    def menuId(self):
        return self.__menuId
    
    @property
    def menuName(self):
        return self.__menuName
    
    @property
    def menuUrl(self):
        return self.__menuUrl
    
    @property
    def menuLevel(self):
        return self.__menuLevel
    
    @property
    def parentMenuId(self):
        return self.__parentmMenuId