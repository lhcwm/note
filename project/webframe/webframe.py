#!/usr/bin/env python3
#coding=utf-8

'''
模拟网站后端应用处理程序
httpserver v3.0
'''

from socket import *
# 导入配置文件
from settings import *
from select import select
import json

# 创建应用类用于具体处理请求
class Application(object):
    def __init__(self,address):
        self.ip = frame_address[0]
        self.port = frame_address[1]
        self.sockfd = socket()
        self.sockfd.bind(address)

    def start(self):
        self.sockfd.listen(10)
        print('listen the port %d'% self.port)
        rlist = [self.sockfd]
        wlist = []
        xlist = []
        while True:
            rs,ws,xs = select(rlist,wlist,xlist)
            for r in rs:
                if r is self.sockfd:
                    connfd,addr = r.accept()
                    rlist.append(connfd)
                else:
                    # 接收httpserver请求
                    request = r.recv(1024).decode()
                    if not request:
                        rlist.remove(r)
                        # r.close()
                        continue
                    self.handle(r,request)

# 处理请求
    def handle(self,connfd,request):
        request=json.loads(request)
        print(request)
        method = request['method']
        path_info = request['path_info']
        if method == 'GET':
            if path_info == '/' or path_info[-5:] == '.html':
                data = self.get_html(path_info)
            else:
                data = self.get_data(path_info)
        elif method == 'POST':
            pass

        # 根据具体返回的数据,
        if data:
            connfd.send(data.encode())
        else:
            connfd.send(b'404')
            

    def get_html(self,path_info):
        if path_info =='/':
            filename=STATIC_DIR + '/index.html'
        else:
            filename=STATIC_DIR + path_info
        try:
            f=open(filename)
        except IOError:
            print('网页打开失败')
            return
        data=f.read()
        f.close()
        return data

    def get_data(self,path_info):
        for url,func in urls:
            if path_info == url:
                return func()
        return '404'




app = Application(frame_address)
app.start() #启动后端框架服务