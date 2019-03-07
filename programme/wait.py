import os
from time import sleep
pid=os.fork()
if pid <0:
    print('error')
elif pid==0:
    print('child %d process exit'% os.getpid())
    sleep(2)
    os._exit(2)
else:
    #非阻塞等待
    while True:
        pid,status=os.waitpid(-1,os.WNOHANG)
        if pid != 0:
            break
        sleep(2)
        print('afdas')
    while True:
        print('zuoqitashiqing')
        sleep(2)