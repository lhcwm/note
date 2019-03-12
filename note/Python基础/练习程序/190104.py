# a=input('输入第一行文字')
# b=input('输入第二行文字')
# c=input('输入第三行文字')
# x=len(a)
# y=len(a)
# z=len(a)
# x=x if x>y else y
# x=x if x>z else z
# k='%'+str(x)+'s'
# print('第一行：',k%a,'\n'
# '第二行：',k%b,'\n'
# '第三行：',k%c)


# n=int(input('输入整数'))
# i=1
# while i<=n:
#     print(i)
#     i+=1

# １，打印１－２０的整数
# ２，打印１－２０的整数，打印在一行内
# ３，打印１－２０的整数，每行５个，打印４行

# 1,
# i=1
# while i<=20:
#     print(i)
#     i+=1

# 2,
# i=1
# while i<=20:
#     print(i,end='')
#     i+=1
# print()
#3
# i=1
# while i<=20:
#     if i%5==0:
#         print(i)
#         i+=1
#     else:
#         print(i,end='')
#         i+=1


# 写一个程序，输入一个开始的整数存在于ｂｅｇｉｎ变量中，
# 　　输入一个结束的整数，存在于ｅｎｄ变量中。
# 打印从ｂｅｇｉｎ到ｅｎｄ的每个整数，打印在一行中

# 思考：如何实现每五个打印在一行，打印多行

# b=int(input('开始数'))
# e=int(input('结束数'))
# i=b
# k=0
# while i<=e:
#     k+=1
#     if k%5==0: 
#         print(i)
#     else:
#         print(i,end=' ')
#     i+=1
#print()
    
# 计算：
# 　１＋２＋３.....+100的和，并打印这个和是多少
# i=1
# k=0
# while i<=40000000:
#     k+=i
#     i+=1
# print('和为',k)

# 练习：
# 　输入一个整数ｎ，打印一个宽度和高度都为ｎ个字符的长方形

# n=int(input('输入一个整数'))
# i=1
# k='5'
# l=' '
# print(k*n)
# while i<=(n-2):    
#     print(k+l*(n-2)+k)
#     i+=1
# if n>=2:
#     print(k*n)

# 输入一个数，打印制定宽度的正方形
# n=int(input('宽度为'))
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         print(j,end=' ')
#         j+=1
#     print()
#     i+=1
 
# 用ｗｈｉｌｅ语句实现打印三角形，输入一个数，代表三角形的宽度和高度，打印出相应的三角形
# １，
# 0
# 00
# 000
# 0000

# n=int(input('输入一个数'))
# k='#'
# i=1
# while i<=n:
#     print(k*i)
#     i+=1

# print('--------------------------')
# k='#'
# i=1
# while i<=n:
#     print(' '*(n-i)+k*i)
#     i+=1
# print('--------------------------')

# k='#'
# i=n
# while i>0:
#     print(' '*(n-i)+k*i)
#     i-=1
# print('--------------------------')
# k='#'
# i=n
# while i>0:
#     print(k*i)
#     i-=1
# s=0
# while 1:
#     x=int(input('请输入一个数'))
#     if x<0:
#         break
#     s+=x
# print('您刚才输入的数的总和为：',s)

# 打印０－３０范围内的所有偶数
# i=1
# while i<=30:
#     if i%2==0:
#         print(i)
#     i+=1

# 写程序用ｗｈｉｌｅ语句生成如下的字符串，并打印：
# 　　１．'ABC...XYZ'
# 　　２，'AaBb.....YyZz'

# i='A'
# while i<='Z':
#     print(i,end=' ')
#     i=chr(ord(i)+1)
# print()

# j='a'
# i='A'
# while i<='Z':
#     print(i+j,end=' ')
#     i=chr(ord(i)+1)
#     j=chr(ord(j)+1)
# print()

# 写程序求：
# 　　１／１　＋１／３　＋１／５　.....＋１／９９的和
# n=1
# s=0
# while n<=99:
#     k=1/n
#     n+=2
#     s+=k
# print('和为：',s)

# 写程序求：
# 　　１／１－１／３＋１／５－１／７＋....＋（＋－）１/(2*n-1)的和
# 　　　１，求当ｎ取１００００００这个算式的和
# 　　　２，求１的和乘以４是多少

# n=1
# s=0
# m=1
# while n<=1000000:
#     k=m*1/(2*n-1)
#     n+=1
#     m*=-1
#     s+=k
# print('和为：',s,'和乘以４后值为：',4*s)

# 九九乘法表
# i=1
# while i<=9:
#     n=1
#     while n<=i:
#         k=i*n
#         print('%dx%d=%-2d' % (n,i,k),end=' ')
#         n+=1
#     i+=1
#     print()    
# for a in range(1,10):
#     for b in range(1,a+1):
#         print('%dx%d=%d'%(b,a,a*b),end=' ')
#     print()    
