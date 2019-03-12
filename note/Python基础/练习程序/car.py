#car

#继承示例

from auto import*

#定义CAR类
class Car(Am):
    pass

if __name__=='__main__':
    mycar=Car('小汽车','蓝色',1.4)
    mycar.start()
    mycar.run()
    mycar.stop()
    mycar.info()