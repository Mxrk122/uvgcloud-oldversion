from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Importa todos los modelos aquí para que Alembic los detecte
from app.models.users import User
