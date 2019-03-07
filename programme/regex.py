import re

f=open('第一次月考.txt','r')
# x=f.readline()
for x in f:
    a=re.findall(r'[A-Z][a-zA-Z]*',x)
    if a==[]:
        continue
    print(a)

# for x in f:
#     a=re.findall(r'-?\+?[0-9]+\.?/?[0-9]*%?',x)
#     if a==[]:
#         continue
#     print(a)

for x in f:
    a=re.findall(r'[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}',x)
    for i in a:
        b=re.subn(r'-','.',i)
        print(b)
f.close()

# pattern = r'(\w+):(\d+)'
# s='zhang:1994 li:1993'

# l=re.findall(pattern,s)
# print(l)

# # 切割字符串
# l=re.split(r'\s+','hello world nihao   china')
# print(l)

# # 替换字符串
# s=re.sub(r'垃圾','**','张三垃圾垃圾垃圾',2)
# print(s)

# pattern=r'\d+'
# s='2018年4月28日'
# it=re.finditer(pattern,s)
# for x in it:
#     print(x.group())  #取出match对象匹配内容
# # print(dir(next(it)))

# #完全匹配
# # obj=re.fullmatch(r'\w+','hello#1973')
# # print(obj.group())

# # 匹配开始位置
# obj=re.match(r'[A-Z]\w+','Hello World')
# print(obj.group())

# # 匹配第一个
# obj=re.search(r'\d+','1231nian231')
# print(obj.group())
