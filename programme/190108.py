# for i in [1,2]:
#     for j in [1,2,3]:
#         print(i,j)
#         break
#     else:
#         print('for-j')
# else:
#     print('for-i')

# s='python2best'
# s1=[3,5,4,2]
# s2=list(s)
# print (s2)
# k=''
# for a in s2:
#     if a=="2":
#         k+="3"
#         break
#     k+=a
# s2=list(k)
# print(s2)
# s2+='!'
# print(s2)
# print(len(s2))

# l=[3,5]
# l[1:1]=[4]
# l[:0]=1,2
# l[6:]=[6]
# print(l)
# l=l[:-6:-1]
# print(l)

# 循环输入一些正整数，输入负数结束
# 　１，打印一共输入几个有效数（不算负数）
# 　２，打印输入的最大数
# 　３，打印输入的最小数
# 　４，打印输入的这些数的平均数
# k=[]
# while 1:
#     a=int(input('输入正整数'))
#     if a<0:
#         break
#     k+=[a]
# print('有效数字共%d个'% len(k))
# print('最大值为：%d'% max(k))
# print('最小值为：%d'% min(k))
# print('平均值为：%d'% (sum(k)/len(k)))

# 让用户输入两个或以上的正整数，当输入小于０时，结束输入（不允许输入重复的数）
# １，打印这些数的和
# 　２，打印最大数
# 　３，打印第二大的数
# 　４，删除最小的数

# l=[]
# while 1:
#     a=int(inout('输入正整数'))
#     if a<0:
#         if len(a)<2:
#             print('输入次数少，请继续输入')
#             continue
#         break
#     elif a in l:
#         print('不允许输入重复的数')
#         continue
#     l+=a

# l=[]
# while 1:
#     a=int(input('输入正整数'))
#     if a<0:
#         if len(l)<2:
#             print('输入次数太少，请继续输入')
#             continue
#         break
#     elif a in l:
#         print('不能输入重复的数')
#         continue
#     l+=[a]
# l1=sorted(l)
# print("和为",sum(l))
# print('最大数为',l1[-1])
# print('第二大的数为',l1[-2])
# for c in range(len(l)):
#     if l[c]==min(l):
#         del l[c]
#         break
# print(l)
# k=0
# l=[]
# while 1:
#     a=input('输入一段文字')
#     if not a:
#         break
#     l+=[a]
# for b in l:
#     print(b)
#     k+=len(b)
# print('输入了%d行'% len(l))
# print('输入了%d个字符'% k)
# l1=[1,2,[3,4]]
# l2=l1.copy()
# l2[2][0]=5
# print(l1)  #[1,2,[5,4]]
# print(l2)  #[1,2,[5,4]]

# import copy    #导入拷贝模块
# l1=[1,2,[3,4]]
# l2=copy.deepcopy(l1)
# l2[2][0]=5
# print(l1)  #[1,2,[5,4]]
# print(l2)  #[1,2,[5,4]]

# a='hello'
# c=' '.join(a)
# print(c)

# 生成１－１００内所有奇数组成的列表
# a=[2*k-1 for k in range(1,51)]
# print(a)

# １，用字符串‘ＡＢＣ’和‘１，２，３’，生成如下列表
# 　['A1','A2','A3'....'C3']
# a=[x*y for x in 'ABC' for y in [1,2,3]]
# print(a)

# ２，生成一个列表，此列表为ｘ的平方加１不能被５整除的数的列表，
# ｘ取值范围0<=x<100

# b=[x for x in range(100) if (x**2+1)%5!=0]
# print(b)

# １，　已知有一个字符串：
# 　　　s=‘100,200,300,500,800’
# 将其转化为列表，列表内都为整数
# s='100,200,300,500,800'
# l=s.split(',')
# l1=[int(x) for x in l]
# print(l1)

# ２，有一些数存在于列表中
# 　Ｌ＝[1,3,2,1,6,4,2,...98,82]
#  １．将列表中出现数字存入到另一个列表l2中
#  要求：
# 　　重复出现的数只在列表中保留一份。
# 　２，将列表中出现两次的数存在于l3列表中，l3中只保留一份。
# l=[1,1,2,3,3,4,4,4,5,5,5,6,6,7,7,7,7,8,8,8,8,8,9,9,9,9,9,9,9]
# l2=[]
# l3=[]
# l4=[]
# for x in l:
#     if x not in l2:
#         l2.append(x)
#     else:
#         if x in l3:
#             l3.remove(x)
#             l4.append(x)
#             continue
#         elif x in l4:
#             continue
#         l3.append(x)
# l1=[x for x in l if l.count(x)==2]
# for x in l1:
#     if x in l3:
#         continue
#     l3.append(x)
# print('去重后的序列为',l2)
# print('出现两次数的序列为',l3)

# ３，生成前４０个斐波那契数
# 　１　１　２　３　５　８
# 　　要求：
# 　　将这些数保存在列表中，并打印出来
# 　　注：前两个数为１和１，从第三个数起为前两个数相加之和

# l=[1,1]
# for n in range(2,40):
#     k=l[n-2]+l[n-1]
#     l.append(k)
# print(l)


