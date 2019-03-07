# import random as R
# l=list(range(1,14))
# R.shuffle(l)

# k=1
# for x in l:
#     if x==8:
#         print('查找成功,第%d张'%k)
#     k+=1
# def dg(n,left,right):
#     a=(left+right)//2
#     if left>right:
#         return
#     if l[a]==n:
#         print('OK',a)
#         return
#     elif l[a]>n:
#         dg(n,left,a-1)
#     elif l[a]<n:
#         dg(n,a+1,right)
# dg(6,0,len(l)-1)

# def dg(n,left,right):
#     while True:
#         a=(left+right)//2
#         if left>right:
#             return
#         if l[a]==n:
#             print('OK',a)
#             return
#         elif l[a]>n:
#             right=a-1
#             continue
#         elif l[a]<n:
#             left=a+1
#             continue
# dg(6,0,len(l)-1)

# def dg(n):
#     left=0
#     right=len(l)-1
#     while left<=right:
#         middle=(left+right)//2
#         if l[middle]==n:
#             print('ok',middle)
#             return
#         elif l[middle]>n:
#             right=middle-1
#         elif l[middle]<n:
#             left=middle+1
#     print('未找到')
#     return

# dg(6)
import random as R
l=list(range(150,170,2))
R.shuffle(l)
print(l)
# 外层循环
for x in range(len(l)-1):
    #设置数据交换的标识
    flag=False
    # 内层循环
    for y in range(len(l)-x-1):
        # 如果次序有误,进行交换
        if l[y]>l[y+1]:
            l[y],l[y+1]=l[y+1],l[y]
            flag=True
    # 如果未发生数据交换,则说明后续数据均有序,跳出循环
    if flag==False:
        break
    #走访数据次数
print('走访次数',x+1)
print(l)