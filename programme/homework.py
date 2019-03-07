from pymongo import MongoClient
from random import randint
conn=MongoClient('localhost',27017)
db=conn.grade
myset=db.class0
al=myset.find({})
for x in al:
    myset.update_one({'name':x['name']},{'$set':{'score':
    {'Chinese':'%d'%randint(50,100),'match':'%d'%randint(50,100),
    'english':'%d'%randint(50,100)}}})
