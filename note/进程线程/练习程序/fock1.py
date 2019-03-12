# import os
# from time import sleep
# pid = os.fork()
# if pid <0:
#     print('error')
# elif pid==0:
#     print('child pid',os.getpid())
#     print('get ppid',os.getppid())
#     os._exit(1)
# else:
#     print('parent pid',os.getpid())
#     print('get child pid',pid)
#     while True:
#         pass

import os
pid =os.fork()
if pid <0:
    print('error')
elif pid=0:
    print('child pid')
else:
    print('parent pid')