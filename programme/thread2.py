from threading import Thread
from time import sleep,ctime

class Mythread(Thread):
    def __init__(self,target=None,args=(),kwargs={},name='Thread-1'):
        super().__init__()
        self.target=target
        self.args=args
        self.kwargs=kwargs
        self.name=name

    def run(self):
        self.target(*self.args,**self.kwargs)

def fun(sec,song):
    for i in range(3):
        print ('Play %s:%s'%(song,ctime()))
        sleep(1)

t=Mythread(target=fun,args=(3,),kwargs={'song':'lili'},name='happy')
t.start()
t.join()