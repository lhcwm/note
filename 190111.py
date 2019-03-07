# def myfun(a,b,c):
#     print(a,b,c)
# l1=[11,22,33]
# t2=(100,200,300)
# s3={'a':1,'b':2,'c':3,'d':5}
# myfun(100,*(1,2))
# # L=[1,2,True,None,3.14]
# # print(*L, sep='#')

# def myadd(a,b,c=0,d=0):
#     return a+b+c+d
# print(myadd(10,20))
# print(myadd(100,200,300))
# print(myadd(1,2,3,4))

# def mysum(*args):
#     return sum(args)
# print(mysum(1,2,3,4))
# print(mysum(1,3,5,7,9))

# 练习：
# 仿造ＭＡＸ

# def mymax(a,*args):
#     if len(args)==0:
#         z=a[0]
#         for x in a:
#             if x>z:
#                 z=x
#         return z
#     else:
#         for n in args:
#             if a<n:
#                 a=n
#         return a
# print(mymax([6,8,3,5]))
# print(mymax(100,200))
# print(mymax(1,3,5,7,9))

# １，算出１００－９９９以内的水仙花数
# 　　水仙花数是百位的３次方加上十位的３次方加上个位的３次方等于原数的整数
# 　　例如：１５３　＝1**3 +5**3 +3**3
# for n in range(100,999):
#     a=n//100
#     b=n//10%10
#     c=n%10
#     if a**3+b**3+c**3==n:
#         print(n)

# ２，完全数：
# 　　１＋２＋３＝６（６为完全数）
# 　　１，２，３都为６的因数
# 　　完全数是指除自身以外的所有因数之和相加等于自身的数
# 　求４－５个完全数，并打印

# for a in range(2,10000):
#     l=[]
#     for b in range(1,a):
#         if a%b==0:
#             l.append(b)
#     if sum(l)==a:
#         print(a)        

# ３，写一个ｍｙｒａｎｇｅ（）函数，参数可以传１－３个，实际意义同ｒａｎｇｅ函数规则完全相同，
# 此函数返回符合ｒａｎｇｅ（）函数规则的列表

def myrange(star,stop=0,step=1):
    if stop==0 and step==1:
        l=[]
        a=0
        if star>0:
            while a<star:
                l.append(a)
                a+=step
        else:
            while star<stop:
                l.append(star)
                star+=step
    else:
        l=[]
        a=star
        if step>0:
            while a<stop:
                l.append(a)
                a+=step
        else:
            while a>stop:
                l.append(a)
                a+=step
    return l

print(myrange(-10,0))
print(myrange(3,6))
print(myrange(20,10,-2))
