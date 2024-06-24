# models/users.py

from sqlalchemy import Column, Integer, String
from db.base import Base  # Asegúrate de que la importación sea correcta

class User(Base):
    __tablename__ = 'Users'
    
    __table_args__ = {'extend_existing': True}  # <-- Añade esta línea

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)
        