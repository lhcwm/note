from pymongo import MongoClient
# 创建数据库连接
conn=MongoClient('localhost',27017)
# 创建数据库对象
db=conn.stu
# db=conn['stu']

# 创建集合对象
myset=db.class0

# 数据操作
# myset.insert_one({'name':'小小','kk':'宵小'})
# myset.insert_many([{'name':'张国立','king':'康熙'},{'name':'陈道明','king':'康熙'}])
# myset.insert([{'name':'唐国强','king':'雍正'},{'name':'程建斌','king':'雍正'},{'_id':1,'name':'吴奇隆','king':'四爷'}])
# myset.save({'_id':'ObjectId("5c7cc7d169d72e0ba4742e3e")','name':'郑少秋','king':'乾隆'})
# cursor=myset.find({'name':{'$exists':True}},{'_id':0})
# for i in cursor.limit(3).sort([('name',1)]):
#     print(i)

# dic={'$or':[{'king':'乾隆'},{'name':'陈道明'}]}
# d=myset.find_one(dic)
# print(d)

# myset.update_many({'king':'康熙'},{'$set':{'king_name':'玄烨'}})
# myset.update_one({'king':'雍正'},{'$set':{'king_name':'胤禛'}})
# myset.update_one({'name':'郑少秋'},{'$set':{'king':'乾隆'}},upsert=True)
# myset.update({'name':'乾隆'},{'$set':{'king_name':'弘历'}})

# myset.delete_many({'name':'小小'})
myset.remove({'king_name':None},multi=True)
# 关闭连接
conn.close()