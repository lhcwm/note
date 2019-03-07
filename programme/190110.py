# s1={'刘备','曹操','孙权'}　#经理
# s2={'曹操','孙权','张飞','关羽'}　#技术员
# s3=s1 &s2
# s4=s1 - s2
# s5=s2-s1
# '张飞'　in s1:
# s6=s1^s2
# len(s1|s2)




# def.py
# 带有参数的函数
# def mymax(a,b):　　#a,b形参
#     print('a=',a)
#     print('b=',b)
#     if a>b:
#         print(a,'大于',b)
#     else:
#         print(a,'小于等于',b)
# mymax(100,200)　#100,200实参

# def myadd(x,y):
#     print('x=',x)
#     print('y=',y)
#     z=x+y
#     print('x+y=',z)
# myadd(100,200)
# myadd('ABC','123')

# def print_event(n):
#     print('这之前的偶数有')
#     for a in range(0,n,2):
#         print(a,end=' ')
#     print()
# n=int(input('输入一个整数'))
# print_event(n)

# def say_hello():
#     print('hello aaa')
#     print('hello bbb')
#     return
#     print('hello ccc')
# v=say_hello()
# print('v=',v)

# v2=say_hello()
# print('v2=',v2)

# def myamx(a,b):
#     if a>=b:
#         return a
#     return b
# print(myamx(10,200))
# print(myamx('ABCa','ABCD'))

# def myadd(x,y):
#     return (x+y)
# a=int(input('输入第一个数：'))
# b=int(input('输入第二个数：'))
# print('您输入的两个数的和为：',myadd(a,b))

# def input_number():
#     l=[]
#     while 1:
#         a=int(input('请输入一个正整数'))
#         if a <0:
#             break
#         l+=[a]
#     return l
# L=input_number()
# print('用户输入的最大值：',max(L))
# print('用户输入的最小值：',min(L))
# print('用户输入数的和为：',sum(L))

# １，定义两个函数：
# 　　ｓｕｍ３（a,b,c）用于返回三个函数的和
# 　　ｐｏｗ３（ｘ）用于返回ｘ的三次方
# 　　用以上函数计算：
# 　　　１，计算１的立方＋２的立方＋３的立方
# 　　　２，计算１＋２＋３的和的立方

def sum3(a,b,c):
    return a+b+c
def pow3(x):
    return x**3
# l=[]
# for n in range(1,4):
#     d=int(input('输入第%d个数'%n))
#     l+=[d]
# d1=int(input('输入第一个数'))
# d2=int(input('输入第二个数'))
# d3=int(input('输入第三个数'))
# s=sum3(d1,d2,d3)
# z1=sum3(pow3(d1),pow3(d2),pow3(d3))
# print('三个数的立方和：',z1)
# print('三个数和的立方：',pow3(s))

# ２，写一个函数　get_chinese_char_count(s)，此函数功能是给定一个字符串ｓ，返回这个字符串中中文字符的个数
# 　　ｄｅｆ　get....:
#    ...
#   s=input('请输入中英文混合字符串')
# 　　ｐｒｉｎｔ（中文字符的个数）
# 注：中文的编码范围是：0x4E00-0x9FA5
def get_chinese_char_count(s):
    k=0
    for n in s:
        if 0x4E00<=ord(n)<=0x9FA5:
            k+=1
    return k
s=input('请输入中英文混合字符串')
print('中文字符的个数为：',get_chinese_char_count(s))