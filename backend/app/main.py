import time
from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# Database setup
DATABASE_URL = "postgresql://postgres:password@db:5432/mydatabase"
engine = None

# Function to check if PostgreSQL is ready
def check_postgres():
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect():
            print("Connected to PostgreSQL!")
            return engine
    except Exception as e:
        print(f"PostgreSQL is not ready yet: {e}")
        return None

# Wait until PostgreSQL is ready
while not (engine := check_postgres()):
    time.sleep(1)  # Wait for 1 second before retrying

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Example route
@app.get("/")
def read_root():
    return {"Hello": "World"}
