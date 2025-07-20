from typing_extensions import Annotated
from fastapi import FastAPI , Body , Depends
from sqlalchemy.orm import Session, sessionmaker
from database.core import engine , SessionLocal
import todo.model
from todo.model import Todos
import users.model
from users.model import User
app = FastAPI()

todo.model.Base.metadata.create_all(bind=engine)
users.model.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
async def health_check():
    return {"status": "ok"}
