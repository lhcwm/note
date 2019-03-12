from socket import *
import os,sys
#服务器地址
ADDR=('127.0.0.1',6789)

def send_msg(s,name):
    while True:
        try:
            text = input('发言:')
        except KeyboardInterrupt:
            text='quit'
        if text.strip()=='quit':
            msg = 'Q %s'% name
            s.sendto(msg.encode(),ADDR)
            sys.exit('退出聊天室')
            # return
        msg = 'C %s %s'%(name,text)
        s.sendto(msg.encode(),ADDR)

def recv_msg(s,name):
    while True:
        try:
            data,addr=s.recvfrom(2048)
        except KeyboardInterrupt:
            sys.exit()
        if data.decode()==name+':退出聊天室':
            sys.exit('退出聊天室')
            # return
        print('\n'+data.decode())
#创建网络连接
def main():
    s=socket(AF_INET,SOCK_DGRAM)
    while True:
        name=input('输入姓名:')
        msg='L '+name
        s.sendto(msg.encode(),ADDR)
        #等待回应
        data,addr=s.recvfrom(1024)
        if data.decode()=='ok':
            print('登陆成功')
            break
        else:
            print(data.decode())
    #创建新的进程
    pid = os.fork()
    if pid<0:
        sys.exit('error')
    elif pid ==0:
        send_msg(s,name)
    else:
        recv_msg(s,name)


if __name__=='__main__':
    main()