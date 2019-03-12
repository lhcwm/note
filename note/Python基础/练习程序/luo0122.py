# try:
#     f=open('note.txt','a')
#     f.write('123\n')
#     f.writelines(['sasdf\n','dddd'])
#     f.close()
# except OSError:
#     print('打开文件失败')

# f=open('./note.txt')
# for x in f:
#     print(x)
# f.close()
# def fl(l):
#     f=open('ss.txt','w')
#     for x in l:
#         f.writelines([x['name'],',',str(x['age']),',',str(x['score']),'\n'])
#     f.close()
# L=[dict(name='xiaozhang',age=20,score=100),
#    dict(name='xiaoli',age=21,score=90)]
# fl(L)

# f=open('./ss.txt')
# for x in f:
#     print(x)
# f.close()
# import sys
# def myprint(*args,sep=' ',end='\n',file=sys.stdout):
#     flag=False
#     for x in args:
#         if flag:
#             file.write(sep)
#         file.write(str(x))
#         flag=True
#     file.write(end)


# print('1','12',5)
# myprint('1','12',5)

# f=open('note.txt','rb')
# print('当前位置',f.tell())
# b=f.read(3)
# print('当前位置',f.tell())
# f.seek(2,1)
# print('当前位置',f.tell())
# f.seek(5,0)
# print('当前位置',f.tell())
# f.close()

# 练习:
#   实现复制文件的功能
#    如:
#     请输入源文件:/home/tarena/day16.txt
#     请输入目标文件:....
#   输出:
#   复制文件成功
#   要求:
#   1,要考虑文件关闭的问题
#   2,考虑大文件的问题
#   3,要能复制二进制文件
# def mycopy(a,b):
#     a=input('输入源文件')
#     b=input('输入目标文件')
#     f1=open(a)

def fx(n):
    l=[1]
    l1=[[1]]
    for x in range(2,n+1):
        L=[]
        for y in range(len(l)-1):
            a=l[y]+l[y+1]
            L.append(a)
        l=[1]+L+[1]
        l1.append(l)
    print(l1)
    return l1

def cen(l):
    for x in l:
        z=''
        for y in x:
            z+=str(y)
        s=','.join(z)
        print(s.center(len(l[-1])*2))

k=int(input('输入层数'))


cen(fx(k))