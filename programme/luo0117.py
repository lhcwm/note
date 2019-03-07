# def myfac(n):
#     print('正在计算%d的阶乘'%n)

# def mysum(n):
#     print('正在计算1+2+3+..+%d的和'%n)
# name1='audi'
# name2='tesla'
# print('模块被加载')

# import random as r
# x=r.randint(1,100)
# k=1
# while 1:
#     y=int(input('猜个数'))
#     if x==y:
#         if k==1:
#             print('我靠,太能蒙了')
#         elif 1<k<5:
#             print('牛B,这么快就猜出来了')
#         else:
#             print('哈哈,被玩了吧!\n你猜了%d次'%k)
#         break
#     elif x>y:
#         print('猜小了')
#     else:
#         print('猜大了')
#     k+=1
# print('luo0117')
# from ..note.lianxi import a
# print(a)
# from random import choice as ch
# la=list(map(lambda x:chr(x) , range(ord('a'),ord('z')+1)))
# lA=list(map(lambda x:chr(x) , range(ord('A'),ord('Z')+1)))
# l1=list(range(0,10))
# l=la+lA+l1
# print(ch(l),ch(l),ch(l),ch(l),ch(l),ch(l))

# 2,模拟斗地主发牌,牌共54张
# 种类:
#  黑桃('\u2660'),梅花('\u2663'),方块\u2665 ,红桃(\u2666)
# 数字
#  A2-10JQK
# 王牌:大小王
# 三个人,每人发17张牌,底牌留三张
# 输入回车,打印第一个人的17张牌
# .
# .
# 输入回车,打印3张底牌


def fx():
    L=['\u2660','\u2663','\u2665','\u2666']
    l=[str(x) for x in range(2,11)]
    l+=['A','J','Q','K',]
    w=['大王','小王']
    pai=[x+y for x in L for y in l]
    P=pai+w
    from random import shuffle as sh
    sh(P)
    k=1
    while True:
        i=input('按回车键发牌')
        if k==1:
            f=P[0:17]
        elif k==2:
            f=P[17:34]
        elif k==3:
            f=P[34:51]
        else:
            print('底牌:\n%s' % P[51:54])
            break
        print('第%d个人的牌:\n%s' % (k,sorted(f,key=lambda x:x[1])))
        k+=1
print('斗地主游戏开始')
fx()