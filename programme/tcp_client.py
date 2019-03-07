from socket import *
from time import sleep

#创建套接字
sockfd=socket(AF_INET,SOCK_STREAM,0)

#发起连接
server_addr=('172.40.71.129',6789)
sockfd.connect(server_addr)
while True:
#收发消息
    file=input('输入文件名')
    if not file:
        break
    F=open(file,mode='rb')
    sockfd.send(file.encode())
    sleep(1)
    for x in F:
        sockfd.send(x)
    F.close()
    #
    sleep(1)
    print('kong')
    sockfd.send('##'.encode())
sockfd.close()      