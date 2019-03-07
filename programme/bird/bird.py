# 鸟类

#  1,定义一个鸟类(Bird),具有吃(eat),飞行(fly),繁殖(reproduction)方法
#  2,定义老鹰类(Eagle),鸵鸟类(Ostrich),继承自鸟类
#  3,编写测试代码,测试

class Bird:
    def __init__(self,name,high,food,weight):
        self.name=name
        self.high=high
        self.food=food
        self.weight=weight

    def eat(self):
        print('%s在吃%s'%(self.name,self.food))

    def fly(self):
        print('%s飞离地面%.1f米'%(self.name,self.high))

    def rep(self):
        print('%s下了一个%d克的蛋'%(self.name,self.weight))
    