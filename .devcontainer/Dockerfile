# Usamos la imagen oficial de Python
FROM python:3.9-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /workspace

# Instalamos herramientas adicionales (opcional)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiamos el código fuente al contenedor
COPY . .

# Instalamos las dependencias del proyecto
RUN pip install --upgrade pip && \
    pip install pytest pytest-mock && \
    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Configura Git para usar VSCode como editor predeterminado
RUN git config --global core.editor "code --wait"

# Expone el puerto 5000 (ajusta según tu aplicación)
EXPOSE 5000

# Comando por defecto (abre una terminal interactiva)
CMD ["/bin/bash"]