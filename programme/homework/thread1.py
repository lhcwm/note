from threading import Thread
from time import time
from thread_test import *


l=[]
start=time()
for i in range(20):
    p=Thread(target=count,args=(0,0))
    l.append(p)
    p.start()
for i in l:
    i.join()
end=time()
t=end-start
print('线程计算密集型时间:',t)

l=[]
for i in range(20):
    p=Thread(target=do)
    l.append(p)
    p.start()
for i in l:
    i.join()
end2=time()
t2=end2-end
print('线程IO密集型时间:',t2)