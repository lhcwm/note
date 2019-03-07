#多重继承示例:

class Fighter:
    def fig(self):
        print('战斗')

    def roar(self):
        print('狮吼碎金吟')

class Flyer:
    def fly(self):
        print('飞行')

    def roar(self):
        print('狮吼功')

class Firer:
    def fire(self):
        print('喷火')

class Superman(Fighter,Flyer,Firer):
    pass 

if __name__=='__main__':
    s=Superman()
    # s.fly()
    # s.fire()
    # s.fig()
    # s.roar()
    # print(Superman.__mro__)
    # print(Superman.__bases__)
    # print(Firer.__bases__)
    # a=str(s)
    # print(a)
    a=repr(s)
    print(a)
