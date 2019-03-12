import re

# 只匹配ascii字符
# regx=re.compile(r'\w+',flags=re.A)
# 忽略字母大小写
# regx=re.compile(r'[a-z]+',flags=re.I)
# 使 . 可以匹配换行
# regx=re.compile(r'.+',flags=re.S)
# 使 ^ $ 可以匹配每一行的开头结尾位置
# regx=re.compile(r'^北京',flags=re.M)
# l=regx.findall('Welcome to \n北京')

# 为正则添加注释
pattern=r'''[A-Z][a-z]*  #匹配第一个单词
\s+\w+  #匹配空行和第二个单词
\s+\w+'''
regx=re.compile(pattern,flags=re.X)
l=regx.findall('Welcome to \n北京')
print(l)



# pattern=r'(?P<pig>ab)cd(ef)'
# regx=re.compile(pattern)
# # 获取match对象
# obj=regx.search('abcdefgh')
# print(obj.group('pig'))
# # match属性变量
# print(obj.pos)
# print(obj.endpos)
# print(obj.re)
# print(obj.string)
# print(obj.lastgroup)
# print(obj.lastindex)

# # match属性方法
# print(obj.span())
# print(obj.start())
# print(obj.end())
# print(obj.groupdict())
# print(obj.groups())
