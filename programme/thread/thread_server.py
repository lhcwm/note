from socket import *
from threading import Thread

# 创建套接字
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',6789))
s.listen(5)

# 客户端处理函数
def handle(c):
    print('connect from',c.getpeername())
    while True:
        data=c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'ok')
    c.close()

# 循环等待客户端连接
while True:
    try:
        c,addr=s.accept()
    except KeyboardInterrupt:
        s.close()
        break
    except Exception as e:
        print(e)
        continue

    # 创建线程处理客户端请求
    t=Thread(target=handle,args=(c,))
    t.setDaemon(True)
    t.start()