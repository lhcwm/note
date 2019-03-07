import signal
import os

signal.signal(signal.SIGCHLD,signal.SIG_IGN)

pid =os.fork()

if pid ==0:
    print ('child pid',os.getpid())
else:
    while 1:
        pass