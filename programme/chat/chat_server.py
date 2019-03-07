#coding=utf-8
'''
Chatroom
env:python3.5
exc:socket and fork
'''
from socket import *
import os,sys

# 用于存储用户{name:ip}
user={}

def do_login(s,name,addr):
    if name in user or name=='管理员消息':
        s.sendto('该昵称已存在'.encode(),addr)
        return
    s.sendto(b'ok',addr)
    #通知其他人
    msg = '欢迎 %s 进入聊天室'%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    #将用户加入user
    user[name]=addr

def do_chat(s,name,text):
    msg='%s:%s'%(name,text)
    for i in user:
        if i !=name:
            s.sendto(msg.encode(),user[i])

def do_quit(s,name):
    msg='%s:退出聊天室'%name
    for i in user:
            s.sendto(msg.encode(),user[i])
    del user[name]

def do_requests(s):
    while True:
        data,addr=s.recvfrom(1024)
        l=data.decode().split()
        if l[0]=='L':
            do_login(s,l[1],addr)
        elif l[0]=='C':
            # 重新组织消息内容
            text=' '.join(l[2:])
            do_chat(s,l[1],text)
        elif l[0]=='Q':
            do_quit(s,l[1])

#创建网络连接
def main():
    ADDR = ('0.0.0.0',6789)
    #创建套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)

    #创建单独进程用于发送管理员消息
    pid=os.fork()
    if pid<0:
        print('error')
    elif pid==0:
        while True:
            msg=input('管理员消息')
            msg='C 管理员消息 '+msg
            s.sendto(msg.encode(),ADDR)

    else:
        #处理各种客户端请求
        do_requests(s)


if __name__=='__main__':
    main()