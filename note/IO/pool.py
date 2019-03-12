from multiprocessing import Pool
from time import sleep,ctime

#进程事件
def worker(msg):
    sleep(2)
    print(msg)
    # return ctime()
print(ctime())
# 创建进程池
pool=Pool()

# l=[]
# 向进程池添加事件
for i in range(10):
    msg='hello %d'%i
    p=pool.apply_async(func=worker,args=(msg,))
    # l.append(p)
    # print(l)
# 关闭进程池
pool.close()
# 回收
pool.join()
print(ctime())