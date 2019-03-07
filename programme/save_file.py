from pymongo import MongoClient
import bson.binary

conn=MongoClient('localhost',27017)
db=conn.image
myset=db.mm

# 存储

# with open('达内.jpg','rb') as f:
#     data =f.read()
# #做格式转换 
# conntent=bson.binary.Binary(data)
# # 插入数据库
# myset.insert_one({'filename':'mm.jpg','data':conntent})

# 提取
img=myset.find_one({'filename':'mm.jpg'})
with open('tt.jpg','wb') as f:
    f.write(img['data'])
conn.close()
