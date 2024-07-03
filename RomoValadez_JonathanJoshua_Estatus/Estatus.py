import socket
import sys
import os
from os import system
import time

os.chdir('F:/Universidad/6to semestre/Tolerante a fallas/Codigos/RomoValadez_JonathanJoshua_RestaurarEjecucion')
ip_addr = socket.gethostbyname('192.168.1.9')
portList = [5173]

while(True):
    for port in portList:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            status = sock.connect_ex((ip_addr, port))
            if status == 0:
                print(f"Port: {port} - OPEN")
            else:
                print(f"Port: {port} - CLOSED")
                system("npm run dev")
            sock.close()
        except socket.error as err:
            print(f"Connection error: {err}")    
            sys.exit()
    
    time.sleep(60)