from socket import *
import sys
import time

# 具体功能
class FtpClient():
    def __init__(self,s):
        self.s=s

    def check(self):
        self.s.send(b'C')  
        data=self.s.recv(128)
        if data.decode()=='ok':
            data=self.s.recv(1024).decode()
            files=data.split(',')
            for f in files:
                print(f)
        else:
            print(data.decode())

    def download(self):
        self.s.send(b'D')  
        data=self.s.recv(128)
        if data.decode()=='ok':
            while True:
                data=input('输入要下载的文件名:')
                self.s.send(data.encode())
                d=self.s.recv(1024).decode()
                if d =='文件名有误':
                    print(d)
                    continue
                f=open('./download/'+data,'wb')
                while True:
                    n=self.s.recv(1024)
                    if n.decode()=='##':
                        f.close()
                        break
                    f.write(n)
                return
        else:
            print(data.decode())
        
    def upload(self):
        self.s.send(b'U')
        while True:  
            data=input('输入要上传的文件名:')
            try:
                f=open('./download/'+data,'rb')
                self.s.send(data.encode())
                time.sleep(0.1)
            except Exception:
                print('文件不存在')
                continue
            for i in f:
                self.s.send(i)
            time.sleep(0.1)
            self.s.send(b'##')
            f.close()
            return

def menu():
    print('------选择操作项------')
    print('1,查看文件库文件')
    print('2,下载文件库文件')
    print('3,上传文件')
    print('输入other退出')



# 网络连接
def main():
    s=socket()
    try:
        s.connect(('127.0.0.1',6789))
    except Exception as e:
        print('登录失败',e)
        s.close()
    ftp=FtpClient(s)
    while True:
        menu()
        i=input('请选择:')
        if i=='1':
            ftp.check()
        elif i=='2':
            ftp.download()
        elif i=='3':
            ftp.upload()
        else:
            s.send(b'Q')
            s.close()
            break


if __name__=='__main__':
    main()
