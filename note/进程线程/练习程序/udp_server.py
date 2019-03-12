# import socket
from socket import *
sockfd =socket(AF_INET,SOCK_DGRAM)
sockfd.bind(('172.40.71.129',8888))
while 1:
    print('等待接收消息')
    data,addr = sockfd.recvfrom(1024)
    print ('接收到%s的消息为:%s'% (addr,data.decode()))
    sockfd.sendto('收到消息'.encode(),addr)

sockfd.close()