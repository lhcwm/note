# a =input('输入字符串')
# k=0
# j=0
# for n in a:
#     if n==' ':
#         k+=1
#     if 'A'<=n<='Z' or 'a'<=n<='z':
#         j+=1
# print('空格个数为%d个，英文字母为%d个' % (k,j))


# 输入字符串，从尾向头输出这个字符串的字符
# n=input('输入字符串')
# a=n[::-1]
# for k in a :
#     print(k)

# 用ｆｏｒ语句打印１－２０的整数，打印在一行内
# for a in range(1,21):
#     print(a,end=' ')
# print()

# 求１００以内有哪些整数与自身＋１的乘积再对１１求余的结果等于８？打印出这些数。
# for n in range(101):
#     if n*(n+1)%11==8:
#         print(n)

# 计算１００内奇数的和　分别用ｆｏｒ和ｗｈｉｌｅ语句实现
# k=0
# for a in range(1,100,2):
#     k+=a
# print (k)
# i=1
# k=0
# while i<100:
#     k+=i
#     i+=2
# print(k)
# 
# i=6
# for x in range (1,i):
#     print('x=',x,'i=',i)
#     i-=1

# 输入一个整数。打印正方形的宽和高，打印相应的正方形
# n=int(input('输入一个整数'))
# i=1
# while i<=n:
#     for a in range(1,(n+1)):
#         print(a,end=' ')
#     i+=1
#     print()

# n=int(input('输入一个整数'))
# i=1
# for b in range(1,(n+1)):
#     for a in range(b,(n+b)):
#         print(a,end=' ')
#     i+=1
#     print()

# for a in range(10):
#     if a%2==1:
#         continue
#     print (a)

# 打印１０以内的偶数，要求试用ｗｈｉｌｅ语句＋ｃｏｎｔｉｎｕｅ语句，采用跳过奇数的方式实现
# i=0
# while i<=10:
#     if i%2==1:
#         i+=1
#         continue
#     print(i)
#     i+=1

# 求１－１００之间所有不能被２．３．５．７中任意一个数整除的数的和（ｃｏｎｔｉｎｕｅ实现）
# i=1
# k=0
# while i<=100:
#     if i%2==0 or i%3==0 or i%5==0 or i%7==0:
#         i+=1
#         continue
#     else:
#         print(i)
#         k+=i
#         i+=1
# print (k)
# l=[]
# while 1:
#     n=int(input("输入正整数"))
#     if n<0:
#         break
#     l+=[n]
# print(l)

# 07练习：
# 　１，输入一个整数，代表树干的高度，打印如下一棵圣诞树
# 输入２
# 　　　×
#  　 ×××
# 　　　×
# 　　　×
# 　２，写一个程序，任意输入一个整数，判断这个数是否是素数
# 　　素数：只能被１和自身整除的正整数。
# 　
# 　３，输入三行文字，将这三行文字保存于一个列表中，并打印出来

# 1
# n=int(input('输入一个整数'))
# a=1
# for k in range(1,n+1):
#     s='*'*(k*2-1)
#     t=s.center((n*2)-1)
#     print(t)
# for k in range(n):
#     t='*'.center((n*2)-1)
#     print(t)

# 2
n=int(input('输入一个大于１的整数'))
if n>1:
    for k in range(2,(n-1)):
        if n%k==0:
            print('这是合数')
            break
    else:
        print('这个数是素数')
else:
    print('输入错误')

# ３，
# a=input('输入第一行文字')
# b=input('输入第二行文字')
# c=input('输入第三行文字')
# print([a,b,c])

