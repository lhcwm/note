from socket import *
import pymysql
import os,sys
import time 
import signal

# 定义全局变量
if len (sys.argv)<3:
    print('start as:python3 dict_server.py 0.0.0.0 6789')
    sys.exit()
HOST=sys.argv[1]
PORT=int(sys.argv[2])
ADDR=(HOST,PORT)
DICT='./dict.txt'
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
# 搭建网络连接
def main():
    # 连接数据库
    db=pymysql.connect('localhost','root','123456','dict',charset='utf8')
    # 创建套接字
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)


    while True:
        try:
            c,addr=s.accept()
            print('connect from',addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit('服务器退出')
        except Exception as e:
            print(e)
            continue
        # 创建子进程
        pid=os.fork()
        if pid==0:
            s.close()
            do_child(c,db)
            sys.exit()

        else:
            c.close()
# 处理客户端请求
def do_child(c,db):
    while True:
        data=c.recv(1024).decode()
        print(c.getpeername(),':',data)
        if not data:
            c.close()
            sys.exit()
        elif data[0]=='I':
            do_login(c,db,data)
        elif data[0]=='R':
            do_register(c,db,data)
        elif data[0]=='E':
            c.close()
            sys.exit()
        elif data[0]=='Q':
            do_query(c,db,data)
        elif data[0]=='H':
            do_hist(c,db,data)

def do_hist(c,db,data):
    name=data.split(' ')[1]
    cur=db.cursor()
    sql='select * from history where name="%s" order by time desc limit 10'%name
    cur.execute(sql)
    r=cur.fetchall()
    if not r:
        c.send(b'fail')
    else:
        c.send(b'ok')
        time.sleep(0.1)
    for i in r:
        msg='%s %s %s'%(i[0],i[1],i[2])
        c.send(msg.encode())
        time.sleep(0.1)
    c.send(b'##')
    cur.close()


def do_query(c,db,data):
    l=data.split(' ')
    name=l[1]
    word=l[2]
    cur=db.cursor()
    sql='insert into history (name,word) values ("%s","%s")'%(name,word)
    try:
        cur.execute(sql)
        db.commit()
        cur.close()
    except Exception as e:
        print(e)
        db.rollback()
    # 单词本查找
    f=open(DICT)
    for x in f:
        tmp=x.split(' ')[0]
        if tmp>word:
            break
        elif tmp==word:
            c.send(x.encode())
            f.close()
            return
    c.send('没有此单词'.encode())
    f.close()

def do_login(c,db,data):
    l=data.split(' ')
    name=l[1]
    passwd=l[2]
    cur=db.cursor()
    sql='select * from users where name="%s" and passwd="%s"'%(name,passwd)
    cur.execute(sql) 
    r=cur.fetchone()
    if r ==None:
        c.send(b'fail')
    else:
        c.send(b'ok')
    cur.close()

def do_register(c,db,data):
    l=data.split(' ')
    name=l[1]
    passwd=l[2]
    cur=db.cursor()
    sql='insert into users values ("%s","%s")'%(name,passwd)
    try:
        cur.execute(sql)
    except Exception:
        c.send('用户已存在'.encode())
        db.rollback()
        cur.close()
        return
    c.send(b'ok')
    db.commit()
    cur.close()

if __name__=='__main__':
    main()