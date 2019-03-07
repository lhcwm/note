from multiprocessing import Process
from socket import *
import signal

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',6789))
s.listen(3)
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

def fun(c):
    pass

# 循环等待客户端连接
while True:
    try:
        c,addr=s.accept()
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)
        continue
    p=Process(target=fun,args=(c,))
    p.daemon=True
    p.start()