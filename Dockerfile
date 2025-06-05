# Imagen base oficial de Python
FROM python:3.11-slim

# Variables de entorno para evitar la creación de archivos pyc y buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY . /app

# Instalar dependencias
RUN pip install --upgrade pip \
 && pip install fastmcp httpx

# Comando por defecto
#CMD ["uv", "run", "server.py"]
CMD ["python", "server.py"]
