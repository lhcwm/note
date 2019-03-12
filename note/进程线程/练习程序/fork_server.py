from socket import *
import os,sys
import signal

# 创建监听套接字
HOST='0.0.0.0'
PORT=6789
ADDR=(HOST,PORT)

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

signal.signal(signal.SIGCHLD,signal.SIG_IGN)

# 客户端处处理函数
def client_handle(c):
    print ('客户端',c.getpeername())
    while True: 
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Receive message')
    c.close()

#循环等待客户端连接 
while True:
    try:
        c,addr=s.accept()
    except KeyboardInterrupt:
        sys.exit('服务器退出')
    except Exception as e:
        print(e)
        continue
    # 创建子进程处理客户端请求
    pid=os.fork()

    if pid==0:
        s.close()
        client_handle(c)
        os._exit(0)
    else:  #无论父进程或者创建进程失败都是循环接受新的连接
        c.close()