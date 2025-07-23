from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.environment import get_environment

environment = get_environment()

SQLALCHEMY_DATABASE_URL = environment.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)




