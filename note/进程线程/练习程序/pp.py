from socket import *
from select import select
s=socket()
s.bind(('0.0.0.0',6789))
s.listen()

rlist=[s]
wlist=[]
xlist=[]

while True:
    rs,ws,xs=select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            c,addr=r.accept()
            rlist.append(c)
        else:
            data=r.recv(1024)
            if not data:
                r.close()
                rlist.remove(r)
                continue
            print(data.decode())
            wlist.append(r)
    for w in ws:
        w.send(b'ok')
        wlist.remove(w)