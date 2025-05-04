
from sqlalchemy import func, Column, TIMESTAMP, VARCHAR
from sqlalchemy.orm import declared_attr, as_declarative

from pydantic import BaseModel
from fastapi import Response

@as_declarative()
class CommonBase(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    
    def get_userId(context):
        return context.get_current_parameters()["userId"]
        
    registDate = Column(name = "reg_dt", nullable=False, type_ = TIMESTAMP, default=func.now()) # 이걸로 적용됨
    modifyDate = Column(name = "mod_dt", nullable=False, type_ = TIMESTAMP, default=func.now(), onupdate=func.now())
    registId = Column(name = "reg_id", type_ = VARCHAR, default = get_userId)
    modifyId = Column(name = "mod_id", type_ = VARCHAR, default = get_userId)


# from __future__ import annotations
# from pydantic import BaseModel


# class OuterClass:
#     class Student(BaseModel):
#         name: str
#         age: int

#     class StudentRequest(BaseModel):
#         ...
#         students: list[OuterClass.Student]


# OuterClass.StudentRequest.update_forward_refs()
    
class CommonResponse(BaseModel):
    message: str | None
    data: object | None
    pageInfo: str | None
    isSuccess: bool