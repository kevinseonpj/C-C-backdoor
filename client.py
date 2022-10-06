import socket
import os
import sys
# this is for the attacking machine

HOST = sys.argv[1] 
PORT = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Created socket")
s.connect((HOST, PORT))
print("Connected to socket")
pwd = sys.argv[3]
s.send(pwd.encode())
data = s.recv(1024).decode()
print("Received data: " + data)
if data != "done":
    print(data)
    exit()
print("Finished")
s.close()
