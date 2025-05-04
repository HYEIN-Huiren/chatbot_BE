from sqlalchemy import Column, Date, Integer, Boolean, NUMERIC, VARCHAR
from db.session import Base
from common.models import CommonBase

class UserProject(Base):
    __tablename__ = "legacy_data"
    __table_args__ = dict(schema="chatbot")

    index= Column(name = "data_seq", type_ = NUMERIC, primary_key = True, nullable= False)
    userId = Column(name = "member_id", type_ = VARCHAR, nullable = False)
    code = Column(name = "project_code", type_ = VARCHAR(5), nullable = False)

class Projects(Base):
    __tablename__ = "project_list"
    __table_args__ = dict(schema="chatbot")

    code = Column(name = "project_code", type_ = VARCHAR(5), primary_key=True, nullable = False)
    name = Column(name = "project_name", type_ = VARCHAR, nullable = False)

class Questions(CommonBase):
    __tablename__ = "prev_question"
    __table_args__ = dict(schema="chatbot")
    
    index= Column(name = "question_seq", type_=Integer, primary_key=True, nullable = False)
    question= Column(name = "question", type_ = VARCHAR(200), nullable = False)
    date = Column(name="updateday", type_=Date)
    userId = Column(name = "member_id", type_ = VARCHAR(50), nullable = False)
    active = Column(name = "use", type_ = Boolean, nullable = False)