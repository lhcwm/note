import multiprocessing as mp
from time import sleep
import os
# 编写进程函数
def f1():
    sleep(3)
    print('111')
    print(os.getppid(),'---',os.getpid())
    # 创建进程对象

def f2():
    # sleep(2)
    print(input('>>'))
    print(os.getppid(),'---',os.getpid())

def f3():
    sleep(4)
    print('33')
    print(os.getppid(),'---',os.getpid())
f=[f1,f2,f3]
pro=[]
for x in f:
    p=mp.Process (target=x)
    pro.append(p)
    p.start()

for p in pro:
    p.join()
