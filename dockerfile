# Usa una imagen base con Python
FROM python:3.12-slim

# Instalar dependencias necesarias para Rust y la construcción de Python
RUN apt-get update && \
    apt-get install -y curl build-essential

# Instalar Rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- --default-toolchain stable -y

# Configurar el entorno de Rust
ENV PATH="/root/.cargo/bin:${PATH}"

# Configurar el directorio de trabajo
WORKDIR /app

# Copiar archivos de requisitos
COPY requirements.txt .

# Actualizar pip y instalar dependencias de Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copiar el código del proyecto
COPY . .

# Comando para ejecutar tu aplicación
CMD ["python", "main.py"]
