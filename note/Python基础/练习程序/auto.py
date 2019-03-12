# class ell:
#     #类中的函数,称之为方法
#     def __init__(self,a,b):
#         self.a=a   #属性:短半径
#         self.b=b   #属性:长半径
#     def len(self):
#         return 2*3.14*self.a+4*(self.b-self.a)
#     def area(self):
#         return 3.14*self.a*self.b

# e = ell(2,3)
# le =e.len()
# are =e.area()
# print('周长:%f,面积:%f'%(le,are))


#汽车类
import random as R
class Am:
    def __init__(self,name,color,output):
        self.name=name
        self.color=color
        self.output=output
        self.__li=0
        self.__you=6

    def start(self):
        print('启动')

    def __jli(self):
        k=R.randint(1,400)
        self.__li+=k
        return self.__li

    def get_li(self):
        return self.__li

    def run(self):
        k=self.__jli()
        y=k*self.__you/100
        print('开始行驶,行驶里程为%d,共耗油%.2f升'%(k,y))

    def stop(self):
        print('停止')

    def info(self):
        print('名称:%s,颜色:%s,排量:%.1f'%(self.name,self.color,self.output))

if __name__=='__main__':
    am=Am('家用轿车','白色',1.6)
    am.start()
    am.run()
    am.stop()
    am.info()
    a=repr(am)
    print(a)
    b=eval(a)
    print(b)
