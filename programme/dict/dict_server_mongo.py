from socket import *
from pymongo import MongoClient
import os,sys
import time 
import signal

# 定义全局变量

HOST='0.0.0.0'
PORT=6789
ADDR=(HOST,PORT)
DICT='./dict.txt'
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
# 搭建网络连接
def main():
    # 连接数据库
    conn=MongoClient('localhost',27017)
    db=conn.dict
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
    myset=db.history
    r=myset.find({'name':'%s'%name})
    if not r:
        c.send(b'fail')
    else:
        c.send(b'ok')
        time.sleep(0.1)
    for i in r:
        msg='%s %s %s'%(i['name'],i['word'],i['time'])
        c.send(msg.encode())
        time.sleep(0.1)
    c.send(b'##')
    cur.close()


def do_query(c,db,data):
    l=data.split(' ')
    name=l[1]
    word=l[2]
    myset=db.history
    try:
        myset.insert_one({'name':'%s'%name,'word':'%s'%word,'time':time.ctime()})
    except Exception as e:
        print(e)
    # 单词本查找
    myset=db.class0
    tmp=myset.find_one({'word':'%s'%word})
    if tmp==None:
        c.send('没有此单词'.encode())
        return
    elif tmp['word']==word:
        tmp=tmp['word']+' '+tmp['mean']
        c.send(tmp.encode())
        return
    

def do_login(c,db,data):
    l=data.split(' ')
    name=l[1]
    passwd=l[2]
    myset=db.users
    r=myset.find_one({'name':'%s'%name,'passwd':'%s'%passwd})
    if r ==None:
        c.send(b'fail')
    else:
        c.send(b'ok')

def do_register(c,db,data):
    l=data.split(' ')
    name=l[1]
    passwd=l[2]
    myset=db.users
    r=myset.find_one({'name':'%s'%name})
    if r==None:
        myset.insert_one({'name':'%s'%name,'passwd':'%s'%passwd})
    else:
        c.send('用户已存在'.encode())
        return
    c.send(b'ok')

if __name__=='__main__':
    main()