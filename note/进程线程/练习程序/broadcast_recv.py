from socket import *
s=socket(AF_INET,SOCK_DGRAM)
#设置可以发送接收广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
#选择一个接收地址
s.bind(('0.0.0.0',9999))
while True:
    try:
        msg,addr=s.recvfrom(1024)
        print('从%s接收到广播:%s'%(addr,msg.decode()))
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)

s.close()