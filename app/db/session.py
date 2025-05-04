from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base # Base 생성
from core.config import settings

config = settings()
# engine = create_engine(config.get('DB_URL'))
engine = create_engine(config.get('DBR_URL'))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()