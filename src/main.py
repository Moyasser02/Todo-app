from typing_extensions import Annotated
from fastapi import FastAPI , Body , Depends
from sqlalchemy.orm import Session, sessionmaker
from dal.database import engine , SessionLocal
import dal.models.todo_model
from dal.models.todo_model import Todos
import dal.models.todo_model
from dal.models.todo_model import User
app = FastAPI()

dal.models.todo_model.Base.metadata.create_all(bind=engine)
dal.models.todo_model.Base.metadata.create_all(bind=engine)

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
