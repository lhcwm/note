from socket import *

sockfd=socket(AF_INET,SOCK_DGRAM)
print(sockfd.family)
print(sockfd.type)
print(sockfd.fileno())
# sockfd.setsockopt(SQL_SOCKET,SO_REUSEADDR,1)

while True:
    data = input ('Msg>>')
    if not data:
        break
    sockfd.sendto(data.encode(),('172.40.71.255',8888))
    msg,addr=sockfd.recvfrom(1024)
    print('收到的消息为:',msg.decode())
sockfd.close()
