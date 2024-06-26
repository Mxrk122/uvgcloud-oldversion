# app/api/users.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db import crud
from app.models.users import User
from app.schemas.users import UserCreate  
import uuid

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def user_root():
    return {"Hello": "Users"}

@router.post("/create_user/", response_model=None)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user.email, user.password)

@router.get("/get_user/{user_email}", response_model=None)
def read_user(user_email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
