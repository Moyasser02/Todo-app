from dal.base import Base 
from sqlalchemy import Column, Integer, String, Boolean , ForeignKey

class Todos(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    completed = Column(Boolean, default=False)
    priority = Column(Integer, default=1)  
    owner_id = Column(Integer, ForeignKey("users.id"))