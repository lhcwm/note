from socket import *
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

c,addr =s.accept()
print(addr)
data =c.recv(4096)
print(data)
#组织响应http响应
dat='''HTTP/1.1 200 ok
connect_type:text/html

Hi~ o(*￣▽￣*)ブ
'''
   
c.send(dat.encode())
c.close()
s.close()