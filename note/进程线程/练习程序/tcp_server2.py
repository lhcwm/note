from socket import *
sockfd=socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# 绑定地址
sockfd.bind(('172.40.71.129',6789))
#设置监听
sockfd.listen(8)
#等待处理客户端连接
while 1:
    print('等待连接')
    try:
        connfd,addr = sockfd.accept()
    except KeyboardInterrupt :
        print('Server close')
        break
    print('connect from',addr)
    while 1:
        print('等待传输')
        file=connfd.recv(1024)
        if not file:
            break
        F=open('copy_'+file.decode(),'wb')
        while 1:
            data=connfd.recv(1024)
            if data=='##'.encode():
                break
            F.write(data)

        F.close()
        print('文件传输完毕')
    connfd.close()
sockfd.close()
