import socket
import os
import sys
# this is for the attacking machine

HOST = sys.argv[1] 
PORT = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
pwd = sys.argv[3]
s.send(pwd.encode())
data = s.recv(1024).decode()
if data != "done":
    print(data)
    exit()

s.close()
