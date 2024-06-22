import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = "postgresql://postgres:password@db:5432/mydatabase"

    class Config:
        env_file = ".env"

settings = Settings()
