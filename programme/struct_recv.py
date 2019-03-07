from socket import *
import struct
s=socket(AF_INET,SOCK_DGRAM)
s.bind(('0.0.0.0',6666))
#确定数据结构
st=struct.Struct('i4sf')
while 1:
    data,addr = s.recvfrom(1024)
    #解析数据
    data =st.unpack(data)
    print(data)

    