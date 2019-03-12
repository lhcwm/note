# 第一题：
# k=0
# for a in range (1,5):
#     for b in range (1,5):
#         for c in range (1,5):
#             if a!=b and a!=c and b!=c:
#                 print('%d%d%d' % (a,b,c))
#                 k+=1
# print('这样的数一共有%d个' % k)

# 第二题：
# name='tarena'
# pw='123'
# k=3
# while k>0:
#     n=input('用户名：')
#     p=input('密码：')
#     if n==name and p==pw:
#         print('登录成功')
#         break
#     else:
#         k-=1
#         if k>0:
#             print('输入错误,您还有%d次机会' % k)
# else:
#     print('登陆失败')

# 第三题：
# name=' alax '
# a=name.strip()
# print(a)
# b=name.startswith('al')
# print(b)
# c=name.endswith('X')
# print(c)
# d=name.replace('l','p')
# print(d)
# e=name.split('l')
# print(e)
# g=name.upper()
# print(g)
# h=name.lower()
# print(h)
# i=name[1]
# print(i)
# j=name[:3]
# print(j)
# k=name[-1:-3:-1]
# print(k)
# l=name.find('e')
# print(l)


# 第四题：
# n=int(input('输入数字'))
# if 1<= n <=7:
#     if n==6 or n==7:
#         print('周末')
#     else:
#         print('工作日')
# else:
#     print('错误')

# 第六题：
# x=int(input('第一个数'))
# y=int(input('第二个数'))
# z=int(input('第三个数'))
# a=max(x,y,z)
# c=min(x,y,z)
# if x!=y and x!=z and y!=z:
#     for b in (x,y,z):
#         if a>b>c:
#             print('%d<%d<%d' % (c,b,a))
# else:
#     print('请输入三个不同的数')

# 第七题
# y=int(input('哪年'))
# m=int(input('哪月'))
# d=int(input('哪日'))
# a=[31,28,31,30,31,30,31,31,30,31,30,31]
# if 1<=m<=12 and d<=31:
#     s=sum (a[:(m-1)])
#     if m>2:
#         if y%4==0 and y%100!=0 or y%400==0:
#             s+=1
#     s+=d
#     print('这是这年的第%d天'%s)
# else:
#     print('输入错误')

#  第八题：奖金问题
# r=int(input("输入奖金"))
# a=[1000000,600000,400000,200000,100000,0]
# b=[0.01,0.015,0.03,0.05,0.075,0.1]
# x=0
# for k in range(0,6):
#     if r>a[k]:
#         m=(r-a[k])*(b[k])
#         x+=m
#         r=a[k]
# print('奖金是',x,'元')