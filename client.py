import socket
import sys
from urllib.request import urlopen
# this is for the attacking machine

HOST = sys.argv[1] 
PORT = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Created socket")
print("HOST: " + HOST)
print("PORT: " + str(PORT))
s.connect((HOST, PORT))
print("Connected to socket")
pwd = sys.argv[3]
res = urlopen('http://just-the-time.appspot.com/')
print("res: ", res)
time = res.read().strip().decode('utf-8')
hashed_pwd = str(hash(pwd + time))
print("Hashed pwd: " + hashed_pwd)
s.send(hashed_pwd.encode())
print("Sent password")
data = s.recv(1024).decode()
print("Received data: " + data)
if data != "done":
    print(data)
    exit()
print("Finished")
s.close()
