# t=()
# for a in range(1,10):
#     t+=(a**2,)
# print(t)

# d={
# 1:'春季有１，２，３月',
# 2:'夏季有４，５，６月',
# 3:'秋季有７，８，９月',
# 4:'冬季有１０，１１，１２月'}
# n=int(input('输入季度'))
# if n not in d:
#     print('信息不存在')
# else:
#     print(d[n])

# d={
# 1:'一等奖',
# 'k2':'二等奖',
# 113:'三等奖',
# 'jj':'四等奖',
# 2:'二等奖',
# 3:'三等奖',
# 4:'三等奖',
# 5:'三等奖',
# 6:'三等奖'}
# for a in d:
#     k=input('抽奖')
#     print(d[a])

# n=input('请输入：')
# d={}
# for a in n:
#     if a in d:
#         d[a]+=1
#         continue
#     d[a]=1
# for b in d.keys():
#     print('字符',b,'出现',d[b],'次')

# l=['tarena','xiaozhang','hello']
# d={x:len(x) for x in l}
# print(d)

# Nos=[1001,1002,1005,1008]
# names=['Tom','Jerry','Spike','Tyke']
# d={}
# d={Nos[x]:names[x] for x in range(len(Nos))}
# d={x:names[Nos.index(x)] for x in Nos}

# １．思考下面的程序执行结果是什么，为什么？
# l=list(range(10))
# for x in l:
#     l.remove(x)
# print('l=',l)  #请问是空列表吗？
# ２，输入一些单词和解释，将单词作为键，解释为值，存入字典中
# 　单输入单词或解释为空时停止输入，并打印字典。
# 　　然后，输入查询的单词，给出单词的内容，如果单词不存在则提示：查无此词
# d={}
# while 1:
#     a=input('输入单词')
#     if a=='':
#         break
#     b=input('输入解释')
#     if b=='':
#         break
#     d[a]=b
# print(d)
# while 1:
#     c=input('输入查询的单词')
#     if c=='':
#         print('查无此词')
#         break
#     else:
#         print('此词解释为',d[c])

