# def myyield():
#     yield 2
#     print('函数运行结束')


# g=myyield()
# print(g)

# def my(n):
#     i=0
#     while i<n:
#         yield i
#         i+=1

# for x in my(3):
#     print(x)

# def myeven(b,e):
#     while b<e:
#         if b%2==0:
#             yield b
#         b+=1
# for x in myeven(2,10):
#     print(x)

# L=[2,3,5,7]
# def fx(l):
#     for x in l:
#         x=x**2+1
#         yield x

# l1=list(fx(L))
# l2=(x**2+1 for x in L)
# print(l1)
# print(list(l2))

# def fn(fx,x):
#     for a in x:
#         if fx(a):
#             yield a
# for x in fn(lambda x:x%2==0,range(10)):
#     print(x)

# l =[2,3,5,7]
# A=[x*10 for x in l]
# it=iter(A)
# print(next(it))  #20
# l[1]=33
# print(next(it))  #30

# l =[2,3,5,7]
# A=(x*10 for x in l)
# it=iter(A)
# print(next(it))  #20
# l[1]=33
# print(next(it))  #330

# def myenu(a,start=0):
#     for x in a:
#         yield (start,x)
#         start+=1

# L=[3,5,8,10]
# for i,v in myenu(L):
#      print(i,v)

f=open('myfile.txt')
print('文件打开成功')

s=f.readline()
print(s,len(s))

# f.close()
# print('文件关闭成功')

# 1,写一个生成器函数myrange(start,stop,step)来生成一些列整数
#   功能与range完全相同
#   用myrange求1-10内的奇数的平方和

# def myrange(start,stop=None,step=1):
#     if stop is None:
#         s=0
#         while s<start:
#             yield s
#             s+=step
#     else:
#         if step>0:
#             while start<stop:
#                 yield start
#                 start+=step
#         else:
#             while start>stop:
#                 yield start
#                 start+=step
# print(sum(x**2 for x in myrange(4,1,-1) if x%2==1))

