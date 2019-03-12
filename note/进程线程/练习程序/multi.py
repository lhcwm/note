from multiprocessing import Process
import os

# def fun(file1,file2,n):
#     f=open(file1,'rb')
#     F=open(file2,'wb')
#     f.seek(0,2)
#     size=f.tell()
#     if n==1:
#         f.seek(0,0)
#         s=f.read(size//2)
#         F.write(s)
#     else:
#         f.seek(size//2,0)
#         s=f.read()
#         F.write(s)
#     f.close()
#     F.close()
    

file1='carlist.txt'
file2='day02_copy.txt'
file3='day02_copy2.txt'

size=os.path.getsize(file1)

def top():
    f=open(file1,'rb')
    n=size//2
    fw=open(file2,'wb')
    while True:
        if n<1024:
            data=f.read(n)
            fw.write(data)
            break

        data=f.read(1024)
        fw.write(data)
        n-=1024
    f.close()
    fw.close()


def boot():
    f=open(file1,'rb')
    n=size//2
    fw=open(file3,'wb')
    f.seek(size//2,0)
    while True:
        data=f.read(1024)
        if not data:
            break
        fw.write(data)
    f.close()
    fw.close()

p1=Process(target=top)
p2=Process(target=boot)

p1.start()
p2.start()
p1.join()
p2.join()
f=open(file2,'r')
f.seek(0,2)
size=f.tell()
print(size)
f.close()