import time
from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
from app.db.session import engine
from app.routes import users
from fastapi.middleware.cors import CORSMiddleware

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configurar CORS
origins = [
    "http://localhost",
    "http://localhost:666",  # Agrega aquí la URL de tu frontend en React
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Montar las rutas de los usuarios
app.include_router(users.router, prefix="/users", tags=["users"])

# Example route
@app.get("/")
def read_root():
    return {"Hello": "World"}