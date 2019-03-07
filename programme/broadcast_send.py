from socket import *
from time import sleep

dest=('172.40.71.255',9999)
s=socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
data = '道路千万条,安全第一条'
while 1:
    sleep(2)
    s.sendto(data.encode(),dest)
s.close()
