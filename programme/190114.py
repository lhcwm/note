# def f1():
#     print('f1被调用')

# def f2 ():
#     print('f2被调用'

# def goodbye(L):
#     for x in L:
#         print('再见',x)

# def op(fn,L):
#     fn(L)

# op(goodbye,['tom','jerry','spike'])

# def myinput(fn):
#     L=[1,3,5,7,9]
#     return fn(L)
# print(myinput(max))
# print(myinput(min))
# print(myinput(sum))

# def get():
#     s=input('请输入你要做的操作')
#     if s =='求最大':
#         return max
#     elif s == '求最小':
#         return min
#     elif s=='求和':
#         return sum

# L=[2,4,6,8,10]
# f=get()
# print(f)
# print(f(L))

# 写一个计算公式的解释器
# 已知有如下函数：
# 定一个带有一个参数的函数　get(s)
# def get(s):
#     def myadd(x,y):
#         return x+y
#     def mysum(x,y):
#         return x-y
#     def mymul(x,y):
#         return x*y
#     if s == '加' or s=='+':
#         return myadd
#     elif s=='乘' or s=='*':
#         return mymul
#     elif s=='减' or s=='-':
#         return mysum

# # 此函数的在传入字符串‘加’或‘＋’返回myadd函数；
# # 乘或*，返回mymul
# # 在主函数中程序如下：
# def main():
#     while True:
#         s=input('请输入计算公式：')
#         L=s.split()
#         a=int(L[0])
#         b=int(L[2])
#         fn=get(L[1])
#         print('结果是：',fn(a,b))
# main()

# def fn_out():
#     print('fn_out被调用')
#     def fn_in():
#         print('fn_in被调用')
#     fn_in()
#     fn_in()
#     print('fn_out调用结束')
# fn_out()
# v=100
# def fun1():
#     # v=200
#     print('fun1.v=',v)
#     def fun2():
#         # v=300
#         print('fun2.v=',v)
#     fun2()
# fun1()
# print('全局的v=',v)

# 执行以下程序
# L=[1,2,3]
# v=100
# def f1():
#     L.append(4)
#     v=200
# f1()
# print(L)
# print(v)

# def f2():
#     L+=[5]
#     v+=1
# f2()
# print(L)
# print(v)

# count=0
# def fx(name):
#     print('您好',name)
#     global count
#     count+=1

# fx('小张')
# fx('小李')
# print('FX函数被调用',count,'次')


# fx=lambda n:(True if (n**2+1)%5==0 else False)
# print(fx(3))
# print(fx(4))
# def mymax(x,y):
    # return max(x,y)
# mymax=lambda x,y:max(x,y)
# print(mymax(100,200))
# print(mymax('100','20'))

# 练习：
# １，写一个函数mysum(n),此函数用来计算，同ｓｕｍ完全相同

# def mysum(n):
#     k=0
#     for a in range(n+1):
#         k+=a
#     return k
# print(mysum(3))

# ２，写一个函数myfac(n)，来计算ｎ！（ｎ的阶乘）
# 　n!=1*2*3...*n
# ｐｒｉｎｔ（myfac(5)）

# def myfac(n):
#     k=1
#     for a in range(1,n+1):
#         k*=a
#     return k
# print(myfac(5))

# 3,写一个函数，计算
# 　１＋２**2+3**3+....n**n的和
# def ms(n):
#     l=[]
#     for a in range(1,n+1):
#         l.append(a**a)
#     return sum(l)
# print(ms(3))

def myfac(n):
    if n==0:
        return 1
    else:
        return n*myfac(n-1)
print(myfac(5))

def myfac(n):
    if n==0:
        return 0
    else:
        return n+myfac(n-1)
print(myfac(5))