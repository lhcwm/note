# from pymongo import MongoClient
# conn=MongoClient('lockhost',27017)
# db=conn.stu
# myset=db.class0
from pymongo import MongoClient
# 创建数据库连接
conn=MongoClient('localhost',27017)
# 创建数据库对象
db=conn.stu
# db=conn['stu']

# 创建集合对象
myset=db.class1
# index_age=myset.create_index('age',name='Age',sparse=True)
# 索引聚合
# for i in myset.list_indexes():
#     print(i)
l=[{'$group':{'_id':'$age','num':{'$sum':1}}}]
cursor=myset.aggregate(l)
for i in cursor:
    print(1)
conn.close()