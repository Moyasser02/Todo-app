
from database.core import Base 
from sqlalchemy import Column, Integer, String , Boolean

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String, nullable=True)  # Optional field
    hashed_password = Column(String)  # Store hashed password securely
    is_active = Column(Boolean, default=True)  # User is active by default
    role = Column(String, default="user")  # Default role is 'user'