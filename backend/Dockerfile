# Usa una imagen base con Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /project

# Instala netcat y otras dependencias del sistema
RUN apt-get update && apt-get install -y netcat-openbsd

# Copia los archivos necesarios al contenedor
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia los archivos de Alembic
COPY ./alembic /project/alembic
COPY alembic.ini /project/alembic.ini

# Copia el script para esperar a la base de datos
COPY wait_for_db.sh /project/wait_for_db.sh
RUN chmod +x /project/wait_for_db.sh

# Ejecuta las migraciones con Alembic
# RUN alembic -c /project/alembic.ini upgrade head

# Expone el puerto de la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["./wait_for_db.sh", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--reload-dir", "/project/app"]
