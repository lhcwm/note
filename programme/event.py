from threading import Event,Thread
from time import sleep

s=None  #全局变量,用于通讯
e=Event()

def fun():
    print('Fun前来拜山头')
    sleep(1)
    global s
    s='天王盖地虎'
    print(s)
    e.set()

f=Thread(target=fun)
f.start()


# 主线程验证口令
print('说对口令就是自己人')
e.wait()
if s =='天王盖地虎':
    print('确认过眼神,你是对的人')
else:
    print('打死他')

# # 创建事件对象
# e=Event()
# e.set() #设置e,使wait不阻塞
# e.wait()
# print('ooooooo')
f.join()