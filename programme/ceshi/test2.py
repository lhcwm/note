# n=int(input("输入宽度"))
# x='※'
# y='*'
# a=x*(n-2)
# b=y*(n-2)
# print(x+a+x)
# print(x+b+x)
# print(x+b+x)
# print(x+a+x)


# 写程序，输入一个长字符串，判断你的姓名是否存在于输入的字符串中，如果存在则打印“你的名字出现了”，否则不予理睬
# n=input('输入字符串')
# name="张三丰"
# if name in n:
#     print('你的名字出现了')


# 输入一个字符串，打印如下内荣：
# 　１，打印这个字符串的第一个字符
# 　２，打印最后一个
# 　３，如果长度是奇数，打印中间这个字符
# 　　　注：求字符串长度的函数len(x)
# n=input('输入字符串')
# a=len(n)
# print('第一个字符：',n[0])
# print('最后一个字符：',n[a-1])
# if a%2==1:
#     print('中间字符：',n[a//2])

# 写一个程序，输入一个字符串，把字符串的第一个字符和最后一个字符去掉后，打印出处理后的字符串
# 　输入任意一个字符，判断判断这个字符串是否是回文
# 　　回文示例：
# 　　　上海自来水来自海上
# 　　　　１２３２１
# 　　回文是指中心对称的文字
# n=input('输入字符串')
# a=len(n)
# print(n[1:(a-1)])
# 
# b =n[::-1]
# if n==b:
#     print('这是回文')

# 输入一段字符，如果字符串不为空，则把字符串的第一个字符的编码值打印出来

# n=input('字符串')
# if n!="":
#     print('第一个字符的编码值：',ord(n[0]))

# 练习：
# 　　１，给出一个年份，判断是否为闰年
# 　　　规则：
# 　　　四年一润，百年不润，四百年再润
# 　　
# 　２，输入一个字符串，把输入的字符串中的空格全部去掉，打印出处理后的字符串的长度和字符串内容
# 　　３，输入三行文字，让这三行文字在一个方框居中显示
# 　　　　　（注：不要输中文）
# １１１１１
# １　a　  １
# １１１１１

# １，
# y=int(input('输入年份'))
# if y%4==0 and y%100!=0 or y%400==0:
#     print('%s年是闰年' % (y))
# else:
#     print('%s年不是闰年' % (y))

# ２，
# n=input('输入字符串')
# a=n.replace(' ','')
# b=len(a)
# print('去掉空格后的字符串长度为%d，字符串内容为%s' % (b,a))

# 3,
# a=input('输入第１条字符串')
# b=input('输入第２条字符串')
# c=input('输入第３条字符串')
# x=len(a)
# y=len(b)
# z=len(c) 
# x=x if x>y else y
# x=x if x>z else z
# x+=2
# k='※'
# l=' '
# a=a.center(x)
# b=b.center(x)
# c=c.center(x)
# print(k+k*x+k)
# print(k+l*x+k)
# print(k+a+k)
# print(k+b+k)
# print(k+c+k)
# print(k+l*x+k)
# print(k+k*x+k) 

# 练习
# 输入某年某月某日，判断这一天是这一年的第几天

# a=int(input('哪年'))
# b=int(input('哪月'))
# c=int(input('哪日'))
# x=[31,59,90,120,151,181,212,243,273,304,334]
# if 0<=b<=12 and 0<=c<=31:  
#     s=(x[b-2]+c) if b>=0 else c  
#     if (a%4==0 and a%100!=0 or a%400==0):
#         if b>2:
#             s+=1
#             print('这天是这一年的第%d天' % (s))      
#         elif b==2 and c>29:
#             print('输入错误') 
#         else:
#             print('这天是这一年的第%d天' % (s))
#     else:
#         if b==2 and c>28:
#             print('输入错误') 
#         else:
#             print('这天是这一年的第%d天' % (s))
# else:
#     print('输入错误')

# 奖金问题
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


