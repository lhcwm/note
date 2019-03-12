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

def mymax(a,*args):
    if len(args)==0:
        z=a[0]
        for x in a:
            if x>z:
                z=x
        return z
    else:
        for n in args:
            if a<n:
                a=n
        return a
print(mymax([6,8,3,5]))
print(mymax(100,200))
print(mymax(1,3,5,7,9))