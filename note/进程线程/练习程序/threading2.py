from threading import Thread
from time import sleep

# 含有参数的线程函数
def fun (sec,name):
    print('线程传参')
    sleep(sec)
    print('%s的线程执行完毕'%name)
# 创建多个线程
l=[]
for i in range(5):
    t=Thread(target=fun,args=(2,),kwargs={'name':'T%d'%i})
    l.append(t)
    t.start()

for i in l:
    i.join()    
