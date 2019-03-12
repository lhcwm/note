from multiprocessing import Process,Array
import time

# 创建共享内存
# shm= Array('i',[1,2,3,4,6])
# 指定开辟空间大小
# shm=Array('i',5)
# 存入字符串
shm=Array('c',b'hello')

def fun ():
    for i in shm:
        print(i)
    shm[4]=b'k'

p=Process(target=fun)
p.start()
p.join()
print(shm.value) #打印字符串
for i in shm:
    print(i)
