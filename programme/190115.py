# def power2(x):
#     return x**2
# for x in map(lambda x:x**2,range(1,10)):
#     print(x)
# print(sum(map(lambda x:x**2,range(1,10))))

# for x in map(pow,range(1,5),range(4,0,-1)):
#     print(x)
# print(sum(map(pow,range(1,10),range(9,0,-1))))

# def is_odd(x):
#     return x%2==1
# for x in filter(lambda x:x%2==1,range(20)):
#     print(x)

# print(list(filter(lambda x:x%2==0,range(20))))
# l=list(filter(lambda x:x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0,range(2,100)))
# l1=[2,3,5,7]
# print(l1+l)

# 排序的依据为字符串的反序


# def fx(n):
#     print('递归进入第',n,'层')
#     fx(n+1)
#     print('递归退出第',n,'层')
# fx(1)

# def story():
#     print('从前有座山，山上有座庙，庙里有个老和尚，老和尚在讲故事，他讲：')
#     story()
# story()

# def age(n):
#     if n==1:
#         return 10
#     else:
#         return 2+age(n-1)

# def cd(money):
#     def buy(obj,m):
#         nonlocal money
#         if money>m:
#             money-=m
#             print('买',obj,'花了',m,'元,剩余',money,'元')
#         else:
#             print('买',obj,'失败')
#     return buy
# child=cd(2000)
# child('变形金刚',200)
# child('漫画',100)
# child('手机',1300)

# def mi(y):
#     def fn(x):
#         return x**y
#     return fn
# shu=mi(2)
# print(shu(5))
# print(shu(6))

# 1,写程序,算出1-20的阶乘的和
#  1!+2!+....20!
# def s(m):
#     l=[]
#     def jie(n):
#         if n==1:
#             return 1
#         return n*jie(n-1)
#     for n in range(1,m+1):
#         l.append(jie(n))
#     return sum(l)
# print(s(20))

# print('和是:',sum(map(s,range(1,20))))

# 2,已知列表:
#  L=[[3,5,8],10,[[13,14],15,18],20]
#  1,写一个函数print(lst)打印出所有的数字
#   (不要求打印在一行内)
#  2,以一个函数sum(lst)返回这个列表中所有数字的和
#  print(sum(L))
#  注:type(x)可以返回一个容器的类型
# L=[1,2,3]

L=[[3,5,8],10,[[13,14],15,18],20]
l1=[]
def aa(l):
    for n in l:
        if type(n) is list:
            aa(n)
        else:
            l1.append(n)
    return l1
print(aa(L))
print(sum(l1))