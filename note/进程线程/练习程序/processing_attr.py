from multiprocessing import Process
from  time import sleep,ctime

def tm():
    for i in range(3):
        sleep(2)
        print(ctime())

p=Process(target=tm,name='ggg')
print(p.name)
p.start()
print(p.pid)
p.join()