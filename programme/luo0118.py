# def div(n):
#     print(n,'个苹果你想分几个人?')
#     s=input('输入人数:')
#     cnt = int(s)
#     result=n/cnt
#     print('每个人分了',result,'个苹果')
# try:
#     div(10)
#     print('分苹果成功')
# except ValueError as err:
#     print('分苹果失败,你输入的不是数字吧')
#     print('err=',err)
# except ZeroDivisionError:
#     print('分苹果失败,没人咋分啊')
# print('程序正常退出')

# def score():
#     a=int(input('输入成绩'))
#     assert 0<=a<=100,'成绩超出范围'
#     return a

# # try:
# sc=score()
# # except ValueError:
# #     sc=0
# print('成绩为:',sc)

# def make():
#     print('函数开始')
#     print('函数结束')

# make()
# print('make调用完毕')

# print('程序正常退出')

# def get():
#     sc=int(input('输入成绩'))
#     if sc<0:
#         raise ValueError
#     if sc>100:
#         raise ValueError('超出最大值')
#     return sc

# try:
#     s=0
#     s=get()
# except ValueError as er:
#     print('输入错误:err=',s)
# print(s)

# def age():
#     a=int(input('输入年龄'))
#     if a<1 or a>140:
#         raise ValueError
#     return a

# try:
#     ag=age()
#     print('年龄是:',ag)
# except ValueError:
#     print('输入年龄错误')

s={'唐僧','悟空','八戒','沙僧'}
# for x in s:
#     print(x)
# else:
#     print('遍历结束')
x=iter(s)
while 1:
    try:
        print(next(x))
    except StopAsyncIteration:
        break