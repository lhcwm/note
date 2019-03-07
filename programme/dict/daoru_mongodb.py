from pymongo import MongoClient
conn=MongoClient('localhost',27017)
db=conn.dict
myset=db.class0
f=open('/home/tarena/lhc/programme/dict/dict.txt')
for x in f:
    word=x.split(' ')[0]
    print(word)
    mean=' '.join(x.split(' ')[1:]).strip()
    print(mean)
    try:
        myset.insert_one({'word':'%s'%word,'mean':'%s'%mean})
    except Exception:
        continue
conn.close()