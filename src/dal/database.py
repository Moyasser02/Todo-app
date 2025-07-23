from dal.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.environment import get_environment
from sqlalchemy.ext.asyncio import create_async_engine

environment = get_environment()

SQLALCHEMY_DATABASE_URL = environment.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)




