from socket import *
import struct
s=socket(AF_INET,SOCK_DGRAM)
addr=('127.0.0.1',6666)
while 1:
    id=int(input('id:'))
    name=input('name:')
    height=float(input('height:'))
    len=len(name)

    fmt='i4sf'
    #解析数据
    data =struct.pack(fmt,id,name.encode(),height)
    s.sendto(data,addr)
s.close()