import pymysql
con=pymysql.connect('localhost','root','123456','dict')
cur=con.cursor()
f=open('/home/tarena/lhc/programme/dict/dict.txt')
for x in f:
    word=x.split(' ')[0]
    print(word)
    mean=' '.join(x.split(' ')[1:]).strip()
    print(mean)
    try:
        cur.execute('insert into words (word,mean) values ("%s","%s")'%(word,mean))
        con.commit()
    except Exception:
        continue
cur.close()
con.close()