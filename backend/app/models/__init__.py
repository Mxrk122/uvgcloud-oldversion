# models/__init__.py

# Importa la base declarativa primero
from db.base import Base

# Luego importa los modelos específicos
from models.users import User
from models.example import Example

# Añade todos los modelos a __all__ para que sean accesibles al importar el paquete models
__all__ = ["Base", "User", "Example"]
