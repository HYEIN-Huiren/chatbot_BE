from sqlalchemy import Boolean, VARCHAR
from common.models import CommonBase
from db.session import Base
from sqlalchemy.orm import Mapped, mapped_column
from pgvector.sqlalchemy import Vector

class Chat(CommonBase):
    __tablename__ = "chat_service"

    uuid: Mapped[str] = mapped_column(primary_key=True, nullable= False)
    projectCode: Mapped[str] = mapped_column(VARCHAR(10), nullable= False)
    userId: Mapped[str] = mapped_column(VARCHAR, nullable = False)
    question: Mapped[str] = mapped_column(VARCHAR(100), nullable= False)
    active: Mapped[str] = mapped_column(Boolean, nullable= False)
    sql: Mapped[str] = mapped_column(VARCHAR(100), nullable= True)
    answerType: Mapped[str] = mapped_column(VARCHAR(5), nullable= False)
    answer: Mapped[str] = mapped_column(VARCHAR(500), nullable= False)
    embedding: Mapped[list[float]] = mapped_column(Vector, nullable= False)

class Projects(Base):
    __tablename__ = "projects"

    projectCode: Mapped[str] = mapped_column(VARCHAR(10), primary_key=True, nullable = False)
    projectName: Mapped[str] = mapped_column(VARCHAR(30), nullable = False)

class Keywords(CommonBase):
    __tablename__ = "keywords"
    
    uuid: Mapped[str] = mapped_column(primary_key=True, nullable= False)
    projectCode: Mapped[str] = mapped_column(VARCHAR(10), nullable= False)
    question: Mapped[str] = mapped_column(VARCHAR(100), nullable= False)

class ProjectAdmin(Base):
    __tablename__ = "chat_admin"

    projectCode: Mapped[str] = mapped_column(VARCHAR(10), primary_key=True, nullable = False)
    adminId: Mapped[str] = mapped_column(VARCHAR(30), nullable = False)