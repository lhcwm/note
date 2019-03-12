from thread_test import *
from time import time

start=time()
for i in range(20):
    count(0,0)
end=time()
t1=end-start
print('单进程计算密集型时间:',t1)
for i in range(20):
    do()
end2=time()
t2=end2-end
print('单进程IO密集型时间:',t2)