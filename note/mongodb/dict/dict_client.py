from socket import *
import sys,getpass

def menu1():
    print('''
    1,登录
    2,注册
    3,退出
    ''')

def menu2():
    print('''
    1,查单词
    2,历史记录
    3,注销''')


def main():
    HOST='127.0.0.1'
    PORT=6789
    s=socket()
    try:
        s.connect((HOST,PORT))
    except Exception as e:
        print(e)
        return
    while True:
        menu1()
        try:
            i=int(input('请选择:'))
        except Exception as e:
            print ('命令错误')
            continue
        if i==1:
            do_login(s)
            
        elif i==2:
            do_register(s)
        elif i==3:
            s.send(b'E')
            s.close()
            return
        else:
            print('输入错误')
            continue

def do_register(s):
    while True:
        name=input('用户名:')
        passwd=getpass.getpass('密码:')
        passwd1=getpass.getpass('再次输入密码:')
        if (' 'in name) or (' 'in passwd):
            print('用户名不允许有空格')
            continue
        if passwd != passwd1:
            print('两次密码不一致')
            continue
        s.send(('R'+' '+name+' '+passwd).encode())
        data=s.recv(1024).decode()
        if data=='ok':
            print('注册成功')

        elif data=='用户已存在':
            print('用户已存在')
        else:
            print('注册失败')
        return

def do_login(s):
    i1=input('输入用户名')
    p=input('输入密码')
    s.send(('I'+' '+i1+' '+p).encode())
    date=s.recv(1024).decode()
    if date =='ok':
        print('登陆成功')
        login(s,i1)  #注册成功进入二级界面
    else:
        print('登录失败,请重新登录')

def login(s,name):
    while True:
        menu2()
        try:
            i=int(input('请选择:'))
        except Exception as e:
            print ('输入错误,请重新输入')
            continue
        if i==1:
            do_query(s,name)
            
        elif i==2:
            do_hist(s,name)
        elif i==3:
            return
        else:
            print('输入错误,请重新输入')
            continue

def do_hist(s,name):
    msg='H %s'%name
    s.send(msg.encode())
    data=s.recv(1024).decode()
    if data=='ok':
        while True:
            data=s.recv(1024).decode()
            if data == '##':
                break
            print(data)
    else:
        print('没有历史记录')

def do_query(s,name):
    while True:
        word=input('输入要查询的单词')
        if not word:
            break
        s.send(('Q'+' '+name+' '+word).encode())
        data=s.recv(1024).decode()
        print(data)
                

if __name__=='__main__':
    main()