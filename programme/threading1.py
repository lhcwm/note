import threading
from time import sleep
import os

a=1
# 线程函数
def music():
    global a
    print(a)
    a=1000
    for i in range(5):
        sleep(2)
        print('播放出山',os.getpid())

# 创建线程对象
t=threading.Thread(target=music)
t.start()
# 主线程运行任务
for i in range(3):
    sleep(3)
    print('播放流浪',os.getpid())
t.join()
print(a)