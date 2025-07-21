from sqlalchemy import create_engine
import os
from src.dal.base import Base
from sqlalchemy.orm import sessionmaker
from src.config.environment import get_environment

environment = get_environment()

SQLALCHEMY_DATABASE_URL = environment.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)




