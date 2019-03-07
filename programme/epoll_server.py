from socket import *
from select import *
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',6666))
s.listen()

# 创建poll对象
p=epoll()
# 建立查找字典
fdmap={s.fileno():s}
# 注册IO
p.register(s,EPOLLIN|EPOLLERR)
# 循环监控
while True:
    events=p.poll()  #阻塞
    for fd,ev in events:  
        if fd ==s.fileno():
            c,addr = fdmap[fd].accept()
            print('connect from',addr)
            # 添加新的注册IO
            p.register(c,EPOLLIN|EPOLLHUP|EPOLLET)
            fdmap[c.fileno()]=c
        elif ev & EPOLLHUP:
            print('客户端退出')
            p.unregister(fd)   #取消关注
            fdmap[fd].close()
            del fdmap[fd]
        elif ev & EPOLLIN:
            data=fdmap[fd].recv(1024)
            print('receive:',data.decode())
            fdmap[fd].send('收到'.encode())