from sqlalchemy import create_engine
import os
from src.dal.base import Base
from sqlalchemy.orm import sessionmaker
from src.config.settings import settings 


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)




