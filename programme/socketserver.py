'使用socketServer模块完成网络并发模型'
from socketserver import *
# 创建tcp多进程并发
class Server(ForkingMixIn,TCPServer):
    pass

# 具体的请求处理
class Handle(StreamRequestHandler):
    #重写具体处理方法
    def handle(self):
        print('connect from',self.client_address)
        while True:
            data=self.request.recv(1024)
            if not data:
                break
            print(data.decode())
            self.request.send(b'ok')

server_addr=('0.0.0.0',6789)
#创建服务器对象
server =Server(server_addr,Handle)
server.serve_forever()  #启动服务