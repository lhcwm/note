import socket
def server():
    try:
    # 创建套接字
        sockfd=socket.socket()
    # 绑定地址
        sockfd.bind(('172.40.71.129',8888))
    #设置监听
        sockfd.listen(8)
    #等待处理客户端连接
        print('等待连接')
        connfd,addr = sockfd.accept()
        print('connect from',addr)
        print(connfd.getpeername())
        while 1:
    #收发消息
            data=connfd.recv(1024)
            print('receive message',data.decode())
            n=connfd.send('receive your message!!'.encode())
            print('send %d bytes' % n)

    except Exception:
        connfd.close()
        sockfd.close()
        server()

server()