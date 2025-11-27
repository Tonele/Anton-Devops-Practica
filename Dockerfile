# Imagen base de Python 3.12 slim (ligera)
FROM python:3.12-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de dependencias primero (optimización de caché)
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código fuente al contenedor
COPY src/ ./src/

# Dar permisos de ejecución
RUN chmod -R 755 /app

# Comando por defecto al ejecutar el contenedor (ejecutar desde /src)
CMD ["python", "src/main.py"]
