#!/bin/bash

# Actualizar el sistema
echo "Actualizando el sistema..."
sudo apt update && sudo apt upgrade -y

# Verificar e instalar Python
echo "Verificando instalación de Python..."
if ! command -v python3 &> /dev/null
then
    echo "Python3 no está instalado. Instalando Python3..."
    sudo apt install python3 -y
else
    echo "Python3 ya está instalado."
fi

# Verificar e instalar pip
echo "Verificando instalación de pip..."
if ! command -v pip3 &> /dev/null
then
    echo "pip3 no está instalado. Instalando pip3..."
    sudo apt install python3-pip -y
else
    echo "pip3 ya está instalado."
fi

# Instalar los módulos necesarios de Python
echo "Instalando módulos de Python necesarios..."
pip3 install itertools colorama termcolor

# Verificar e instalar GoBuster
echo "Verificando instalación de GoBuster..."
if ! command -v gobuster &> /dev/null
then
    echo "GoBuster no está instalado. Instalando GoBuster..."
    sudo apt install gobuster -y
else
    echo "GoBuster ya está instalado."
fi

# Descargar DirSearch si no está presente
if [ ! -d "dirsearch" ]; then
    echo "Descargando DirSearch..."
    apt install dirsearch
    echo "DirSearch descargado."
else
    echo "DirSearch ya está presente."
fi

echo "Instalación completada. Los requisitos para el script están configurados."
