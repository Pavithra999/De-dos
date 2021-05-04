#just in case you are using it for eduserver or something please dont
#eduserver IP address = 103.241.136.151

import socket
import threading
import sys, os, time, shodan
from platform import system

osname = system()
if(osname == 'Windows'):
    cmd = 'cls'
else:
    cmd = 'clear'

os.system(cmd)