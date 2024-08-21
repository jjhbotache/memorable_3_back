#!/bin/bash

# Instalar Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- --default-toolchain stable -y

# Configurar el entorno de Rust
source $HOME/.cargo/env

pip install --upgrade pip setuptools wheel

# Instalar las dependencias de Python
pip install -r requirements.txt
