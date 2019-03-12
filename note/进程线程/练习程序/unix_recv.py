from socket import *
#确定套接字文件
sock_file='uuu'
# 创建本地套接字
sockfd=socket(AF_UNIX,SOCK_STREAM)
# 绑定套接字文件
sockfd.bind(sock_file)
# 监听,连接
sockfd.listen(3)
while True:
    c,addr=sockfd.accept()
    while True:
        data=c.recv(1024)
        if not data:
            break
        print(data.decode())
    c.close()
