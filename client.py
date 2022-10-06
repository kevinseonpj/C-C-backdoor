import socket
import sys
from urllib.request import urlopen
import hashlib
# this is for the attacking machine

HOST = sys.argv[1] 
PORT = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
pwd = sys.argv[3].strip()
res = urlopen('http://just-the-time.appspot.com/')
time = res.read().strip().decode('utf-8')
hashed_pwd = str(hashlib.sha512((pwd + time).encode()).hexdigest())
s.send(hashed_pwd.encode())
data = s.recv(1024).decode()
if data != "done":
    s.close()
    exit()
print("Finished")
s.close()
