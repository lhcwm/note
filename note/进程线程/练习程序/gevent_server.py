import gevent
from gevent import monkey
monkey.patch_all() #执行脚本插件,修改原有阻塞行为
from socket import *
# 创建套接字
def server():
    s=socket()
    s.bind(('0.0.0.0',6789))
    s.listen(4)
    while True:
        c,addr=s.accept()
        print('connect from ',addr)
        gevent.spawn(handle,c)

def handle(c):
    while True:
        data=c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'ok')
    c.close()

server()
