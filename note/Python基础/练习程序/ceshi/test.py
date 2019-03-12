# n=3
# while n>0:
#     name=input("name")
#     passwd=input("passwd")
#     n=n-1
#     if name=="tarena" and passwd=="123":
#         print("登录成功")
#         break
#     elif n==0:
#         print("你没有机会了")
#     else:
        # print("输入错误，您还有%d次机会" % (n))
# n =input("字符串")
# b =0
# for a in n:
#     if a==" ":
#         b=b+1
# print(b)
# n=int(input("输入数"))
# for a in range (1,n,2):
#     print(a)
# name="关羽"
# gongji=666
# print("%s的攻击值为%d" % (name,gongji))
# age=int(input("年龄"))
# a=365*age//7
# b=365*age%7
# c=("星期日","星期六","星期五","星期四","星期三","星期二","星期一")
# d=0
# if a==0:
#     print("他将过%d个星期日" % (a))
# else: 
#     for k in range(b):
#         d=c[k]
#         print(d)
#     d=a
#     a+=1
#     print("如果是以上日期出生的话，他将过%d个星期日,否则他将过%d个星期日" % (a,d))
# x=1+2+2+2+2*\
# 3*8
# print(x)
# x=int(input('第一个数'))
# y=int(input('第二个数'))
# print('两个数的和为',x+y)
# print('两个数的积为',x*y)
# n=int(input('输入一个数'))
# if n%2==1:
#     print(n,'是奇数')
# else:
#     print(n,'是偶数')
# n=int(input('输入一个数'))
# if n<0:
#     print(n,"小于０")
# else:
#     print(n,"大于０")
# if 50<n<100:
#     print(n,'在５０～１００之间')
# else:
#     print(n,'不在５０～１００之间')
# n=int(input('输入一个数'))
# if n>0:
#     print(n,'是正数')
# elif n==0:
#     print(n,'是０')
# else:
#     print(n,'是负数')
# n=int(input('输入季度'))
# if n==1:
#     print('这个季度有１，２，３月')
# elif n==2:
#     print('这个季度有4，5，6月')
# elif n==3:
#     print('这个季度有7，8，9月')
# elif n==4:
#     print('这个季度有10，11，12月')
# else:
#     print('输入
# n=int(input('输入月份'))
# if 1<=n<=3:
#     print("这个月在第一季度")
# elif 4<=n<=6:
#     print("这个月在第二季度")
# elif 7<=n<=9:
#     print("这个月在第三季度")
# elif 10<=n<=12:
#     print("这个月在第四季度")
# else:
#     print('输入错误')
#商场促销，满１００减２０
# money = int(input('商品金额'))
# pay = money -20 if money>=100 else money
# print('您需要支付',pay,'元')
# n=int(input('输入一个数'))
# a= n if n>=0 else -n
# print('这个数的绝对值是',a)
# n=int(input('输入一个数'))
# if n>=0:
#     print('这个数的绝对值是',n)
# else:
#     print('这个数的绝对值是',-n)


# １，北京出租车计价程序：
# 　　　收费标准：３公里以内收费１３元
# 　　　基本单价：２．３元／公里（超出３公里以外）
# 　　　空驶费：超出１５公里后，每公里加收单价的５０％空驶费（即：１５公里后为３．４５元／公里）
# 　　要求：
# 输入公里数，打印出费用金额（以元为单位，精确到分，分以后四舍五入）
# n=int(input('输入公里数'))
# a=13
# b=2.3
# c=3.45
# if n<=3:
#     print('需要费用：',round(a,2),'元')
# elif 3<n<=15:
#     k1=b*(n-3)+a
#     print('需要费用：',round(k1,2),'元')
# else:
#     k2=c*(n-15)+b*(15-3)+a   
#     print('需要费用：',round(k2,2),'元')

# 写程序，任意给出三个数，打印出三个数中最大的一个数
# a=int(input('第一个数'))
# b=int(input('第二个数'))
# c=int(input('第三个数'))
# if a>b:
#     if a>c:
#         print('最大数为',a)
#     else:
#         print('最大数为',c)
# else:
#     if b>c:
#         print('最大数为',b)
#     else:
#         print('最大数为',c)

# 改进：
m=a
if b>m:
    m=b
if c>m:
    m=c
print('最大值为',c)




# ＢＭＩ指数（ｂｏｄｙ　ｍａｓｓ　ｉｎｄｅｘ）又称身体质量指数
# 　ＢＭＩ计算公式：　ＢＭＩ＝体重（公斤）／身高的平方（米）
# 　如：
# 　　一个６９公斤的人，射高１７３公分
# ＢＭＩ＝６９／１．７３××２　得２３．０５
# 标准表：ＢＭＩ<１８．５　体重过轻
# 　　　　１８．５< bmi <24正常范围
# 　　ＢＭＩ》２４体重过重
# 输入身高体重打印出ＢＭＩ的值，并打印体重状况
# h=float(input('请输入身高（米）：'))
# w=int(input('请输入体重（公斤）：'))
# BMI=w/(h**2)
# if BMI<18.5:
#     print('BMI：',BMI,'体重过轻')
# elif 18.5<=BMI<=24:
#     print('BMI：',BMI,'身体很棒')
# else:
#     print('BMI：',BMI,'有点胖了！')

# 输入三个整数xyz，请把这三个数有小到大输出
# x=int(input('第一个数'))
# y=int(input('第二个数'))
# z=int(input('第三个数'))
# a=x if x<y else y
# a=a if a<z else z
# c=y if y>x else x
# c=c if c>z else z
# for n in (x,y,z):
#     if n!=a and n!=c:
#         b=n
# print(a,b,c)

# 输入某年某月某日，判断这一天是这一年的第几天
# y=int(input("哪年"))
# m=int(input('哪月'))
# d=int(input('哪日'))
# m1=m-1

