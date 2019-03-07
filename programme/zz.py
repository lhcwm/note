from select import select
from socket import *
import sys
from time import ctime 

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',6666))
s.listen(3)

rlist=[s,sys.stdin]
wlist=[]
xlist=[]
f=open('zz.txt','a')

print('等待连接')
while True:
    try:
        rl,wl,xl=select(rlist,wlist,xlist)
    except KeyboardInterrupt:
        break
    for r in rl:
        if r is s:
            c,addr=r.accept()
            print('建立连接',addr)
            rlist.append(c)
        elif r is c:
            data=r.recv(1024)
            if not data:
                r.close()
                rlist.remove(r)
                continue
            print('收到客户端消息:',data.decode())
            f.write(ctime()+'  '+data.decode()+'\n')
            f.flush()
            wlist.append(r)
        else:
            f.write(ctime()+'  '+r.readline())
            f.flush()
    for w in wl:
        w.send('收到消息'.encode())
        wlist.remove(w)
s.close()
f.close()