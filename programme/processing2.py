from multiprocessing import Process
from time import sleep

def work(sec,name):
    for i in range(3):
        sleep(sec)
        print(name)
p=Process(target=work,kwargs={'name':'adf','sec':1})
# p =Process(target=work,args=(2,'afsf'))
p.start()
p.join()