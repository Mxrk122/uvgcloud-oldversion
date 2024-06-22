# Usa la imagen base de Python 3.9
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /project

# Copia los archivos de requerimientos e instálalos usando pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia los archivos de la aplicación al contenedor
COPY ./app ./app
COPY alembic ./alembic


WORKDIR /project/alembic

# Ejecuta las migraciones de Alembic para configurar la base de datos
RUN alembic upgrade head

WORKDIR /project

# Expone el puerto 8000 en el contenedor (puedes ajustar esto según sea necesario)
EXPOSE 8000

# Comando para ejecutar la aplicación FastAPI usando Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
