import os
from time import sleep
pid =os.fork()
if pid<0:
    print('create process failed')
elif pid==0:
    sleep(4)
    print('The new process')
else:
    sleep(3)
    print('The old process')

print('fork test over')