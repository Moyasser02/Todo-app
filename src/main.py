from typing_extensions import Annotated
from fastapi import FastAPI , Body , Depends
from sqlalchemy.orm import Session, sessionmaker
from dal.database import engine , SessionLocal
import dal.models.todo_model
from dal.models.todo_model import Todos
import dal.models.todo_model
from dal.models.user_model import User
from dal.deps import get_db
from controllers import user_controller
from exceptions.exceptions import ApplicationException, application_exception_handler
app = FastAPI()

dal.models.todo_model.Base.metadata.create_all(bind=engine)
dal.models.user_model.Base.metadata.create_all(bind=engine)

app.add_exception_handler(ApplicationException, application_exception_handler)
app.include_router(user_controller.router)

@app.get("/")
async def health_check():
    return {"status": "ok"}
