# import pymysql

# con=pymysql.connect('localhost','root','123456','jason')
# cur=con.cursor()
# cur.execute('select * from acct')
# re=cur.fetchall()
# for x in re:
#     print(x[0],x[1],x[6])

# cur.close()
# con.close()




import pymysql
con=connect(host,port,user,passwd,库名称)
cur=con.cursor()
cur.execute('select * from acct')
result=cur.fetchall()
for i in result:
    print(i[0],i[1],i[6])
con.commit()
cur.close()
con.close()