from multiprocessing import Semaphore,Process
import time
import os

# 创建信号量
sem=Semaphore(3)

def fun():
    print('%d想执行事件'%os.getpid())
    # 想执行事件必须得到信号量资源
    sem.acquire()
    print('%d抢到了信号量.可以执行操作'%os.getpid())
    time.sleep(2)
    print('%d执行完事件在增加信号量'%os.getpid())
    sem.release()

jobs=[]
for i in range(5):
    p=Process(target=fun)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()

print(sem.get_value())