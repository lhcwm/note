# def xx(fn):
#     def ss():
#         print('*****')
#         fn()
#         print('######')
#     return ss
# @xx
# def myfunc():
#     print('函数myfunc被调用')
# # myfunc=xx(myfunc)
# myfunc()
# myfunc()
# myfunc()

# 装饰器的应用
# def check(fn):
#     def fx(n,x):
#         print('检察权限')
#         fn(n,x)
#     return fx

# def send(fn):
#     def fx(n,x):
#         fn(n,x)
#         print('发短信')
#     return fx

# @check
# def save(name,x):
#     print(name,'存钱',x,'元')

# @send
# @check
# def withdraw(name,x):
#     print(name,'取钱',x,'元')

# save('小王',200)
# save('小赵',400)
# withdraw('小李',500)

# def func(a,b,c=0):
#     '''这是func函数的文档字符串
#     参数:
#         a : 代表xxx
#         b : 代表yyy
#         ...
#     '''
#     pass

# L=[1,2,3]
# def f(n=0,lst=[]):
#     lst.append(n)
#     print(lst)
# f(4,L)
# f(5,L)
# f(100)
# f(200)
# import time
# import math as m
# r=int(input('输入半径'))
# print('圆的面积为',m.pi*r**2)
# time.sleep(10)
# s=int(input('输入面积'))
# print('半径为',m.sqrt(s/m.pi))

# import time
# y=int(input('出生年'))
# m=int(input('出生月'))
# d=int(input('出生日'))
# t=(y,m,d,8,0,0,0,0,0)
# bt=time.mktime(t)
# ls=time.time()-bt
# days=ls/3600/24
# bttu=time.localtime(bt)
# week={
#     0:'星期一',
#     1:'星期二',
#     2:'星期三',
#     3:'星期四',
#     4:'星期五',
#     5:'星期六',
#     6:'星期日'
# }
# print('出生了',days,'天')
# print('您出生的那天是',week[bttu[6]])

# 练习:
# 1,编写函数fun,其功能是计算并返回下列的和
#  sn=1+1/1!+2/2!+...1/n!
# (建议用数学模块中的math.factorial(x))
# 求当n=20时的和
# import math
# print(sum(map(lambda x:1/math.factorial(x),range(0,21))))

# 2,写一个程序,以电子时钟格式打印时间
#  格式为:
#  HH:MM:SS
# while 1:
#     import time
#     t=time.localtime()
#     print('%02d:%02d:%02d'% t[3:6],end='\r')
#     time.sleep(1)

# 3,编写一个闹钟程序,启动时设置定时时间,到时间后打印一句'时间到了',然后退出



def time():
    import time
    t=int(input('输入定时时间(s)'))
    def fn():
        nonlocal t
        if t==0:
            print('炸了')
        else:
            print(t,end='\r')
            time.sleep(1)
            t-=1
            fn()
    return fn()

time()

# def fx(fn):
#     def aa():
#         print('1')
#         fn()
#     return aa
# def fy(fn):
#     def ss():
#         print(2)
#         fn()
#     return ss

# @fy
# @fx
# def asdf():
#     print('asdfasdfas')

# asdf()