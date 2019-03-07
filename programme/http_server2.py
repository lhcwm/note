# coding=utf-8
'''
HTTP Server v2.0
多线程并发
基本的request解析
能够反馈基本数据
实用类封装
'''

from socket import *
from threading import Thread
import sys

# 封装具体的类作为HTTP Server功能模块
class HTTPServer(object):
    def __init__(self,server_addr,static_dir):
        # 添加对象属性
        self.server_address=server_addr
        self.static_dir=static_dir
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.sockfd=socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    def bind(self):
        self.sockfd.bind(self.server_address)
        self.ip=self.server_address[0]
        self.port=self.server_address[1]

    def server_forever(self):
        self.sockfd.listen(5)
        print ('listen the port%d'%self.port)
        while True:
            try:
                connfd,addr=self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit('退出服务器')
            except Exception as e:
                print(e)
                continue
            #创建多线程处理请求
            clientThread=Thread(target=self.handle,args=(connfd,))
            clientThread.setDaemon(True)
            clientThread.start()

    # 具体处理httpd请求
    def handle(self,connfd):
        request=connfd.recv(1024)
        # 防止浏览器异常断开
        if not request:
            connfd.close()
            return
        # 请求解析
        requestHeaders=request.splitlines()
        print(connfd.getpeername(),':',requestHeaders[0])
        # 获取请求内容
        getrequest=str(requestHeaders[0]).split(' ')[1]

        if getrequest=='/' or getrequest[-5:]=='.html':
            self.get_html(connfd,getrequest)
        else:
            self.get_data(connfd,getrequest)
        connfd.close()

    def get_html(self,connfd,getrequest):
        if getrequest =='/':
            filename=self.static_dir+'/index.html'
        else:
            filename=self.static_dir+getrequest
        try:
            f=open(filename)
        except IOError:
            responseHeaders='HTTP/1.1 404 Not Found\r\n'
            responseHeaders+='\r\n'
            responsebody='sorry ,Not found the page'
        else:
            responseHeaders='HTTP/1.1 200 ok\r\n'
            responseHeaders+='\r\n'
            responsebody=f.read()
        finally:
            response=responseHeaders+responsebody
            connfd.send(response.encode())

    def get_data(self,connfd,getrequest):
        responseHeaders='HTTP/1.1 200 ok\r\n'
        responseHeaders+='\r\n'
        responsebody='<p>waiting httpserver v3.0<p>'
        response=responseHeaders+responsebody
        connfd.send(response.encode())


if __name__=='__main__':
    # 使用者自己设定addr
    server_addr=('0.0.0.0',6789)
    # 用户提供存放网页的目录
    static_dir='./static'
    # 创建服务器对象
    httpd=HTTPServer(server_addr,static_dir)
    # 启动服务
    httpd.server_forever()