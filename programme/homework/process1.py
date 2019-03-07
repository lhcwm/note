from multiprocessing import Process,Pool
from time import time
from thread_test import *

l=[]
start=time()
for i in range(20):
    p=Process(target=count,args=(0,0))
    l.append(p)
    p.start()
for i in l:
    i.join()
end=time()
t1=end-start
print('进程计算密集型时间:',t1)

l=[]
for i in range(20):
    p=Process(target=do)
    l.append(p)
    p.start()
for i in l:
    i.join()
end2=time()
t2=end2-end
print('进程IO密集型时间:',t2)