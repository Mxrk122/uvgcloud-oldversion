#!/bin/sh

# Espera hasta que la base de datos esté accesible
echo "Waiting for the database to be ready..."
while ! nc -z db 5432; do
  sleep 1
done

# Ejecuta las migraciones de Alembic
echo "Database is ready! Running migrations..."
alembic upgrade head

# Inicia la aplicación
# exec "$@"


uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload --reload-dir /project/app