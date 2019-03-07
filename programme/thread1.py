from threading import Thread
from time import sleep

def fun():
    sleep(1)
    print ('线程测试')

t=Thread(target=fun,name='tarena')

print('thread name',t.name)
t.setName('teda')
print('thread name',t.getName())
# 设置daemon
t.setDaemon(True)
t.start()
# t.join()
print('alive',t.is_alive())