from sqlalchemy import Column, Integer, String
from app.db.base import Base

class User(Base):
    __tablename__ = 'examples'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)
