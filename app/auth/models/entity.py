from sqlalchemy import Column, BigInteger, Integer, VARCHAR
from db.session import Base
from common.models import CommonBase

class User(CommonBase):
    __tablename__ = "member"

    userId = Column(name = "user_id", type_ = VARCHAR, primary_key = True, nullable = False)
    password = Column(name = "user_pw", type_ = VARCHAR, nullable = False)
    name = Column(name = "user_nm", type_ = VARCHAR, nullable = False)
    email = Column(name = "user_email", type_ = VARCHAR, nullable = False)
    description = Column(name = "user_desc", type_ = VARCHAR)
    live  = Column(name = "live_gb", type_ = VARCHAR)
    active = Column(name = "use_yn", type_ = VARCHAR)
    language  = Column(name = "lang", type_ = VARCHAR)
    # age = Column(Integer)
    # ip = Column(name = "ip_address", type_ = VARCHAR(20))
    # salary = Column(NUMERIC)

class UserRole(CommonBase):
    __tablename__ = "member_role"

    userId = Column(name = "user_id", type_ = VARCHAR, nullable = False)
    id = Column(name = "role_id", type_ = Integer, primary_key = True, nullable = False)#, ForeignKey('role.role_id'))

class Role(CommonBase):
    __tablename__ = "role"

    id = Column(name="role_id", type_= BigInteger, primary_key=True)
    name = Column(name="role_nm", type_=VARCHAR)
    active = Column(name="use_yn", type_ = VARCHAR)

class Menu(CommonBase):
    __tablename__ = "menu"

    menuId = Column(name = "menu_id", type_ = VARCHAR, primary_key=True, nullable = False)
    menuNm= Column(name="menu_nm", type_ = VARCHAR)
    menuUrl = Column(name="menu_url", type_ = VARCHAR)
    ssrMenuUrl = Column(name="ssr_menu_url", type_ = VARCHAR)
    menuLevel = Column(name="menu_level", type_ = VARCHAR)
    parentMenuId = Column(name="parent_menu_id", type_ = VARCHAR)
    active = Column(name="use_yn", type_ = VARCHAR)

class MenuRole(CommonBase):
    __tablename__ = "menu_role"

    roleId = Column(name="role_id", type_ = BigInteger, primary_key= True, nullable = False)
    menuId = Column(name="menu_id", type_ = VARCHAR, primary_key= True, nullable = False)