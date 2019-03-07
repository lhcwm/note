from socket import *
from time import sleep,ctime

sockfd = socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(3)

#设置非阻塞状态
sockfd.setblocking(False)

#设置超时时间
sockfd.settimeout(10)

while True:
    print('waiting for connect')
    try:
        connfd,addr=sockfd.accept()
    except BlockingIOError:
        sleep(2)
        print('%s connect error'% ctime())
        continue
    except timeout:
        print('超时了')
    else:
        print('connect from',addr)