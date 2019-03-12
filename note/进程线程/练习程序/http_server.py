'''
http server v.1.0
接受浏览器请求
返回固定的响应内容
'''
from socket import *
#处理客户端请求
def handleClient(conn):
    print('request from',conn.getpeername())
    request=conn.recv(4096)  #接受http请求
    #将request按行分割
    request_lines=request.splitlines()
    for x in request_lines:
        print(x)
    try:
        f=open('/home/tarena/danei.html')
    except IOError:
        response='HTTP/1.1 404 Not Found\r\n'
        response+='\r\n'
        response+='-----sorry,not found------'
    else:
        response='HTTP/1.1 200 ok\r\n'
        response+='\r\n'
        response+=f.read()
    finally:
        #将结果发送给浏览器
        conn.send(response.encode())


#创建套接字
def main():
    sockfd=socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8000))
    sockfd.listen(3)
    print('listen to the port 8000')
    while True:
        conn,addr=sockfd.accept()
        handleClient(conn)  #负责具体的请求处理
        conn.close()

if __name__=='__main__':
    main()