from multiprocessing import Pool
import time 
from thread_test import *

start=time.time()
pool=Pool()
r=pool.map(count(0,0),list(range(10)))
pool.close()
pool.join()
end=time.time()
t1=end-start
print('进程池计算密集型时间:',t1)

pool=Pool()
r=pool.map(do(),list(range(10)))
pool.close()
pool.join()
end2=time.time()
t2=end2-end
print('进程池IO密集型时间:',t2)