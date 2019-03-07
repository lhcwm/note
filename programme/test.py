#test
import AK47
import awp

ak=AK47.AK()   #实例化ak47
ak.reload()    #填弹
for x in range(11):
    ak.fire()      #开火
print('------------------------')
awp=awp.Awp()  #实例化awp对象
awp.reload()
for x in range(2):  
    awp.open() 
    awp.fire()
    awp.close()
