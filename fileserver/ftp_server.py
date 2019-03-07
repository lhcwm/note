from socket import *
import os,sys
import signal
import time

#全局变量
HOST='0.0.0.0'
PORT=6789
ADDR=(HOST,PORT)
FILE_PATH='/home/tarena/lhc/fileserver/'

class FtpServer():
    def __init__(self,c):
        self.c=c

    def check(self):
        file_list=os.listdir(FILE_PATH)
        if not file_list:
            self.c.send('文件库为空'.encode())
            return
        else:
            self.c.send('ok'.encode())
            time.sleep(0.1)
        f=''
        for i in file_list:
            if i[0] !='.' and os.path.isfile(FILE_PATH+i):
                f=f+i+','
        self.c.send(f.encode())

    def download(self):
        self.c.send('ok'.encode())
        time.sleep(0.1)
        while True:
            name=self.c.recv(1024).decode()
            try:
                f=open(FILE_PATH+name,'rb')
                print('打开文件成功')
                self.c.send('ok'.encode())
                time.sleep(0.1)
            except Exception:
                self.c.send('文件名有误'.encode())
                continue
            for i in f:
                self.c.send(i)
            time.sleep(0.1)
            self.c.send(b'##')
            f.close()
            return

    def upload(self):
        name=self.c.recv(1024).decode()
        if os.path.exists(FILE_PATH+name):    #判断文件名是否已存在
            self.c.send('该文件已存在'.encode())
            return
        f=open(FILE_PATH+name,'wb')
        while True:
            n=self.c.recv(1024)
            if n.decode()=='##':
                f.close()
                break
            f.write(n)
        return



def control(c):
    ftp=FtpServer(c)
    while True:
        data=c.recv(1024).decode()
        if not data or data=='Q':
            c.close()
            break
        elif data=='C':
            ftp.check()
        elif data=='D':
            ftp.download()
        elif data=='U':
            ftp.upload()

# 网络连接
def main():
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    while True:
        try:
            c,addr=s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit('服务器退出')
        except Exception as e:
            print(e)
            continue
        print('客户端连接成功',addr)
        pid=os.fork()

        if pid==0:
            s.close()
            control(c)
            sys.exit('客户端断开连接',addr)
        else:
            c.close()

if __name__=='__main__':
    main()

