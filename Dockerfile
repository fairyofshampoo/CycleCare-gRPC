# Imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar virtualenv
RUN pip install virtualenv

# Crear y activar el entorno virtual
RUN python -m venv env
ENV PATH="/app/env/bin:$PATH"

# Copiar archivos necesarios y scripts de inicialización
COPY . .

# Instalar las dependencias desde requirements.txt
COPY requirements.txt .
RUN . env/bin/activate && pip install -r requirements.txt

# Generar los módulos Python del protocol buffer (si es necesario)
RUN . env/bin/activate && python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/video.proto

# Exponer el puerto en el que corre el servidor gRPC
EXPOSE 3000

# Comando para ejecutar el servidor gRPC
CMD ["sh", "-c", ". env/bin/activate && python server.py"]