# 1. 一个球从100米高空落下，每次落地后反弹高度为原高度的一半，再
#     落下,写程序算出:
#        1) 皮球在第10次落地后反弹的高度
#        2) 皮球在第10次落地反弹后共经历多少米路程

# def fx(a):
#     k=100
#     k1=0
#     for n in range(1,a+1):
#         k1+=k+k/2
#         k=k/2
#     print('第１０次落地后反弹的高度为：',k)
#     print('皮球在第10次落地反弹后共经历%d米路程',k1)
# fx(10)

# 2. 分解质因数.输入一个正整数，分解质因数
#     如:
#       输入: 90
#     打印：
#     　　90 = 2*3*3*5
#     (质因数是指最小能被原数整数的素数(不包括1))

# def fn(n):
#     l=[2]
#     for a in range(2,n+1):
#         for b in range(2,a):
#             if a%b==0:
#                 if a in l:
#                     l.remove(a)
#                 break
#             elif a in l:
#                 continue
#             else:
#                 l+=[a]
#     return l


# def f1(l):
#     L=[]
#     k=0
#     def fx():
#         global n
#         nonlocal k
#         a=n%(l[k])
#         if a ==0:
#             L.append(l[k])
#             n/=l[k]
#             if n in l:
#                 L.append(int(n))
#                 return L
#             else:
#                 return fx()
#         else:
#             k+=1
#             return fx()
#     return fx()


#     # if a in l:
#     #     L.append(l[k])
#     #     if a not in L:
#     #         L.append(a)
#     #     return L
#     # else:
#     #     L.append(l[k])
#     #     f1(k+1)

        


# n=int(input('输入一个正整数'))
# print(fn(n))
# print(f1(fn(n)))

# 4,打印杨辉三角,打印6层
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# def fx(k):
#     l=[1,1]
#     for a in range(2,k):
#         l1=[]
#         for b in range(0,len(l)-1):
#             l1.append(l[b]+l[b+1])
#         l=[1]+l1+[1]
#         print(l)

# k=int(input('输入层数'))
# print([1])
# print([1,1])
# fx(k)
